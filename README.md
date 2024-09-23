# PH3 PROJECT: ENGINEERING STORE DATABASE
## Introduction
Welcome, this is an engineering tool database for a company, AAC. The database should help in the management of tool transactions that is by checking who has taken a certain tool and checks if the same person has returned the tool. This is a SQLAlchemy database.


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

      - ToolRecords: It creates the toolrecords table. This table maintains the relationship of the tables mentioned above to this one. It is therefore an association table. You can follow this link to check the Entity Relationship Diagram, ERB:
      https://lucid.app/lucidspark/96e090bd-abbb-48d8-8946-6ee08fde2b24/edit?beaconFlowId=CF240903351EB75F&invitationId=inv_73e3c522-d98e-4be5-9d63-1223880795b1&  page=0_0# . The table has the following columns: id, date_taken and date_returned, tool_id, employee_id, and store_employee_id.
      
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
     It consists of the sample data for the database. In the terminal in the project directory you can run  python lib/seed.py to enter the sample date in the database. Also by running the code, you will get list of the all the data on the terminal. I used the sqlalchemy query methods to display that.  Example: 
                              # displaying tool list
                              print('')
                              print('Tool list')
                              tools = session.query(Tools).all()
                              print(tools)
  
  4. debug.py: It was used for debugging and also for displaying the same data in seed.py, First you have to create an virtual environment with pipenv shell command then use command python lib/seed.py to push the data in database then run command python lib/debug.py to debug or also used it to display data by entering: session.query(Tools).all() to display the tool list.

  5. helpers.py: It consists of CRUD- Create, Read , Update and Delete functions or methods for each table in the database. First I created a session then the functions followed. The functions will be explained later.

  6. cli.py: It consists of Python code that defines the structure of the Command Line Interface,CLI. For my code i used two approaches: one, the menu() approach and click() approach. I have commented the Click approach way which I worked on earlier so the menu() approach works which I preferred using. To run the CLI, use the command lib/cli.py.
 
### CLI
  To access the as mentioned you run the command "python lib/cli.py" in the projects directory in the virtual environment(pipenv shell). You will be provided with a list of options. The CLI user should be a store employee and the person who developed the database. The CLI works hand in hand with the functions in the helpers.py file. To understand this I explain how this works with toolrecords table in the database. CRUD functions are almost similar for the other tables but I'll specify for this table.

   1. Display all the records
      - cl
   



 



<!-- GUIDE
    
    What Goes into a README?
This README should serve as a template for your own- go through the important files in your project and describe what they do. Each file that you edit (you can ignore your Alembic files) should get at least a paragraph. Each function should get a small blurb.

You should descibe your actual CLI script first, and with a good level of detail. The rest should be ordered by importance to the user. (Probably functions next, then models.)

Screenshots and links to resources that you used throughout are also useful to users and collaborators, but a little more syntactically complicated. Only add these in if you're feeling comfortable with Markdown.
    



 -->

## References
1. README: https://www.markdownguide.org/cheat-sheet/
2. Building CLI: https://www.youtube.com/watch?v=kTaqR1WyT8A
3. Using Click: https://click.palletsprojects.com/en/8.1.x/commands/#merging-multi-commands
4. Using getpass() for passwords: https://www.youtube.com/watch?v=hk3ubc1-ZGg
