class Employee:
    def __init__(self, name, contract_type=None, salary=0, hourly_rate=0, hours_worked=0, commission_type=None, commission=0):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.commission_type = commission_type
        self.commission = commission

    def get_pay(self):
        if self.contract_type == 'salary':
            base_pay = self.salary
        elif self.contract_type == 'hourly':
            base_pay = self.hourly_rate * self.hours_worked

        if self.commission_type == 'bonus':
            total_pay = base_pay + self.commission
        elif self.commission_type == 'contract':
            total_pay = base_pay + (self.commission * self.hours_worked)
        else:
            total_pay = base_pay

        return total_pay

    def __str__(self):
        description = f"{self.name} works on a "
        if self.contract_type == 'salary':
            description += f"monthly salary of {self.salary}. "
        elif self.contract_type == 'hourly':
            description += f"contract of {self.hours_worked} hours at {self.hourly_rate}/hour. "

        if self.commission_type == 'bonus':
            description += f"They receive a bonus commission of {self.commission}. "
        elif self.commission_type == 'contract':
            description += f"They receive a commission for {self.hours_worked} contract(s) at {self.commission}/contract. "

        description += f"Their total pay is {self.get_pay()}."
        return description


billie = Employee('Billie', contract_type='salary', salary=4000)
charlie = Employee('Charlie', contract_type='hourly', hourly_rate=25, hours_worked=100)
renee = Employee('Renee', contract_type='salary', salary=3000, commission_type='contract', commission=200)
jan = Employee('Jan', contract_type='hourly', hourly_rate=25, hours_worked=150, commission_type='contract', commission=220)
robbie = Employee('Robbie', contract_type='salary', salary=2000, commission_type='bonus', commission=1500)
ariel = Employee('Ariel', contract_type='hourly', hourly_rate=30, hours_worked=120, commission_type='bonus', commission=600)
