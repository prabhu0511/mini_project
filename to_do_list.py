tasks=[]

while True:
    print("\n 1.Add Task")
    print("2.view Task")
    print("3.Exit")

    choice = input("enter choice : ")

    if choice =="1":
        task = input("enter task :")
        tasks.append(task)
        print("Task added")

    elif choice =="2":
        print("your tasks:")
        for t in tasks:
            print("-",t)

    elif choice =="3":
        break

    else:
        print("not an proper input : ")