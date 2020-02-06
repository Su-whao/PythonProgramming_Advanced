# -*- coding: utf-8 -*-

class Company(object):
    def __init__(self, employee_lst):
        self.employee = employee_lst
        
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

company = Company(["tom", "bob", "jane"])
company1 = company[:2]
print(len(company1))

for em in company:
    print(em)