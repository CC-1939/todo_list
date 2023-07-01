import tabulate
import sqlite3


class ToDo:

    global connect, cursor

    #trying connect to db
    try:
        connect = sqlite3.connect("todo_list_database.sqlite")
        print("[+] sucessful connect to db")
        cursor = connect.cursor()

    except Exception as err:
        # in case of error print error message
        print(f"[!!!] ERROR: {err}")

    # here create db
    def create_data_base(self):
        # trying to create db
        try:
            cursor.execute("""
                        CREATE TABLE TASKS (
                                id INTENGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                description TEXT NOT NULL,
                        );
                    """)
            connect.commit() # accept updates into db
            print("[+] DB created")

        except: # in case of error show err message
            print("[!!!] Something going wrong, may be db already already exist....")

    # this function will add data(task) to db
    def insert_into_database(self):
        task_name = input("Enter task name >> ") # get name of the task
        task_describe = input("Enter describe of task >> ") # get describe of task

        print("[!!!] Check input data:")
        print(f"Task name: {task_name}")
        print(f"Task describe: {task_describe}")

        # podtverzhdenie

        answer = input("do u agry? y/n:")
        if answer == "y": # if y add task at db
            values = [task_name, task_describe]
            try:
                cursor.execute("INSERT INTO TASKS (name, description) VALUES (?, ?)", values)
                connect.commit()

            except Exception as err:
                print(f"[!!!] Error: {err}")

           #self.show_database()
        else: # else - pass
            print("pon")
    #this function will show tasks from db
    def show_database(self):
        pass

    #this funtion will update data in db
    def update_database(self):
        pass

    #this funtion will remove data from db
    def remove_task_from_database(self):
        pass


db = ToDo()

db.create_data_base()
