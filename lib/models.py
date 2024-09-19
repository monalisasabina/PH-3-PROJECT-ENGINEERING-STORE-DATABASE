#!/usr/bin/env python3

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

engine=create_engine('sqlite:///tools_store.db')

Base=declarative_base()