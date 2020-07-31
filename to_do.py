print("Hello, There create a tast list: ")

# collect Task name
task_list = [input("Name your tasks : \n>>")]

#collect Date and time
date_ = input("time limit \n>>")
time_ = input("time limit \n>>")

# print taks lists
print(list(enumerate(task_list)), date_, time_, sep="\t")

# delete a completed task