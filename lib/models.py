#!/usr/bin/env python3

from datetime import datetime
from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import MetaData,Column,Integer,String,DateTime,ForeignKey
# import uuid



convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)


# generating id string
# def generate_uuid():
#     return str(uuid.uuid4())


# creating employees table: these are company employees, the ones who will be taking tools
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    role = Column(String)

    # relationships
    tool_records = relationship('ToolRecords', back_populates='employee')

    def __repr__(self):
        return f"<Employee id: {self.id}, " +\
            f"Name: {self.name}, " +\
            f"Department: {self.department}, " +\
            f"Role: {self.role}"
    
    
    

# creating store employee model: these are employees that work in the store
class StoreEmployee(Base):
    __tablename__ = "store_employees"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    role = Column(String)

    tool_records = relationship('ToolRecords', back_populates='store_employee')

    def __repr__(self):
        return f"<Store Employee id: {self.id}, " +\
            f"Name: {self.name}, " +\
            f"Role: {self.role}"





# creating the tools model
class Tools(Base):
    __tablename__ = "tools"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    brand = Column(String)
    purchase_date= Column(DateTime, default = datetime.utcnow)
    no_of_tools = Column(Integer)

    tool_records = relationship('ToolRecords', back_populates='tool')
   
    def __repr__(self):
        return f"<Tools id: {self.id}, " +\
            f"Name: {self.name}, " +\
            f"Brand: {self.brand}, " +\
            f"Date Bought: {self.purchase_date}, " +\
            f"No. of Tools: {self.no_of_tools}"
    
    

# creating the tool records model: it should shows which tool was taken and by who
# serves as an association table
class ToolRecords(Base):
    __tablename__ = "toolrecords"

    id = Column(Integer,primary_key=True)
    date_taken = Column(DateTime, default= datetime.utcnow)
    date_returned = Column(DateTime)

    # foreign keys
    tool_id = Column(Integer, ForeignKey('tools.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))
    store_employee_id= Column(Integer, ForeignKey('store_employees.id'))

    # relationships
    tool = relationship('Tools', back_populates='tool_records')
    employee = relationship('Employee', back_populates='tool_records')
    store_employee = relationship('StoreEmployee', back_populates='tool_records')

    def __repr__(self):
        return f"Tool record id: {self.id}. {self.employee.name} has taken {self.tool.name} " +\
             f"at {self.date_taken}. The tool was returned on {self.date_returned} " +\
             f"{self.store_employee.name} was in charge"








    
