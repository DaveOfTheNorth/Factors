from time import sleep

while True:
    i=int(input("Enter your number    "))
    x = int(i-1)
    print()
    list = []

    while x > 0:
        if i%x == 0:
            list.append(x)
        x -= 1

    print(list)
    print()
    
    again = input("Do you want to try another number y/n?    ")
    if again == "y":
        print()
        print()
        continue
    if again != "y":
        print()
        print("Have a good day")
        sleep(2)
        break
    
    