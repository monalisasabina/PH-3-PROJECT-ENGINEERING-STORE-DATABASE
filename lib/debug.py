#!/usr/bin/env python3

# debug.py:This file contains the debugger. It is used for debugging and you can also display the data on the debugging interface.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Employee,StoreEmployee, Tools,ToolRecords

if __name__ == '__main__':
    engine=create_engine('sqlite:///tools_store.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    #using ipdb as the debugger 
    import ipdb; ipdb.set_trace()