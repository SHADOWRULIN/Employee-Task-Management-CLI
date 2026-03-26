#program of a system for company employees to manage their task :
#where three department are avalible
CS = {"saim111":{"23/05/2024": "to compelete"},"hassan222":{"23/04/2024":"meeting to discuss how to improve task prefromance next year"}}
SE = {"fahaz222":{"04/06/2024":"deadline of submit the on research on how to capture max market","02/04/2024":"presentation on the product"}}
CE = {"fawad333":{"23/05/2024":"deadline to submit the research on leak accure"}}
#this new dict is use in to thing first to append the task in task dict second use for new user to create its task dict
new_task_dic = {}
#using this to call the above variable from user input because you can not change str to charactor
department = {"CS":CS,"SE":SE,"CE":CE}

# want to add task and date
def add():
    date = input("Enter date: ")
    value = input("Enter the task: ")
    new_task_dic[date] = value

# want to add a new task dictionary
def new_task():
    date = input("Enter date: ")
    value = input("Enter the task: ")
    new_task_dic[date] = value
def depart():
    a = input("Enter the department(CS,SE,CE): ")
    department[a.upper()]
    return department

# want to add a new user in their department
def new_user():
    username = input("enter your name: ")
    id = input("enter your id: ")
    key = username + id
    depart[key] = new_task_dic
    print("now you are registered")
    return key

#the main body of the code
while True:
    login = input("new user(yes/no): ")
    #this if going to run when the user is all ready registered and want to preform operetion
    if login.lower() == "no":
        username = input("enter your name: ")
        a = input("enter your department(CS/SE/CE): ")
        depart = department[a.upper()]
        id = input("enter your id: ")
        key = username + id
        #this while will going to enter in loop where user can prefome given operetion on there task
        while key in depart:
            want_to = input("want to (check/add/delete/change) or exit: ")
            if want_to.lower() in ["check", "add", "delete", "change", "exit"]:
                if want_to.lower() == "check":
                    check = input("to check (current task/customize/all): ")
                    if check.lower() == "customize":
                        print(depart[key][input("enter a date(dd/mm/yyyy) to check the task: ")])
                    elif check.lower() == "all":
                        all = depart[key]
                        #this for loop going to read the key and value of the dict at same time and going to print
                        for i, j in all.items():
                            print(i + "  =  " + j)
                    elif check.lower() == "current":
                        import time
                        #this time.strftime("%d/%m/%Y") use to genrate the current time
                        date = time.strftime("%d/%m/%Y")
                        if date in depart[key]:
                            print(date + " = " + depart[key][date])
                        elif date not in depart[key]:
                                print("there are no tasks for today")
                elif want_to.lower() == "add":
                    #this while loop going loop to add task as many time user want to
                    while want_to == "yes" or "add":
                        task = depart[key]
                        #this add function use to add new task
                        add()
                        task.update(new_task_dic)
                        print("new data has been added")
                        want_to = input("want to add more task(yes/no): ")
                        if want_to == "no":
                            break
                elif want_to.lower() == "delete":
                    task = input("enter date to delete that task: ")
                    if task in depart[key]:
                        del depart[key][task]
                        print("task is deleted")
                    else:
                        print("task does not exist")
                elif want_to.lower() == "change":
                    change = input("want to change task/date of task: ")
                    if change == "task":
                        date = input("enter date of that you want to change task: ")
                        if date in depart[key]:
                            depart[key][date] = input("enter a new task: ")
                            print("task is changed " + date + " = " + depart[key][date])
                        else:
                            print("task does not exist")
                    elif change == "date" or "date of task":
                        date = input("enter date which you want to change : ")
                        if date in depart[key]:
                            new_date = input("enter a new date: ")
                            depart[key][new_date] = depart[key][date]
                            del depart[key][date]
                            print("date is change " + new_date + " = " + depart[key][new_date])
                        else:
                            print("date does not exist")
            elif want_to.lower() == "exit":
                break
            #this else going to run when user give wrong input under
            # this else their is continue which will send the interpertor to ask again.
            else:
                print("Inappropiate Input")
                continue
    #this elif going run when user is new and want to register himself
    elif login.lower() == "yes":
        depart = depart()
        key = new_user()
        want_to_add = input("want to add task(yes/no): ")
        if want_to_add.lower() == "yes":
            new_task()
            want_to_add = input("want to add task(yes/no): ")
            while want_to_add.lower() == "yes":
                task = depart[key]
                add()
                #this logic help to append the new task to main main task section
                task.update(new_task_dic)
                want_to_add = input("want to add more task : ")
            if want_to_add.lower() == "no":
                print("your data is entered")
                want_to_check = input("want to check your  all data(all date) or delete particular task(delete): ")
                if want_to_check.lower() == "all data" or "all":
                    all = depart[key]
                    for i, j in all.items():
                        print("your all task")
                        print(i + "  =  " + j)
                elif want_to_check.lower() == "delete":
                    del depart[key][input("enter date to delete that task: ")]
                    print("task is deleted")
    else:
        continue