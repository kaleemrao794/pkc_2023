# while loop

age = 17
while age < 18:
    print("You are not eligible to vote")
    age = age + 1
    
# for loop
for i in range(10):
    print(i)

kids = ['Areesha', 'Fareha', 'Abdul_Rehman']
for kid in kids:
    print(kid)

kids = ['Areesha', 'Fareha', 'Abdul_Rehman']
for kid in kids:
    if kid == 'Fareha': break
    print(kid)

kids = ['Areesha', 'Fareha', 'Abdul_Rehman']
for kid in kids:
    if kid == 'Fareha': continue
    print(kid)

kids = ['Areesha', 'Fareha', 'Abdul_Rehman']
for kid in kids:
    if kid == 'Fareha':
        print("Fareha is good girl")   

    # print(kid)
