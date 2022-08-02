
fruits_available = ['cherry', 'banana', 'apple']

total_toadd = int(input("How many fruits would you like to add? "))

if total_toadd == 0:
    print('Okay! You can tell us next time.')
else:
    i = 1
    frut
    while i <= total_toadd:
        new_fruit = input(f"Enter $i-th fruit you would like us to add to the menu: ")
        print(f"{new_fruit} is added to our selection")
        fruits_available.append(new_fruit)
        i += 1
    
print("Our fruits selection includes: ", fruits_available)


