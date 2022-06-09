import os
import sys

# Password for admins section
psw = 12345


products = [
    {
        'id': 1,
        'produkti': 'Vipa Qips',
        'cmimi': 50
    },
    {
        'id': 2,
        'produkti': 'Sola Ice Tea',
        'cmimi': 1
    },
]
new_products = {

}

user = None
item = ''
item2 = ''



# Function for Products
def Products():
    pass

def main():
    global user_input
    global new_produkt
    global new_cmimi
    print('\n1. Shiko Produktet ')
    print('2. Blej Produktin ')
    print('3. Shto Produkt ')
    print('4. Hiq Produkt ')
    print('5. Ndalo Porgramin')

    user_input = int(input('\nShkruani zgjidhjen tuaj : '))

# Fucntion 1
    if user_input  == 1:
        for i in products:
            print(i['id'], i['produkti'], i['cmimi'])
        if not new_products:
            pass
        else:
            print(*new_products.values())
        main()
        

# Function 2
    if user_input == 2:
        global payment
        global item
        global new_item_price
        global new_item
        usr_input_choice = int(input('Shkruani ID e produktit qe deshironi ta bleni : '))
        
        for i in products:
            if usr_input_choice == i['id']:
                item = i
                if item == '':
                    print('Ju lutem shkruani nje ID valide')
                    main()
                else:
                    payment = int(input('Ju lutemi pagesen : '))
                    if payment == item['cmimi']:
                        print(f"Ju keni blere {item['produkti']}, {item['cmimi']}")
                        main()
                    else:
                        print('Ju nuk keni para te mjaftueshme te bleni kete produkt.')
                        main()
            elif usr_input_choice == 3:
                item = i
                if item == '':
                    print('Ju lutem shkruani nje ID valide')
                    main()
                else:
                    if not new_products:
                        print('Ju lutem shkruani nje ID valide')
                        main()
                    else:
                        payment = int(input('Ju lutemi pagesen : '))
                        if payment == new_item_price:
                            print(f"Ju keni blere {new_item}, {new_item_price}")
                            main()
                        else:
                            print('Ju nuk keni para te mjaftueshme te bleni kete produkt.')
                            main()

    if user_input  == 3:
        user_psw = int(input('Shkruani Fjalekalimin per ta qasur kete opsion : '))
        if user_psw == psw:
            new_products['id'] = 3
            new_item = input('Shkruani emrin e produktit : ')
            new_products['new_produkt'] = new_item
            new_item_price = int(input('Shkruani Cmimin e produktit : '))
            new_products['new_cmimi'] = new_item_price
            print(f'Ju keni shtuar {new_products.values()}')
            main()

        else:
            print('Fjalekalimi eshte i gabuar !')
            main()

    if user_input == 4:
        user_psw = int(input('Shkruani Fjalekalimin per ta qasur kete opsion : '))
        if user_psw == psw:
            del_produkut = int(input('Shkruani ID e produktit qe deshironi ta hiqni : '))
            if del_produkut == 1:
                del products[0]
            if del_produkut == 2:
                del products[1]
            if del_produkut == 3:
                del new_products[0]
            main()
        else:
            print('Fjalekalimi eshte i gabuar ! ')
            main()
        

    
#Function 5
    if user_input == 5:
        quit()
    
                
                




    

# def buy():
#     global user_input
#     print('2. Blej Produktin')
#     user_input = int(input('Shkruani zgjidhjen tuaj : '))

main()





