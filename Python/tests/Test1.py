def main():
    number_of_values = int(input("Enter number of how many values do you want to add to this list : "))
    list_item = []
    for i in range(number_of_values):
        value = input("Enter a value: " )
        list_item.append(value)
    for x in range(len(list_item)):
        print(list_item[x])
if __name__== "__main__": 
    main()