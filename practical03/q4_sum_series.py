#Filename:q4_sum_series.py
#Author:PS
#Created:20130221
#Description:compute the sum of a series

def m_series(i):
	if(i==1):
		print("i\tm(i)")
		sum=float(1)/2
	else:
		sum=float(i)/(i+1)+float(m_series(i-1))
	print("{0}\t{1:.4f}".format(i,sum))
	return sum

m_series(20)