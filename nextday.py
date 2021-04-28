def nextday():
    print("Enter the day\n")
    str=input()
    if str=='Monday':
        print("Tuesday")
    elif str=='Tuesday':
        print("Wednesday")
    elif str=='Wednesday':
        print("Thrusday")
    elif str=='Thrusday':
        print("Friday")
    elif str=='Friday':
        print("Saturday")
    elif str=='Saturday':
        print("Sunday")
    else:
        print("Monday")