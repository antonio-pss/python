from collections import namedtuple

Employee = namedtuple('Employee', ['name', 'salary'])

employees = []

e1 = Employee(name='Antônio', salary=400)
e2 = Employee(name='Luana', salary=700)
