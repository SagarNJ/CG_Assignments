n = 5623
a = 0
while n != 0:
    temp = n % 10
    a = (a * 10) + temp
    n = n // 10
print(a)
#print('reversed number:' +str(a))


#n = 5623
#r = 0

#while n != 0:
#    digit = n % 10
#    r = r * 10 + digit
#    n //= 10

#print("Reversed Number: " + str(r))