#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from alhesos.args import ExportArgs
from alhesos.database.models import *


def export(args: ExportArgs):
    samples = []
    for sample in session.query(Sample):
        if args.export_all:
            samples.append(sample)
            print(len(samples))
            continue
        if sample.properties is None:
            continue
        if json.loads(sample.properties).get(args.property) is not None:
            samples.append(sample)
    atom_list = [sample.get_atom_list() for sample in samples]
    tag = [sample.tag if sample.tag is not None else 'None'
           for sample in samples]
    if args.property is None:
        df = pd.DataFrame({'atom_list': atom_list,
                           'tag': tag})
    else:
        p = [json.loads(sample.properties)[args.property] for sample in samples]
        df = pd.DataFrame({'atom_list': atom_list, args.property: p,
                           'tag': tag})
    df.atom_list = df.atom_list.apply(lambda x: ','.join(list(map(str, x))))
    df.to_csv('data.txt', index=False)


if __name__ == '__main__':
    export(args=ExportArgs().parse_args())
