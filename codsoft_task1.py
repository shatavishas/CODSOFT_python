# Create a list to store the to-do items
tasks = []

# Define a function to add a task to the list
def add_task(task):
  tasks.append(task)

# Define a function to view the tasks in the list
def view_tasks():
  for task in tasks:
    print(task)

# Define a function to mark a task as done
def mark_task_done(task):
  tasks.remove(task)

# Define a function to exit the program
def exit_program():
  print("Goodbye!")
  exit()

# Display the main menu
def main_menu():
  print("To-Do List")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Mark a task as done")
  print("4. Exit")
while True:
  main_menu() #to start the program
  # Get the user's choice
  choice = input("Enter your choice: ")
  # Call the appropriate function based on the user's choice
  if choice == "1":
    x=input(("enter your task "))
    add_task(x)
  elif choice == "2":
    view_tasks()
  elif choice == "3":
    mark_task_done()
  elif choice == "4":
    exit_program()
  else:
    print("Invalid choice.")
