class Student:
    def __init__(self, roll, name, mark):
        self.roll = roll
        self.name = name
        self.mark = mark

class SMS:
    def __init__(self):
        self.students = []


    def add(self):
        self.students.append(Student(int(input("Roll_no:")), input("Name:"), input("mark:")))

    def display(self):
        for s in self.students:
            print(f"ID: {s.roll} | Name: {s.name} | Grade: {s.mark}")

        def search(self):
            r = int(input("Search Roll: "))
            found = [s for s in self.students if s.roll == r]
            for s in found: print(f"Found: {s.name}")
            if not found: print("Not found.")

sms = SMS()
while True:
    choice = input("\n1.Add 2.Show 3.Search 4.Exit: ")
    if choice == '1': 
        sms.add()

    elif choice == '2': 
        sms.display()

    elif choice == '3': 
        sms.search()

    elif choice == '4': 
        break
   