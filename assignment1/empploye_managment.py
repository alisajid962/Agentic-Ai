employee_names = []
employee_salary = []
employee_net_pay = []
total_payroll = 0
employees_paid = 0
budget = int(input("Enter the payroll budget: "))
n = int(input("Enter the number of employees: "))
for i in range(n):
    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    employee_names.append(name)
    employee_salary.append(salary)
for i in range(len(employee_names)):
    if employee_salary[i] == 0:
        continue
    if employee_salary[i] > 5000:
        bonus = employee_salary[i] * 0.10
    elif employee_salary[i] >= 2000:
        bonus = employee_salary[i] * 0.05
    else:
        bonus = 0
    net_pay = employee_salary[i] + bonus
    total_payroll += net_pay
    if total_payroll > budget:
        print("Budget exceeded")
        total_payroll -= net_pay
        break
    employee_net_pay.append(net_pay)
    employees_paid += 1
    print(employee_names[i], "Net Pay =", net_pay)
print("\nEmployees Paid:", employees_paid)
print("Final Payroll Total:", total_payroll)