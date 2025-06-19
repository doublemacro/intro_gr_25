
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
            print("Duplicate task! '{}'".format(title))
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

        # only show "Updated task!" if a task has actually been updated, and not if we are given an invalid title.
        has_been_updated = False

        for t in tasks:
            if t["title"] == title:
                t["status"] = new_status
                has_been_updated = True
        if has_been_updated:
            print("Updated task '{}'!".format(title))
        else:
            print("Task '{}' not found!".format(title))
    else:
        print("Status '{}' not valid!".format(new_status))

def remove_task(title):
    # Remove task from our db.
    for task in tasks:
        if task["title"] == title:
            # Found task. Now delete from db.
            tasks.remove(task)
            print("Task '{}' has been deleted!".format(title))

def list_tasks_by_status(status):
    # Return all tasks that have the given status
    if status in valid_statuses:
        # Method 1:
        # filtered_tasks = []
        # for task in tasks:
        #     if task["status"] == status:
        #         filtered_tasks.append(task)

        # Method 2
        filtered_tasks = list(filter(lambda t: t["status"] == status, tasks))
        return filtered_tasks
    else:
        print("Status '{}' invalid!".format(status))
        return []

def print_tasks():
    for task in tasks:
        print(task)


add_task("Pickles", "Buy cucumbers and salt, and mustard seeds.", "in_progress")
add_task("Dishes", "Wash the dishes.", "in_progress")
add_task("Workout", "Go to the gym.", "done")
add_task("Work", "Annotate data.", "in_progress")
add_task("School", "Receive diploma.", "pending")
add_task("Life", "Get married.", "pending")
add_task("Life2", "Relax a bit.", "in_progress")

add_task("Workout", "Look for another gym.", "pending")

update_status("Dishes", "done")
update_status("Play", "done")
remove_task("Dishes")

# print_tasks()
print(list_tasks_by_status("in_progress"))
