import time

medicines = []

def add_medicine():
    name = input("Enter medicine name: ")
    time_input = input("Enter time (HH:MM in 24hr): ")
    
    medicines.append({"name": name, "time": time_input})
    print("Medicine added!\n")

def view_medicines():
    if not medicines:
        print("No medicines added.\n")
        return
    
    print("\nYour Medicines:")
    for med in medicines:
        print(f"{med['name']} at {med['time']}")
    print()

def check_reminder():
    print("Reminder system started... (Press Ctrl+C to stop)\n")
    try:
        while True:
            current_time = time.strftime("%H:%M")
            
            for med in medicines:
                if med["time"] == current_time:
                    print(f"\n Time to take: {med['name']} \n")
            
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nReminder stopped.\n")

while True:
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Start Reminder")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        add_medicine()
    elif choice == "2":
        view_medicines()
    elif choice == "3":
        check_reminder()
    elif choice == "4":
        break
    else:
        print("Invalid choice\n")