#Filename:q5_compute_series.py
#Author:PS
#Created:20130221
#Description:compute the sum of a series

def m_series1(i):
	if(i==0):
		print("i\tm(i)")
		sum=4
	elif(i%2==0):
		sum=m_series1(i-1)+4*float(1)/(2*i+1)
	else:
		sum=m_series1(i-1)-4*1.0/(2*i+1)
	if(i%2==1):
		print("{0}\t{1:.11f}".format(i,sum))
	return sum

m_series1(17)