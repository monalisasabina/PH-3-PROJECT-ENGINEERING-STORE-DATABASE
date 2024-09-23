# PH3 PROJECT: ENGINEERING STORE DATABASE
## Introduction
Welcome, this is an engineering tool database for a company, AAC. The database should help in the management of tool transactions that is by checking who has taken a certain tool and checks if the same person has returned the tool. 


## Project overview

### Directory
The most important files in the directory are :

  1. tools_store.db
     This is the engineering store database, where the tables employees, store_employees, tools and toolrecords are created.

  2. models.py:
     It consists of four models, namely;
      - Employee: It creates the employees table, The table consists of the company's employees and to be specific, the employees in the Technical side of the company. These could be engineers, technicians or even head of departments. The columns on the table has shows the id, name, department and role of the employee.

      - StoreEmployee: It creates the store_employees table. This table consists of the store employees only. The store employees are company employees too but I wanted them to stand out so that I can I know how assigned a tool the other employees. The columns show the id, name and role of the store employee.

      - Tools: It creates the tools table. All the tools that are entered in the database go here. The columns show the id, name, brand and the date which the tool was bought.

      - ToolRecords: It creates the toolrecords table. This table maintains the relationship of the tables mentioned above to this one. It is therefore an association table. You can follow this link to check the Entity Relationship Diagram, ERD:

      [ENGINEERING_STORE_DATABASE_ERD](https://lucid.app/lucidspark/96e090bd-abbb-48d8-8946-6ee08fde2b24/edit?beaconFlowId=CF240903351EB75F&invitationId=inv_73e3c522-d98e-4be5-9d63-1223880795b1&page=0_0#) 

      ![DATABASE_ERD](./ENGINEERING%STORE%ERD.png)
      
      The table has the following columns: id, date_taken and date_returned, tool_id, employee_id, and store_employee_id.
            
                           class ToolRecords(Base):
                             __tablename__ = "toolrecords"

                            id = Column(Integer,primary_key=True)
                            date_taken = Column(DateTime, default= datetime.utcnow)
                            date_returned = Column(String)
 
                             # foreign keys
                            tool_id = Column(Integer, ForeignKey('tools.id'))
                            employee_id = Column(Integer, ForeignKey('employees.id'))
                            store_employee_id= Column(Integer, ForeignKey('store_employees.id'))

                            # relationships
                            tool = relationship('Tools', back_populates='tool_records')
                            employee = relationship('Employee', back_populates='tool_records')
                            store_employee = relationship('StoreEmployee', back_populates='tool_records')

                            def __repr__(self):
                            return f"<Tool record id: {self.id}. {self.employee.name} has taken {self.tool.name} " +\
                            f"at {self.date_taken}. The tool was returned on {self.date_returned}" +\
                            f". {self.store_employee.name} was in charge>"

   


  3. seed.py:
     It consists of the sample data for the database. In the terminal in the project directory you can run ```$python lib/seed.py``` to enter the sample date in the database. Also by running the code, you will get list of the all the data on the terminal. I used the sqlalchemy query methods to display that.  Example: 
                          
                              python # displaying tool list
                              print('')
                              print('Tool list')
                              tools = session.query(Tools).all()
                              print(tools)
                           
  
  4. debug.py: It was used for debugging and also for displaying the same data in seed.py using ipdb, First you have to create an virtual environment with ```pipenv shell``` command then use command ```python lib/seed.py``` to push the data in database then run command ```python lib/debug.py``` to debug or also used it to display data by entering: ```session.query(Tools).all()``` to display the tool list.

  5. helpers.py: It consists of CRUD- Create, Read , Update and Delete functions or methods for each table in the database. Before the functions I have the session set up first.

  6. cli.py: It consists of Python code that defines the structure of the Command Line Interface,CLI. For my code I have used two approaches: one, the menu() approach and click() approach. I have commented the Click approach way which I worked on earlier so the menu() approach works which I preferred using. To run the CLI, use the command ```python lib/cli.py```on the terminal.
 
### CLI
  To access the as mentioned you run the command "python lib/cli.py" in the projects directory in the virtual environment(pipenv shell). You will be provided with a list of options.

  The CLI user should be a store employee and the person who developed the database. The CLI works hand in hand with the functions in the helpers.py file. 
  So I'll explain some options in the list provided to you once you access the CLI. 

   0. Exit the program
      As the option suggests. It closes the program or the CLI. You type "0", the number accompanying it, press Enter and then you'll be met with a "GoodBye!" message and the program exits.


   1. List all the employees
      This option(option 1)lists all the employees from the "employees" table in the database. Type it's menu number "1", press Enter and the list is brought. The same also applies for, "list all store employees", "list all the tools and "list all the tool records" options.

   2. Find employee by name
      This option (option 2) finds the name of the employee. When you access the option, you'll be told enter the employees name as stored in the 'employees' table. When you put a wrong name or the name is written in the wrong format, you'll be met by an error message.
      'find by name' option also applies the same for the store employees and tools stored in the database.

   3. Find employee by id
      This option finds the employees in the database by their id number. This is a much better option than finding their names. It is also faster since you only type a number(id) as opposed to writing their full names. 
      So by accessing this option(option 3), you'll be prompted to enter the id number, press Enter and the employee details are brought.
      'find by id' option works the same for store employee, tools and tool records.

   4. Add new employee
      A new employee who is hired in the company, is added in the store database using this option. When you access it(option 4), you'll be prompted to add the new employees name, department and role(position).
      The other 'add something' options  in the CLI almost work in the same way. They add the necessary details.

   5. Update employee detail
      This option (option 5)is used when may be the employee's name was registered differently, may be the employee's role was changed. So it basically changes a detail or two on the employee who was stored in the database.
      Other 'update' options work the same way.
      The 'Update date returned' option 22, works differently. It is used to update the date_returned column in the 'toolrecords' table. When a tool is returned, use this option put the date the tool was returned.

   6.  Delete employee
       This option(option 6) deletes an employee from the database. The employee could be fired or resigned so using this option deletes them from the database. The same also applies for the store employees.
       The delete tool option deletes the tool from the database. This could be may be if the tool is completely spoilt or if it were stolen.
       The 'delete tool record" option is password protected. You'll be asked to enter a password (for project:12345). This should be ideally for the store manager for security purposes.

   
## References
1. README: https://www.markdownguide.org/cheat-sheet/
2. Building CLI: https://www.youtube.com/watch?v=kTaqR1WyT8A
3. Using Click: https://click.palletsprojects.com/en/8.1.x/commands/#merging-multi-commands
4. Using getpass() for passwords: https://www.youtube.com/watch?v=hk3ubc1-ZGg
