#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
CWD = os.path.dirname(os.path.abspath(__file__))
from typing import Dict, Iterator, List, Optional, Union, Literal, Tuple
from tap import Tap


atom_dict_full = {12: 'Mg', 13: 'Al', 20: 'Ca', 22: 'Ti', 23: 'V', 24: 'Cr',
                  25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn',
                  31: 'Ga', 38: 'Sr', 40: 'Zr', 41: 'Nb', 42: 'Mo', 48: 'Cd',
                  49: 'In', 56: 'Ba', 58: 'Ce', 62: 'Sm', 64: 'Gd', 74: 'W'}


class CreateArgs(Tap):
    elements: List[int] = [12, 13, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 38, 56]
    # 12 13 22 23 24 25 26 27 28 29 30 31 40 41 42 48 49 58 62 64 74
    """Elements used to create database."""
    n_elements: Tuple[int, int] = (5, 10)
    """TODO"""
    n_max_occurance: int = 1
    """The maximum occurance of each element."""

    @property
    def atom_dict(self) -> Dict[int, str]:
        return {e: atom_dict_full[e] for e in self.elements}


class ImportArgs(Tap):
    input: str
    """Input data in csv format."""
    tag: str = None
    """Mark the data with arbitrary string."""
    property: str
    """The target property name."""


class ExportArgs(Tap):
    property: str = None
    """The target property name."""
    export_all: bool = False
    """export all data"""


class ActiveLearningArgs(CreateArgs):
    surrogate_model: Literal['XGBoost'] = 'XGBoost'
    """surrogate model used in active learning."""
    aquisition: Literal['greedy'] = 'greedy'
    """acquisition function used in active learning."""
    n_samples: int = 5
    """The number of samples to select."""
