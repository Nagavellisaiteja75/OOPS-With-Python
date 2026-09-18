class employee:
    employeeid="25RAA1"
    name="SAI"
    salary=1000000
def totalsalary(self,basicsalary):
    basic=basicsalary
    HRA=0.20*basicsalary
    DA=0.1*basicsalary
    totalsalary = self.basicsalary + HRA + DA
    print(totalsalary)
    
s=employee()
print(s.employeeid)
print(s.name)
print(s.salary)
