#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Employee,Tools,StoreEmployee,ToolRecords,Base,datetime


if __name__ == '__main__':

    # setting up the session
    engine=create_engine('sqlite:///tools_store.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # creating all the tables
    Base.metadata.create_all(engine)

    # avoiding repetition of data when entering data in the database
    session.query(Employee).delete()
    session.query(Tools).delete()
    session.query(StoreEmployee).delete()
    session.query(ToolRecords).delete()


# creating data

    # employee list
    monalisa = Employee(name='Monalisa Onyango', department='Electrical',role='Engineer')
    sharon = Employee(name='Sharon Odhiambo', department ='Electrical', role='Engineer')
    daniel = Employee(name = 'Daniel Kamau', department='Electrical', role ='Technician')
    joshua = Employee(name='Joshua Caleb', department='Mechanical',role='Chief Welder')
    manu = Employee(name='Emmanuel Smith', department='Mechanical',role='Head of Department')
    simon = Employee(name='Simon Washington', department='Mechanical',role='Engineer')
    
    session.add_all([monalisa,sharon,daniel,joshua,manu,simon])
    session.commit()
    

    # store employees list
    fauz = StoreEmployee(name="Fauz Mohammed",role="Store Manager")
    ruth = StoreEmployee(name="Ruth Ng'ang'a", role="Store Clerk")
    joseph =StoreEmployee(name="Jennifer Mumo", role="Store Clerk")
    elizabeth = StoreEmployee(name="Elizabeth Kipkorir", role="Intern")
    jane = StoreEmployee(name="Jane Ouma", role="Intern")
    
    session.add_all([fauz,ruth,joseph,elizabeth,jane])
    session.commit()




    #tool list
    pliers = Tools(name='Pliers', brand='Stanley', no_of_tools=5) 
    digital_multimeter= Tools(name='Digital multimeter', brand='Fluke', no_of_tools=3)
    welding_machine = Tools(name='Welding machine', brand='Licoln Electric', no_of_tools=3)
    screw_driver = Tools(name='Screw Drivers set', brand='Stanley', no_of_tools=7)
    hammer = Tools(name='Hammer', brand='Craftsman', no_of_tools=5)  
    tape_measure = Tools(name='Tape Measure', brand='Lufkin', no_of_tools=10)

    session.add_all([pliers,digital_multimeter,welding_machine,screw_driver,hammer,tape_measure]) 
    session.commit()  


# records list
    # added record: The tool_id 1 is taken by employee 1, assigned by store_employee 1
    record1=ToolRecords(
        date_returned=None, 
        tool_id= 1,
        employee_id=1,
        store_employee_id=1
    )

    record2 =ToolRecords(
        date_returned=datetime(2024,9,21),
        tool_id=1,
        employee_id=1,
        store_employee_id=1
    )

    session.add_all([record1,record2])
    session.commit()

    #  TESTING
    # displaying employee list
    print('')
    print('Employee list')
    employees = session.query(Employee).all()
    print(employees)

    # displaying store employee list
    print('')
    print('Store Employee list')
    store_employees = session.query(StoreEmployee).all()
    print(store_employees)

    # displaying tool list
    print('')
    print('Tool list')
    tools = session.query(Tools).all()
    print(tools)

    # displaying tool records list
    print('')
    print('Tool Records list')
    records = session.query(ToolRecords).all()
    print(records)














