# Task 7 Problem 2

tasks=[]

def add_task (task) :
    tasks.append(task)
    print(f"Task {task} added successfully!")

def del_task (task):
    if task in tasks :
      index = tasks.index(task)
      tasks.pop(index)
      print(f"Task {task} deleted successfully!")
    else :
        print(f"Task {task} not found!")

def show_tasks ():
   for i in range (len(tasks)):
      print(f"Tasks: {tasks[i]}")

 
  

def main () :
   while True :
      print("1. Add task")
      print("2. Delete task")
      print("3. Show tasks")
      print("4. Mark Task as Completed")
      print("Enter an option:")
      gg=int(input()) 

      if gg ==1:
          task= input("Add task")
          add_task(task)
      elif gg ==2 :
         task= input("Add the task")
         del_task(task)
      elif gg==3 :
         show_tasks
      elif gg==4 :
         task_index= int(input("Add task")) -1
         if 0<=task_index<=len(tasks) :
            tasks[task_index]["done"] =True
            print("task marked done")
         else:
            print("invalid task number")
      else :
         print("Error")

      
         
   
    
main()