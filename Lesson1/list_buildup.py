basket = (
    'mango papaya orange grapes strawberry '
    'jackfruit apple calamansi banana '
    'coconut peanuts'
).split() #splits the string into a list

selected = []

for i in basket:
    #print(i)
    if len(i) <= 6:
        selected.append(i)

print(f'--> Basket {basket}')
print(f'--> Selected {selected}')
