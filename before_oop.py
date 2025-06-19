
# Tinem intr-o baza de date o lista de task-uri.
# un task are titlu, descriere, status.

# Implementam un TODO list.

tasks = []

valid_statuses = {"pending", "in_progress", "done"}

# task = {
#     "title": "Pickles",
#     "description": "Buy cucumbers and salt, and mustard seeds.",
#     "status": "pending"
# }

def add_task(title, description, status):
    # check for duplicate task title.
    for t in tasks:
        if t["title"] == title:
            # we have a duplicate task. stop the function
            return
    # create new task
    task = {
        "title": title,
        "description": description,
        "status": status
    }
    # add task to db
    tasks.append(task)

def update_status(title, new_status):
    if new_status in valid_statuses:
        for t in tasks:
            if t["title"] == title:
                t["status"] = new_status
        print("Updated task!")
    else:
        print("Status '{}' not valid!".format(new_status))

def print_tasks():
    for task in tasks:
        print(task)


add_task("Pickles", "Buy cucumbers and salt, and mustard seeds.", "in_progress")
add_task("Dishes", "Wash the dishes.", "in_progress")
add_task("Workout", "Go to the gym.", "done")
add_task("Workout", "Look for another gym.", "pending")

update_status("Dishes", "done")

print_tasks()
