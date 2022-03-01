Number = [10,20,30,40]

def printList():
    try:
        Output = Number[5]
    except IndexError:
        print("Invalid index, try again.")

printList()