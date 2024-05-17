funcs = [{'Name': 'Antônio', 'Salary': 400, 'Gender': 'M'}, {'Name': 'Luana', 'Salary': 700, 'Gender': 'F'},
         {'Name': 'Alex', 'Salary': 2400, 'Gender': 'M'}, {'Name': 'Maria', 'Salary': 400, 'Gender': 'F'}]

# Filter
men = list(filter(lambda items: items['Gender'] == 'M', funcs))
women = list(filter(lambda items: items['Gender'] == 'F', funcs))

print(men)
print(women)

# Map
men_salary = sum(list(map(lambda items: items['Salary'], men)))
women_salary = sum(list(map(lambda items: items['Salary'], women)))

# Iterator For
men_salary_map = sum(items['Salary'] for items in funcs if items['Gender'] == 'M')
women_salary_map = sum(items['Salary'] for items in funcs if items['Gender'] == 'F')

print(men_salary, women_salary)
print(men_salary_map, women_salary_map)

