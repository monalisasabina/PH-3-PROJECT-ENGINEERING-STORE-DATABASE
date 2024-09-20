#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Employee,Tools,StoreEmployee,ToolRecords

if __name__ == '__main__':
    engine=create_engine('sqlite:///tools_store.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Employee).delete()
    session.query(Tools).delete()
    session.query(StoreEmployee).delete()
    session.query(ToolRecords).delete()