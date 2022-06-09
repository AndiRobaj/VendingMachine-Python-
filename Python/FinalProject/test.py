import os
import sys

# Password for admins section
psw = 12345


products = [
    {
        'id': 1,
        'produkti': 'Bravo',
        'cmimi': 50
    },
    {
        'id': 2,
        'produkti': 'Chio Chips',
        'cmimi': 1
    },
]

item = ''


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


    if user_input  == 1:
        for i in products:
            print(i['id'], i['produkti'], i['cmimi'])
        main()
        


    if user_input == 2:
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
main()