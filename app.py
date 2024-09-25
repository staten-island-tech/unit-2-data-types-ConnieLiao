""" """ """ """ """ x = 3
y = float(3)
print (x,y)
values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
print (values[0])
print(values[6])
x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)
Day_of_the_week = input("What day is today? ")
if Day_of_the_week == "Friday":
    print ("corect")
else:
    print ("incorrect")
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')
#challeng 1
if 887 % 2 == 0:
    print("the number is even") 
else:
    print("the number is odd") 
#challenge 2 """ """ """
service = input("how was service? ")
bill=("$18.90")
if service == 'bad':
     print("the service is BAD,YOU PAY $18.90 and tip 0%")
elif service == 'okay':
     print("the service is OKAY,YOU PAY $18.90 and tip 15%")
     print("$"(18.90 * 0.15)+18.90)
elif service == 'good':
     print("the service is GOOD,YOU PAY $18.90 and tip 20%")
     print((18.90 * 0.20)+18.90)
else:
     print("the serivce is WONDERFUl,YOU PAY $18.90 and tip 25%")
     print((18.90 * 0.25)+18.90) 