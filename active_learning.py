#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tqdm import tqdm
import sys
import pandas as pd
import numpy as np
from xgboost import XGBClassifier, XGBRegressor
from alhesos.args import ActiveLearningArgs
from alhesos.database.models import *


def get_X_y(p: str, atom_dict: Dict[int, str]):
    samples = []
    samples_test = []
    for sample in session.query(Sample):
        if sample.properties is None:
            samples_test.append(sample)
        elif json.loads(sample.properties).get(p) is not None:
            samples.append(sample)
        else:
            samples_test.append(sample)
    # training
    atom_list = [sample.get_atom_list() for sample in samples]
    tag = [sample.tag if sample.tag is not None else 'None'
              for sample in samples]
    prop = [json.loads(sample.properties)[p] for sample in samples]
    df = pd.DataFrame({'atom_list': atom_list, p: prop,
                       'tag': tag})
    for an, name in atom_dict.items():
        df[name] = df.atom_list.apply(lambda x: x.count(an) / len(x))
    # test
    atom_list = [sample.get_atom_list() for sample in samples_test]
    df_test = pd.DataFrame({'atom_list': atom_list})
    for an, name in atom_dict.items():
        df_test[name] = df_test.atom_list.apply(lambda x: x.count(an) / len(x))
    return df[atom_dict.values()], df[p], df_test[atom_dict.values()], df_test['atom_list'].apply(json.dumps)


def active_learning(args: ActiveLearningArgs):
    # stable
    X, y, X_test, test_atom_list = get_X_y(p='purity', atom_dict=args.atom_dict)
    clf = XGBClassifier(n_estimators=100, use_label_encoder=False).fit(X, y)
    df = X_test.copy()
    df['atom_list'] = test_atom_list
    df['proba_0'] = clf.predict_proba(X_test)[:, 0]
    df['proba_1'] = clf.predict_proba(X_test)[:, 1]
    df = df[df['proba_1'] > 0.5].reset_index(drop=True)
    X_stable = df[args.atom_dict.values()]
    #
    X, y, _, _ = get_X_y(p='T90', atom_dict=args.atom_dict)
    model = XGBRegressor().fit(X, y)
    y_pred = model.predict(X_stable)
    df['T90_pred'] = y_pred
    idx = np.argsort(y_pred)[:args.n_samples]
    df = df.iloc[idx]
    df[['atom_list', 'proba_0', 'proba_1', 'T90_pred']].to_csv('al.csv', index=False, float_format='%.4f')


if __name__ == '__main__':
    active_learning(args=ActiveLearningArgs().parse_args())
