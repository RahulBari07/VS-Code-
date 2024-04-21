# Take P,N and R as input from user
P= float(input('please enter principal in INR :'))
N= float(input ('please enetr periods in years :'))
R= float(input('please enter rate of interest in %p.a. :'))
#calculate copound interest amount
A=P*(1+R/100)**N
I=A-P
# print above results
print(f'amount for compound intrest : {A:.2F} INR')
print (f'total intrest : {I:.2F}')