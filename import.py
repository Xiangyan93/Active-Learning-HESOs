#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tqdm import tqdm
import pandas as pd
from alhesos.args import ImportArgs, atom_dict_full
from alhesos.database.models import *


def import_data(atom_list, target, property='target', atom_ratio=None,
                tag=None):
    atom_dict = atom_dict_full
    name = [atom_dict[a] for a in atom_list]
    if atom_ratio is None:
        atom_ratio = [1] * len(name)
    s = session.query(Sample).filter_by(**dict(zip(name, atom_ratio))).first()
    if s.properties is None:
        s.properties = json.dumps({property: target})
    else:
        p = json.loads(s.properties)
        if property in p:
            p[property] = target
            s.properties = json.dumps(p)
        else:
            s.properties = json.dumps(dict(p, **{property: target}))
    if tag is not None:
        s.tag = tag


def main(args: ImportArgs, atom_dict_full):
    df = pd.read_csv(args.input)
    for a in df['atom_list']:
        print(a.split(','))
    atom_dict_full = {v: k for k, v in atom_dict_full.items()}
    def f(x):
        if x in atom_dict_full:
            return atom_dict_full[x]
        else:
            return int(x)
    df['atom_list'] = df['atom_list'].apply(lambda x: list(map(f, x.split(','))))
    tqdm.pandas()
    df.progress_apply(lambda x: import_data(x['atom_list'], x[args.property],
                                            property=args.property,
                                            tag=args.tag),
                      axis=1)
    session.commit()


if __name__ == '__main__':
    main(args=ImportArgs().parse_args(), atom_dict_full=atom_dict_full)
