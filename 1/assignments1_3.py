#name = ('Shaun', 'Ron', 'Michael')
#seat_numbers = (101, 102, 103)
#s = list.set_numbers()
#dict = dict.fromkeys(name, seat_numbers)
#print(dict)


name = ('Shaun', 'Ron', 'Michael')
seat_numbers = (101, 102, 103)
dict = {}
for i in range(len(seat_numbers)):
    dict[name[i]] = seat_numbers[i]
print(dict)