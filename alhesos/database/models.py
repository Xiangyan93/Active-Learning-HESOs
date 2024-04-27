#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Database engine
"""
from typing import Dict, Iterator, List, Optional, Union, Literal, Tuple
import os
import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, exists, and_
from sqlalchemy import Column, Integer, Float, Text, Boolean, String, ForeignKey, UniqueConstraint
CWD = os.path.dirname(os.path.abspath(__file__))

Base = declarative_base()
metadata = Base.metadata

db_file = 'sqlite:///%s/../../database/hesos.db' % CWD

engine = create_engine(db_file, echo=False)
Session = sessionmaker(engine)
session = Session()


class Sample(Base):
    __tablename__ = 'sample'
    id = Column(Integer, primary_key=True)
    Mg = Column(Integer, default=0)
    Ca = Column(Integer, default=0)
    Ti = Column(Integer, default=0)
    V = Column(Integer, default=0)
    Cr = Column(Integer, default=0)
    Mn = Column(Integer, default=0)
    Fe = Column(Integer, default=0)
    Co = Column(Integer, default=0)
    Ni = Column(Integer, default=0)
    Cu = Column(Integer, default=0)
    Zn = Column(Integer, default=0)
    Al = Column(Integer, default=0)
    Ba = Column(Integer, default=0)
    Sr = Column(Integer, default=0)
    tag = Column(Text)
    properties = Column(Text)

    def get_atom_list(self):
        atom_list = [12] * self.Mg + [13] * self.Al + [20] * self.Ca + \
                    [22] * self.Ti + [23] * self.V + [24] * self.Cr + \
                    [25] * self.Mn + [26] * self.Fe + [27] * self.Co + \
                    [28] * self.Ni + [29] * self.Cu + [30] * self.Zn + \
                    [38] * self.Sr + [56] * self.Ba
        return atom_list

    def get_property(self, property: Literal['purity', 'T90']):
        if self.properties is None:
            return None
        else:
            return json.loads(self.properties)[property]


metadata.create_all(engine)
