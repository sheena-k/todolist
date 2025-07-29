tasks =[]

def add_task(task_description):
    tasks.append({"task":task_description,"completed":False})

def get_task():
    return tasks

def mark_complete(index):
    if 0<=index<len(tasks):
        tasks[index]["completed"]=True

def delete_task(index):
    if 0<=index<len(tasks):
        del tasks[index]


