x = int(input("Write the value of x: "))
match x:
    case 5:
        print("This number is 5")

    case 3:
        print("This number is 3")

    case 2:
        print("This number is 2")

    case _ if x == 90:
        print("Yes this is 90")

    case _ if x == 80:
        print("Yes this is 80")

    case _:
        print("This number is", x)