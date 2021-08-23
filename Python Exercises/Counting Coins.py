def count():
    total = 0
    i=0
    num = 0
    while i != '-11':
        i = input("\n Current Count : " + str(total) + "\nEnter any key to add one... \n[Press E to Undo]\n[Press -11 to Get Out]")
        if i == 'e':
            total -= 1
        elif i == '-11':
            break
        else:
            total +=1
    return total

def choice(total):
    choice = 0
    while choice != 10 and choice != 20 and choice !=5 and choice !=50:
        print("\nEnter is it 5 Cent, 10 cents, 20 Cents 0r 50 Cents\n")
        print("\n [5  Cents = 5 ]")
        print("\n [10 Cents = 10]")
        print("\n [20 Cents = 20]")
        print("\n [50 Cents = 50]")
        choice = int(input("\n Enter : "))
    if choice == 5:
        print(total*0.05)
        total = total*0.05
    elif choice == 10:
        print(total*0.1)
        total = total*0.1
    elif choice == 20 :
        print(total*0.2)
        total = total*0.2
    elif choice == 50 :
        print(total*0.5)
        total = total*0.5
    return total



print("=== Count Your Coins ===\n")
total = count()
total = choice(total)

f = open("countcoins.txt", "a")
f.write("\n RM"+ str(total))
f.close
