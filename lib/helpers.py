from models import Employee, StoreEmployee, Tools,ToolRecords
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker
from getpass import getpass


engine=create_engine('sqlite:///tools_store.db')
Session = sessionmaker(bind=engine)
session = Session()

def exit_program():
    print("Goodbye!")
    exit()
    
# employee C,R,U,D methods
def employee_list():
    employees = session.query(Employee).all()
    print(employees)

def find_employee_by_name():
    name=input("Enter the employee's name: ")
    employee = session.query(Employee).filter_by(name=name).first()
    print (employee) if employee else print(
        f"Employee {name} not found" 
    )

def find_employee_by_id():
    id = input("Enter the employee's id: ")
    employee = session.query(Employee).get(id)
    print (employee) if employee else print(
        f"Employee id: {id} not valid"
    )

def create_employee():
    name =input("Enter the new employee's name: ")
    department =input("Enter the new employee's department: ")
    role = input("Enter the new employee's role: ")

    if name or department or role:
      new_employee=Employee(name=name,department=department,role=role)
      session.add(new_employee)
      session.commit()
      print(new_employee)

    else:
        print("Warning: One or all fields are blank")

def update_employee():
    id = input("Enter the employee's id: ")
    employee =session.query(Employee).get(id)
    if employee:
        name = input("Enter the employee's new name: ")
        employee.name = name
        department = input("Enter the employee's new department: ")
        employee.department = department
        role = input("Enter the employee's new role: ")
        employee.role=role

        session.commit()
        print(employee)
    return None

def delete_employee():
    id = input("Enter the employee's id: ")
    fired_employee = session.query(Employee).get(id)
    if fired_employee:
        session.delete(fired_employee)
        session.commit()
        print(fired_employee)
    return None


# STORE EMPLOYEE C,R,U,D
def store_employee_list():
    store_employees = session.query(StoreEmployee).all()
    print(store_employees)

def find_store_employee_by_name():
    name = input("Enter the employee's name: ")
    store_employee = session.query(StoreEmployee).filter_by(name=name).first()
    print (store_employee) if store_employee else print(
        f"Store Employee {name} not found" 
    )

def find_store_employee_by_id():
    id = input("Enter the employee's id: ")
    store_employee = session.query(StoreEmployee).get(id)
    print (store_employee) if store_employee else print(
        f"Store Employee id: {id} not valid"
    )

def create_store_employee():
    name =input("Enter the new store employee's name: ")
    role = input("Enter the new store employee's role: ")

    if name or role:
      new_store_employee=StoreEmployee(name=name,role=role)
      session.add(new_store_employee)
      session.commit()
      print(new_store_employee)

    else:
        print("Warning: One or all fields are blank") 

def update_store_employee():
    id = input("Enter the employee's id: ")
    store_employee =session.query(StoreEmployee).get(id)
    if store_employee:
        name = input("Enter the store employee's new name: ")
        store_employee.name = name
        role = input("Enter the employee's new role: ")
        store_employee.role=role

        session.commit()
        print(store_employee)
    return None        

def delete_store_employee():
    id = input("Enter the employee's id: ")
    fired_store_employee = session.query(StoreEmployee).get(id)
    if fired_store_employee:
        session.delete(fired_store_employee)
        session.commit()
        print(fired_store_employee)
    return None

# TOOLS C,R,U,D
def tool_list():
    tools = session.query(Tools).all()
    print(tools)

def find_tool_by_name():
    name = input("Enter the tool name: ")
    tool= session.query(Tools).filter_by(name=name).first()
    print (tool) if tool else print(
        f"Tool {name} not found" 
    ) 

def find_tool_by_id():
    id = input("Enter the tool id: ")
    tool = session.query(Tools).get(id)
    print (tool) if tool else print(
        f"Tool id: {id} not valid"
    )    

def create_tool():
    name =input("Enter the new tool's name: ")
    brand = input("Enter the new tool's brand: ")
    no_of_tools = input("Enter the number of tools bought: ")

    if name or brand or no_of_tools:
      new_tool=Tools(name=name,brand=brand,no_of_tools=no_of_tools)
      session.add(new_tool)
      session.commit()
      print(new_tool)

    else:
        print("Warning: One or all fields are blank") 

def update_tool():
    id = input("Enter the tool's id: ")
    tool =session.query(Tools).get(id)

    if tool:
        name = input("Enter the tool's new name: ")
        tool.name = name
        brand = input("Enter brand's brand: ")
        tool.brand = brand
        no_of_tools = input("Enter the tool's number number: ")
        tool.no_of_tools = no_of_tools


        session.commit()
        print(tool)
    return None        

def delete_tool():
    id = input("Enter the tool's id: ")
    tool = session.query(Tools).get(id)
    if tool:
        session.delete(tool)
        session.commit()
        print(tool)
    return None     


#  TOOL RECORDS C,R,U,D methods
# displays the list of tool records
def records_list():
    records = session.query(ToolRecords).all()
    print(records)


# getting the tool records by id. Tool records doesn't have a name so getting the records
# id is understandable
def find_tool_records_by_id():
    id = input("Enter the tool record id: ")
    tool_record = session.query(ToolRecords).get(id)
    print (tool_record) if tool_record else print(
        f"Tool id: {id} not valid"
    ) 
    
# creating a new tool record 
def create_tool_record():
    tool_id =input("Enter the tool id of the tool taken: ")
    employee_id = input("Enter the employee id of the employee taking the tool: ")
    store_employee_id = input("Enter the store-employee _id: ")
    date_returned=None

    if tool_id or employee_id or store_employee_id:
      new_record = ToolRecords(
                        tool_id=tool_id, 
                        employee_id=employee_id, 
                        store_employee_id=store_employee_id, 
                        date_returned=date_returned)
      
      session.add(new_record)
      session.commit()
      print(new_record)

    else:
        print("Warning: One or all fields are blank") 


#only updating the date_returned on the record to show the tool was returned
def update_tool_record():
    id = input("Enter the tool record's id: ")
    tool =session.query(ToolRecords).get(id)

    if tool:
        date_returned = input("Enter the date when the tool is returned: ")
        tool.date_returned = date_returned
        session.commit()
        print(tool)
    return None    

   # I have avoided upgrading other fields, to avoid manipulation.
   # If the store clerk has access to fields, he/she maybe tempted to change records    

#deleting a tool record
# This could be in scenerio where the tool is
def delete_tool_records():

    password = getpass("Enter password: ")

    if password == "12345":
        
        id = input("Enter the tool's id: ")
        delete_tool = session.query(ToolRecords).get(id)
        if delete_tool:
            session.delete(delete_tool)
            session.commit()
            print(delete_tool)
        else:
            print("No tool to delete")    

    else:    
        print("Incorrect password")

  
    return None





  
    



