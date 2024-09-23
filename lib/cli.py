# import click

from helpers import (
    exit_program, employee_list, find_employee_by_name,find_employee_by_id, create_employee, update_employee,delete_employee,
    store_employee_list,find_store_employee_by_name,find_store_employee_by_id,create_store_employee,update_store_employee,delete_store_employee,
    tool_list,find_tool_by_name,find_tool_by_id,create_tool,update_tool,delete_tool,
    records_list,find_tool_records_by_id,create_tool_record,update_tool_record,delete_tool_records
)

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1.  List all the employees")
    print("2.  Find employee by name")
    print("3.  Find employee by id")
    print("4.  Add new employee")
    print("5.  Update employee details")
    print("6.  Delete employee")
    print("7.  List all store employees")
    print("8.  Find store employee by name")
    print("9.  Find store employee by id")
    print("10. Add store employee")
    print("11. Update store employee details")
    print("12. Delete employee")
    print("13. List all tools")
    print("14. Find tool by name")
    print("15. Find tool by id")
    print("16. Add new tool")
    print("17: Update tool details")
    print("18: Delete tool")
    print("19: List all the tool records")
    print("20: Find tool record by id")
    print("21: Add new tool record")
    print("22: Update date returned")
    print("23: Delete tool record")
   
    
    

def main():
    while True:
        menu()
        choice = input(">")
        if choice == "0":
            exit_program()
        elif choice == "1":
            employee_list()
        elif choice == "2":   
            find_employee_by_name()
        elif choice == "3":
            find_employee_by_id()    
        elif choice == "4":
            create_employee()
        elif choice == "5":
            update_employee()
        elif choice == "6":
            delete_employee()
        elif choice == "7":
            store_employee_list()
        elif choice == "8":
            find_store_employee_by_name()
        elif choice == "9":    
            find_store_employee_by_id()
        elif choice == "10":
            create_store_employee()
        elif  choice == "11":
            update_store_employee()  
        elif choice == "12":
            delete_store_employee()    
        elif choice == "13":
            tool_list()
        elif choice == "14":
            find_tool_by_name()  
        elif choice == "15":
            find_tool_by_id()
        elif choice == "16":
            create_tool()    
        elif choice == "17":
            update_tool()    
        elif choice == "18":
            delete_tool()
        elif choice == "19":
            records_list()
        elif choice == "20":
            find_tool_records_by_id()    
        elif choice == "21":
            create_tool_record()  
        elif choice == "22":
            update_tool_record()    
        elif choice == "23":
            delete_tool_records()       

                

        






if __name__ == "__main__":
    main()

#..........................................................................................
# USING CLICK
 
# @click.group()
# def main():
#     """Welcome to the AAC Engineering Store!"""
#     pass

# # EMPLOYEE
# @main.command()
# def list_employees():
#     """List all the employees."""
#     employee_list()

# @main.command()
# def get_employee_name():
#     """Find employee by name."""
#     find_employee_by_name()

# @main.command()
# def get_employee_id():
#     """Find employee by id."""
#     find_employee_by_id()    

# @main.command()
# def create_new_employee():
#     """Create new employee."""
#     create_employee()     

# @main.command()
# def employee_update():
#     """Update employee."""
#     update_employee()     


# @main.command()
# def get_tool_name():
#     """Find tool by name."""
#     """List all the store employees."""
#     store_employee_list()

# @main.command()
# def get_store_employee_name():
#     """Find store employee by name."""
#     find_store_employee_by_name()   

# @main.command()
# def get_store_employee_id():
#     """Find store employee by id."""
#     find_store_employee_by_id()     

# @main.command()
# def create_new_store_employee():
#     """Create new store employee."""
#     create_store_employee()    

# @main.command()
# def store_employee_update():
#     """Update store employee."""
#     update_store_employee()     

# @main.command()
# def store_employee_delete():
#     """Delete store employee."""
#     delete_store_employee()       


# # TOOLS
# @main.command()
# def list_tools():
#     """List all the tools."""
#     tool_list()

# @main.command()
# def get_tool_name():
#     """Find tool by name."""
#     """Find tool by name."""
#     find_tool_by_name()      

# @main.command()
# def get_tool_id():
#     """Find tool by id."""
#     find_tool_by_id()      

# @main.command()
# def create_new_tool():
#     """Create new tool(s)."""
#     create_tool()       

# @main.command()
# def tool_update():
#     """Update tool."""
#     update_tool()   

# @main.command()
# def tool_delete():
#     """Delete tool."""
#     delete_tool()    

     
# # TOOL RECORDS
# @main.command()
# def list_records():
#     """List all the tool records."""
#     records_list()

# # getting the tool records by it's id is easier than by name
# @main.command()
# def get_tool_records_id():
#     """Find tool records by id."""
#     find_tool_records_by_id()     

# @main.command()
# def create_new_record():
#     """Create new record."""
#     create_tool_record()    

# @main.command()
# def tool_record_update():
#     """Update tool record."""
#     update_tool_record()       

# @main.command()
# def tool_records_delete():
#     """Delete tool record."""
#     delete_tool_records()        


# if __name__ == '__main__':
#     main()


# ........................................................................................


