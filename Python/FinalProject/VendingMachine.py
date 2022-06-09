items = [
    {
        'code':0,
        'name':'coca cola',
        'price':5
    },
    {
        'code':1,
        'name':'cadbury',
        'price':10
    },
    {
        'code':2,
        'name':'chips',
        'price':2
    },
]

is_quit = False
item = ''

while is_quit == False:
    print("Welcome to the vending machine")
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")

    query = int(input("Enter the code number of the item you want to get: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Great, {item['name']} will cost you {item['price']} dollars")

        price = int(input(f"Enter {item['price']} dollars to purchase: "))
        if price == item['price']:
            print(f"Thank you for buying here is your {item['name']}")
        else:
            print(f"Please enter only {item['price']} dollars")

    query = input("To quit the machine enter q and to continue buying enter anything: ")
    if query == 'c':
        is_quit = False
    else:
        is_quit = True
    print('')





















    # ....................
#     def buy():
#     global user_input
#     print('2. Blej Produktin')
#     user_input = int(input('Shkruani zgjidhjen tuaj : '))

# main()

# if user_input  == 1:
#     for i in products:
#         print(i['id'], i['produkti'], i['cmimi'])
#     main()
    
# if user_input == 2:
#     user_choice = int(input('Shkruani ID e produktit qe deshironi ta bleni : '))
    
#     for i in products:
#         if user_choice == i['id']:
#             item = i
#     if item == '':
#         print('Ju lutem shkruani nje ID valide')
#         main()
#     else:
#         payment = int(input('Ju lutemi pagesen : '))
#         if payment == item['cmimi']:
#            print(f"Ju keni blere {item['produkti']}, {item['cmimi']}")
#         else:
#             print('Ju nuk keni para te mjaftueshme te bleni kete produkt.')
#             main()

        
    


# if user_input  == 3:
#     user_psw = int(input('Shkruani Fjalekalimin per ta qasur kete opsion : '))
#     if user_psw == psw:
#         print('you have entered the admin seciton now you can add new products!')
#         new_prd = input('Shkruaje produktin te cilin deshiron ta shtosh ne list : ')
#         new_products['3'] = new_prd
#         print(new_products)

#     else:
#         print('Fjalekalimi eshte i gabuar !')
#         main()