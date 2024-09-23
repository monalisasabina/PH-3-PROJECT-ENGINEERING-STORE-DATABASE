from models import Employee, StoreEmployee, Tools,ToolRecords
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker
from getpass import getpass

# Setting up a session
engine=create_engine('sqlite:///tools_store.db')
Session = sessionmaker(bind=engine)
session = Session()

# Method shuts down the CLI
def exit_program():
    print("Goodbye!")
    exit()
    
# Employee C,R,U,D methods.
# Method displays the list of employees in the store's data database.
def employee_list():
    employees = session.query(Employee).all()
    print(employees)

# Method finds the name of an employee in the database.
def find_employee_by_name():
    name=input("Enter the employee's name: ")
    employee = session.query(Employee).filter_by(name=name).first()
    print (employee) if employee else print(
        f"Employee {name} not found" 
    )

# Method finds the employee's id in the store database.
def find_employee_by_id():
    id = input("Enter the employee's id: ")
    employee = session.query(Employee).get(id)
    print (employee) if employee else print(
        f"Employee id: {id} not valid"
    )

# Method adds a new employee in the store database.
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
        # The warning is given out if one or all fields were left blank.
        print("Warning: One or all fields are blank")

# Method updates an employees credentials in the store database.
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

# Method deletes an employee from the store database.
def delete_employee():
    id = input("Enter the employee's id: ")
    delete_employee = session.query(Employee).get(id)
    if delete_employee:
        session.delete(delete_employee)
        session.commit()
        print(delete_employee)
    return None



# STORE EMPLOYEE C,R,U,D
# Method displays a list of store employees int the store database.
def store_employee_list():
    store_employees = session.query(StoreEmployee).all()
    print(store_employees)

# Method finds a store employee by name.
def find_store_employee_by_name():
    name = input("Enter the employee's name: ")
    store_employee = session.query(StoreEmployee).filter_by(name=name).first()
    print (store_employee) if store_employee else print(
        f"Store Employee {name} not found" 
    )

# Method finds the store employees id. 
def find_store_employee_by_id():
    id = input("Enter the employee's id: ")
    store_employee = session.query(StoreEmployee).get(id)
    print (store_employee) if store_employee else print(
        f"Store Employee id: {id} not valid"
    )

# Method adds a new store employee.
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

# Method updates the store employee credentials.
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

# Method deletes a store employee in the database.
def delete_store_employee():
    id = input("Enter the employee's id: ")
    fired_store_employee = session.query(StoreEmployee).get(id)
    if fired_store_employee:
        session.delete(fired_store_employee)
        session.commit()
        print(fired_store_employee)
    return None


# TOOLS C,R,U,D
# Method displays a list of tools stored in the database.
def tool_list():
    tools = session.query(Tools).all()
    print(tools)

# Method finds the tool in the database by name.
def find_tool_by_name():
    name = input("Enter the tool name: ")
    tool= session.query(Tools).filter_by(name=name).first()
    print (tool) if tool else print(
        f"Tool {name} not found" 
    ) 

# Method finds the tool by the id number.
def find_tool_by_id():
    id = input("Enter the tool id: ")
    tool = session.query(Tools).get(id)
    print (tool) if tool else print(
        f"Tool id: {id} not valid"
    )    

# Method adds new tools in the database.
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

# Method updates a tool credentials stored in the database.
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

# Method deletes tool from the database
def delete_tool():
    id = input("Enter the tool's id: ")
    tool = session.query(Tools).get(id)
    if tool:
        session.delete(tool)
        session.commit()
        print(tool)
    return None     


#  TOOL RECORDS C,R,U,D methods
# Method displays the list of tool records
def records_list():
    records = session.query(ToolRecords).all()
    print(records)


# Method gets the tool records by id. Tool records doesn't have a name so getting the records
# id is understandable
def find_tool_records_by_id():
    id = input("Enter the tool record id: ")
    tool_record = session.query(ToolRecords).get(id)
    print (tool_record) if tool_record else print(
        f"Tool id: {id} not valid"
    ) 
    
# Method adds a tool record in the database.
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

    # The date_returned is set to None cause initially when a tool is taken, its not returned immediately.


#Method only updates the date_returned on the record to show when the tool was returned.
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
   # If the store clerk has access to fields, he/she maybe tempted to change records.    

#Method deletes a tool record.
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

    # The password is only available to the store manager





  
    



