print("Welcome to Employee Attendance System!\n ")

name = input("Write your employee name:")

class Employee:
    def __init__(self, name, id,attendance_status):
        self.name = name
        self.id = id
        self.attendance =attendance_status.capitalize()

    def mark_attendance(self):
        if self.attendance.capitalize() == "Present":
            return"You're already Present!"
        else:
            return"You're absent!"


    def display(self):
        print(f"{self.name} under id no. {self.id} is {self.attendance}" )

class AttendanceSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def mark_attendance_of_employee(self):
        print("\nAttendance of employee is done")
        for employee in self.employees:
            employee.mark_attendance()

    def view_daily_report(self):
        for employee in self.employees:
             employee.display()



system =AttendanceSystem()

while True:
    print("\nMENU")
    print("1. Add employee")
    print("2. View daily report")
    print("3. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        name = input("Employee Name: ")
        emp_id = input("Employee ID: ")
        attendance_status = input("Attendance Status (Present/Absent): ")
        emp = Employee(name, emp_id, attendance_status)
        system.add_employee(emp)
        print(emp.mark_attendance())

    elif choice == 2:
        system.view_daily_report()

    else:
        print("Invalid choice")
        break

