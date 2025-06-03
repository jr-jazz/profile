import csv
import datetime


class Employee_Database:
    def __init__(self):
        self.employees = ["Sam", "Alex", "Henry", "Julie", "Jenny"]
        self.benefits = {
            "Sam": {"Insurance": True, "50% Discount on other outlets": True, "Paid Holiday": 10},
            "Jenny": {"Insurance": True, "50% Discount on other outlets": True, "Paid Holiday": 15},
            "Alex": {"Insurance": True, "50% Discount on other outlets": True, "Paid Holiday": 12},
            "Henry": {"Insurance": True, "50% Discount on other outlets": True, "Paid Holiday": 18},
            "Julie": {"Insurance": True, "50% Discount on other outlets": True, "Paid Holiday": 10}
        }
        self.employee_rota = [
            {"name": "Sam",
             "availability": {"Monday": True, "Tuesday": True, "Wednesday": False, "Thursday": False, "Friday": True,
                              "Saturday": True, "Sunday": True}},
            {"name": "Jenny",
             "availability": {"Monday": True, "Tuesday": True, "Wednesday": True, "Thursday": True, "Friday": True,
                              "Saturday": False, "Sunday": False}},
            {"name": "Alex",
             "availability": {"Monday": True, "Tuesday": False, "Wednesday": True, "Thursday": True, "Friday": False,
                              "Saturday": True, "Sunday": True}},
            {"name": "Henry",
             "availability": {"Monday": False, "Tuesday": True, "Wednesday": False, "Thursday": True, "Friday": True,
                              "Saturday": True, "Sunday": True}},
            {"name": "Julie",
             "availability": {"Monday": False, "Tuesday": True, "Wednesday": True, "Thursday": True, "Friday": False,
                              "Saturday": True, "Sunday": True}},
        ]
        self.shifts = [
            {"day": "Monday", "required": 2},
            {"day": "Tuesday", "required": 3},
            {"day": "Wednesday", "required": 2},
            {"day": "Thursday", "required": 2},
            {"day": "Friday", "required": 3},
            {"day": "Saturday", "required": 3},
            {"day": "Sunday", "required": 3},
        ]
        self.shift_allotment = {}

    def attendance_record(self):
        print("Valid employee names are:", self.employees)
        attendance = {}
        employees_lower = {name.lower(): name for name in self.employees}

        while True:
            name = input("Enter employee name (or 'done' to finish): ").strip().lower()
            if name == "done":
                break
            elif name in employees_lower:
                original_name = employees_lower[name]
                attendance[original_name] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"Recorded attendance for {original_name} at {attendance[original_name]}")
            else:
                print(f"{name} is not a valid employee name. Valid employee names are:", self.employees)

        if attendance:
            with open('employee_attendance.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                for name, time in attendance.items():
                    writer.writerow([time, name])
                    print(f"Written to file: {time}, {name}")
            print(f"Attendance recorded for {len(attendance)} employees.")
        else:
            print("No attendance to record.")

    def rota(self):
        self.shift_allotment = {}
        for shift in self.shifts:
            employee_shift = []
            for employee in self.employee_rota:
                if shift["day"] in employee["availability"] and employee["availability"][shift["day"]] and len(
                        employee_shift) < shift["required"]:
                    employee_shift.append(employee["name"])
                    if shift["day"] not in self.shift_allotment:
                        self.shift_allotment[shift["day"]] = {}
                    self.shift_allotment[shift["day"]][employee["name"]] = "Whole Day"
            print(f"Allocated Whole Day shift on {shift['day']} to: {', '.join(employee_shift)}")

    def employee_benefits(self):
        print("Valid employee names are:", self.employees)
        name = input("Enter your name: ").strip().title()
        if name in self.benefits:
            print(f"Benefits for {name}:")
            for benefit, value in self.benefits[name].items():
                if benefit == "Insurance":
                    print(f"  {benefit.title()}: {'Yes' if value else 'No'}")
                elif benefit == "50% Discount on other outlets":
                    print(f"  {benefit.title()}: {'Yes' if value else 'No'}")
                elif benefit == "Paid Holiday":
                    print(f"  {benefit.title()}: {value} days")
        else:
            print(f"Sorry, {name} is not in our system. Valid employee names are:", self.employees)

    def main_menu(self):
        while True:
            print("Employee Menu:")
            print("  1. Take Attendance")
            print("  2. Check ROTA")
            print("  3. Employee Benefits")
            print("  4. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.attendance_record()
            elif choice == "2":
                self.rota()
            elif choice == "3":
                self.employee_benefits()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")


print("Employee Names:", ["Sam", "Alex", "Henry", "Julie", "Jenny"])

if __name__ == "__main__":
    system = Employee_Database()
    system.main_menu()
