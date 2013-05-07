class Account():
	def __init__(self, pid, balance):
		self.__id=pid
		self.__balance=balance
	def get_account_no(self):
		return self.__id
	def get_balance(self):
		return self.__balance
	def deposit(self,amount):
		self.__balance+=amount
	def withdraw(self, amount):
		self.__balance-=amount
	def display_info(self):
		print ("Account No." , self.__id , " has ", self.__balance , " dollars. ")


class Saving(Account):
	def __init__(self, pid, balance, interest):
		super().__init__(pid,balance)
		self.__interest=interest
	def calc_interest(self):
		return self.__balance*self.__interest

	def calc_total(self):
		self.__balance+=self.calc_interest()
		return self.__balance

	def display_info(self):
		super().display_info()
		print("This is a saving account. The interest rate is ",self.__interest)

class Current(Account):
	def __init__(self,pid,balance,cap):
		super().__init__(pid,balance)
		self.__cap=cap

	def display_info(self):
		super().display_info()
		print("This is a current account. The overdraft cap is ", self.__cap)

savings=Saving(0,100,0.03)
current=Current(1,100,120)
savings.display_info()
current.display_info()