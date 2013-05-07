import datetime


class Staff():
	def __init__(self,name,staff_id):
		self.__name=name
		self.__id=staff_id
		self.__salary=0
	def set_salary(self,salary):
		self.__salary=salary
		return self.__salary
	def get_salary(self):
		return self.__salary
	def display(self):

		print("Month: ", datetime.datetime.now().strftime("%b"))
		print("ID: ", self.__id)
		print("Name: ", self.__name)
		print("Salary: ", self.__salary)

class FulltimeStaff(Staff):
	def __init__(self,name,staff_id,salary):
		super().__init__(name,staff_id)
		self.set_salary(salary)
		self.__bonus=0
	def compute_salary(self):
		month=datetime.datetime.now().month
		if month==6:
			self.__bonus=self.get_salary()/2
		if month==12:
			self.__bonus=self.get_salary()
		self.set_salary(self.get_salary()+self.__bonus)
		return self.get_salary()
	def generate_payroll(self):
		self.display()
		print("Type: Full-time")
		if self.__bonus:
			print("Bonus: ", self.__bonus)
		print("")

class ParttimeStaff(Staff):
	def __init__(self,name,staff_id, daily_rate, work_days):
		super().__init__(name,staff_id)
		self.__daily_rate=daily_rate
		self.__work_days=work_days
	def compute_salary(self):
		self.set_salary(self.__daily_rate*self.__work_days)
		return self.get_salary()
	def generate_payroll(self):
		self.display()
		print("Type: Part-time")
		print("Working days: ", self.__work_days)
		print("Daily rate: ",self.__daily_rate)
		print("")

staff_list=[]
staff_list.append(ParttimeStaff("songkai",0,2,100))
staff_list.append(FulltimeStaff("shuyue",1,100))
staff_list.append(FulltimeStaff("shuyue",1,100))
for staff in staff_list:
	staff.compute_salary()
	staff.generate_payroll()
