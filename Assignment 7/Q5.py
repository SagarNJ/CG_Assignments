List1 = [10,20,30,40]
List2 = [1,2,3]

def add(lst1,lst2):
    try:
        output = []
        for i in range(4):
            output.append(List1[i] + List2[i])
    except IndexError:
        print("Invalid index, try again.")
    except TypeError:
        print("Invalid type, try again.")

add(List1,List2)
