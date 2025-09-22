list_name = []
list_family = []
list_car_name = []
list_car_color = []
list_car_since = []


while True:
    print("1)Enter your name:\n"
          "2)Enter your family:\n"
          "3)Enter your car name:\n"
          "4)Enter your car color:\n"
          "5)Enter your car since:\n"
          "6)show list:\n"
          "7)exit:\n")

    options = int(input("select your number from box:"))
    if options == 1:
        name = input("Enter your name: ")
        list_name.append(name)

    elif options == 2:
        family = input("Enter your family: ")
        list_family.append(family)

    elif options == 3:
        car_name = input("Enter your car name: ")
        list_car_name.append(car_name)

    elif options == 4:
        car_color = input("Enter your car color: ")
        list_car_color.append(car_color)

    elif options == 5:
        car_since = input("Enter your car since: ")
        list_car_since.append(car_since)

    elif options == 6:
        if list_name:
            print("=" * 50)
            print("list of name is :",list_name)
        else:
            print("=" * 50)
            print("the list of name is empty!!!")

        if list_family:
            print("=" * 50)
            print("list of family is :",list_family)
        else:
            print("=" * 50)
            print("the list of family is empty!!!")

        if list_car_name:
            print("=" * 50)
            print("list of car name is :",list_car_name)
        else:
            print("=" * 50)
            print("the list of car name is empty!!!")

        if list_car_color:
            print("=" * 50)
            print("list of car color is :",list_car_color)
        else:
            print("=" * 50)
            print("the list of car color is empty!!!")

        if list_car_since:
            print("=" * 50)
            print("list of car since is :", list_car_since)
        else:
            print("=" * 50)
            print("the list of car since is empty!!!")



    if options == 7:
        print("good buy!!!")
        break


    ask1 = input("do you want to continue?(yes,no):")
    if ask1 == "no":
        break
    elif ask1 == "yes":
        continue