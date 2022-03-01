while True:
    try:
        Num = input("Enter a Number: ")
        if Num.isdigit() == False:
            raise ValueError
        else:
            Num = int(Num)
            print(Num**2)
            break
    except ValueError:
        print("Enter a valid input.")
