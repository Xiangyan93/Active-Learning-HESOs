#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tqdm import tqdm
import sys
from itertools import combinations, product
from alhesos.args import CreateArgs
from alhesos.database.models import *


def IsValidList(v):
    Nmax = max(v)
    if Nmax == 1:
        return True

    factors = list(range(2, Nmax + 1))
    for i in v:
        for j in factors:
            if i % j != 0:
                factors.remove(j)
        if not factors:
            return True
    return False


def create(args: CreateArgs):
    atom_dict = args.atom_dict
    # contain 5-11 types of metal atom
    n = 0
    for i in range(5, 11):
        print("\nProcessing %i-components" % i)
        compositions = [c for c in list(product(range(1, args.n_max_occurance + 1), repeat=i)) if IsValidList(c)]
        combination = list(combinations(atom_dict.values(), i))
        for j, an in tqdm(enumerate(combination), total=len(combination)):
            n += len(compositions)
            for c in compositions:
                sample = Sample(**dict(zip(an, c)))
                session.add(sample)
                n += 1
    session.commit()


if __name__ == '__main__':
    create(args=CreateArgs().parse_args())
