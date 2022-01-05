class Emp:

	raise_amt = 1.04
	num_of_emps = 0
	def __init__(self,first, last,pay):
		self.first = first
		self.last =  last
		self.email =  f'{first}.{last}@compay.com'
		self.pay =  pay

		Emp.num_of_emps += 1

	def fullname(self):
		return f'{self.first} {self.last}"
	
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

print(Emp.num_of_emps)

emp_1 = Emp('John','K',500.30)
emp_2 = Emp('Jane','M', 60000)