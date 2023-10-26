
class Employee:
    def __init__(self, code, name, base_salary, days_worked):
        self.code = code
        self.name = name
        self.base_salary = base_salary
        self.days_worked = days_worked
    def calculate_monthly_salary(self):
        employee_type = self.code[0]
        years_worked = int(self.code[1:3])

        coefficient = 0
        if employee_type == 'A':
            if years_worked >=1 and years_worked <=3 :coefficient = 10
            elif years_worked >=4 and years_worked <=8 :coefficient = 12
            elif years_worked >=9 and years_worked <=15 :coefficient = 14
            elif years_worked >=16  :coefficient = 20
        elif employee_type == 'B':
            if years_worked >=1 and years_worked <=3 :coefficient = 10
            elif years_worked >=4 and years_worked <=8 :coefficient = 11
            elif years_worked >=9 and years_worked <=15 :coefficient = 13
            elif years_worked >=16  :coefficient = 16
        elif employee_type == 'C':
            if years_worked >=1 and years_worked <=3 :coefficient = 9
            elif years_worked >=4 and years_worked <=8 :coefficient = 10
            elif years_worked >=9 and years_worked <=15 :coefficient = 12
            elif years_worked >=16  :coefficient = 14
        elif employee_type == 'D':
            if years_worked >=1 and years_worked <=3 :coefficient = 8
            elif years_worked >=4 and years_worked <=8 :coefficient = 9
            elif years_worked >=9 and years_worked <=15 :coefficient = 11
            elif years_worked >=16  :coefficient = 13

        monthly_salary = (self.base_salary * self.days_worked * coefficient) * 1000
        return monthly_salary

n1 = int(input())
departments = {}
for _ in range(n1):
    s=input()
    code = s[0:2]
    name = s[3:]
    departments[code] = name


n2 = int(input())
employees = []
for _ in range(n2):
    employee_code = input()
    employee_name = input()
    base_salary = int(input())
    days_worked = int(input())

    employee = Employee(employee_code, employee_name, base_salary, days_worked)
    employees.append(employee)

# In thông tin bảng lương
for employee in employees:
    department_name = departments.get(employee.code[3:])
    monthly_salary = employee.calculate_monthly_salary()
    print(f"{employee.code} {employee.name} {department_name} {int(monthly_salary)}")
