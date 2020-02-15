dict={}
while True:
    print("$$$$$$$$ BIRTHDAY APP $$$$$$$$")
    print("1.Show Birthday")
    print("2.Add To Birthday List")
    print("3.Exit")
    Choice=int(input("Enter The Choice"))
    if Choice == 1:
        if len(dict.keys())== 0:
            print("Nothing To Show")
        else:
            name = input("Enter name to look for birthday")
            birthday=dict.get(name,"No Data Found")
            print(birthday)
    elif Choice == 2:
        name=input("Enter friend's Name")
        date=input("Enter Birthdate")
        dict[name]=date
        print("Birthday Added")
    elif Choice == 3:
        break
    else:
        print("Choose a valid option")
