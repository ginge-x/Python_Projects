def main():
    menu()

def menu():  #Shows a set of menu options giving access to the rest of the system
    feature = 1
    screwlist = read_file()
    while feature != 0:
        print("Welcome to Simply Screws")
        print("This system has 6 features.")
        print("Feature 1 - Show a summary report of the stock, including the total number of units and the total value.")               #showing what each feature does
        print("Feature 2 - Show a report which displays the total number of units in stock in each length category.")
        print("Feature 3 - Show a summary report of the stock of a length specified by the user.")
        print("Feature 4 - Pick a particular screw type and choose whether to increase or decrease the stock of the particular screw.")
        print("Feature 5. - Show a discount added to the current screw which has the largest stock level")
        print("Feature 6 - Display a bar chart showing the stock levels of each length.")
        print("Input '1', '2', '3', '4', '5', '6', or '0' to exit")
        feature = int(input("Which feature would you like to use? "))       #asking the user what feature they would like to use

        if feature == 1:                                                    #if the input is equal to 1 then run feature 1
            feature_1(screwlist)
        elif feature == 2:                                                  #if the input is equal to 2 then run feature 2
            feature_2(screwlist)
        elif feature == 3:                                                  #if the input is equal to 3 then run feature 3
            feature_3(screwlist)
        elif feature == 4:                                                  #if the input is equal to 4 then run feature 4
            feature_4(screwlist)
        elif feature == 5:                                                  #if the input is equal to 5 then run feature 5
            feature_5(screwlist)
        elif feature == 6:                                                  #if the input is equal to 6 then run feature 6
            feature_6(screwlist)
        else:                                                               #if the input is not equal to a valid feature the system will exit
            print("You have now successfully exited the system.")


def read_file():
    try:
        screwlist = []  #creating a masterlist
        with open("screw.txt") as f:   #opening the screw text file
            for line in f:
                if not line.startswith('#'): #removing any comment lines
                    line = line.rstrip().split(',') #splitting the text file by the comma
                    screwlist.append(line)
        f.close()
        return screwlist
    except NameError:
        print("This text file does not exist.")
    except:
        print("Something went wrong.")              #try except look for exception handling


def feature_1(screwlist):
    try:
        screwlist  #masterlist being added to the function
        print("Screw Type Details") #basic heading
        print("------------------") #and splitter for printing
        price = 0     #creating variables for the price
        unitstock = 0 #and units in stock
        for each_screw in screwlist: #start of the for loop
                fiftyS = int(each_screw[3])             #reading in the 50 box of screws which equals one unit
                hundredS = int(each_screw[4]) * 2       #reading in the 100 box and converting it to the apppropriate untis
                twohundredS = int(each_screw[5]) * 4    #doing the same with the 200 box
                stock = fiftyS + hundredS + twohundredS #finding the total stock
                unitstock += stock
                fifty = fiftyS
                hundred = hundredS * 0.9
                twohundred = twohundredS * 0.85             #calculating the total price
                totalprice = fifty + hundred + twohundred   #with the correct discounts applied
                totalvalue = float(each_screw[6]) * totalprice
                price += totalvalue
                price = price
                print("Material:", each_screw[0])           #prints each line of the text file
                print("Head Type:", each_screw[1])          #displaying the apporpriate
                print("Length in MM:", each_screw[2])       #information
                print("Stock(Box of 50):", each_screw[3])
                print("Stock(Box of 100):", each_screw[4])
                print("Stock(Box of 200):", each_screw[5])
                print("Cost Per Box of 50:", each_screw[6])
                print("Discount:", each_screw[7])
                print("----------------------------------")
        print("The total units in stock is:", unitstock,"units.")           #printing the total stock
        print("The total value of the stock is:","£",format(price, '.2f'))#and value of stock
    except:
        print("Something went wrong")   #try except look for exception handling

def feature_2(screwlist):
    try:
        screwlist           #bringing in the list
        twentyscrew = 0     #creating variables
        fourtyscrew = 0     #for each type of screw
        sixtyscrew = 0


        for each_screw in screwlist:
            if each_screw[2] == "20":
                twentyscrew+= int(each_screw[3]) + (int(each_screw[4])*2) + (int(each_screw[5])*4)
            elif each_screw[2] == '40':
                fourtyscrew+= int(each_screw[3]) + (int(each_screw[4])*2) + (int(each_screw[5])*4)
            elif each_screw[2] == '60':
                sixtyscrew+= int(each_screw[3]) + (int(each_screw[4])*2) + (int(each_screw[5])*4)
        print("The total units for screw lengths of 20MM is",twentyscrew,"units.")  #printing the total
        print("The total units for screw lengths of 40MM is",fourtyscrew,"units.")  #stock for each length
        print("The total units for screw lengths of 60MM is",sixtyscrew,"units.")   #category of screw
    except:
        print("Something went wrong!") #try except loop for exception handling

def feature_3(screwlist):
    try:
        screwlist
        screwLength = input("Enter a screw length to see the details of that category, either '20', '40' or '60': ") #asking the user for the length they want
        for each_screw in screwlist:
            if each_screw[2] ==screwLength:                                                                          #if the userinput equals a length in the text file
                print("----------------------------------")                                                          #then shpw the details of all screws of that length
                print("Material:", each_screw[0])
                print("Head Type:", each_screw[1])
                print("Length in MM:", each_screw[2])
                print("Stock(Box of 50):", each_screw[3])
                print("Stock(Box of 100):", each_screw[4])
                print("Stock(Box of 200):", each_screw[5])
                print("Cost Per Box of 50:", each_screw[6])
                print("Discount:", each_screw[7])
        if each_screw[2] != screwLength:                                                                       #if the userinput doesn't equal a length
            print("This length does not exist")                                                         #print an error message as the length doesn't exist
    except:
        print("This length is not in the text file try again.")                                                 #try execpt for error handling

def feature_4(screwlist):
    try:
        screwlist
        materialtype = input("Please specify a material type either 'brass' or 'steel': ")
        headtype = input("Please specify a headtype either 'slot', 'pozidriv' or 'star': ")
        screwlength = input("Please specify a screwlength either '20', '40' or '60': ")
        for each_screw in screwlist:
            if each_screw[0] == materialtype and each_screw[1] == headtype and each_screw[2] == screwlength:
                print("M",each_screw[0], "HT", each_screw[1], "L", each_screw[2], "FB", each_screw[3], "HB", each_screw[4], "TB", each_screw[5])
                increase_decrease = input("Would you like to increase or decrease the stock of this screw: ")
                if increase_decrease == 'increase':
                    box = int(input("What size of box would you like to increase: "))
                    if box == 50:
                        increase = int(input("How many units would you like to increase the screw stock by: "))
                        fiftyB = int(each_screw[3])
                        increase_stock = fiftyB + increase
                        each_screw[3] = increase_stock
                        print("New stock is:",each_screw[3])
                    elif box == 100:
                        increase = int(input("How many units would you like to increase the screw stock by: "))
                        hundredB = int(each_screw[4])
                        updatestock = hundredB + increase
                        each_screw[4] = updatestock
                        print("New stock is:",each_screw[4])
                    elif box == 200:
                        increase = int(input("How many units would you like to increase the screw stock by: "))
                        twohundredB = int(each_screw[5])
                        updatestock = twohundredB + increase
                        each_screw[5] = updatestock
                        print("New stock is:",each_screw[5])
                elif increase_decrease == 'decrease':
                    fifty_Box = int(each_screw[3])
                    hundred_Box = int(each_screw[4])
                    twohundred_Box = int(each_screw[5])
                    box = int(input("What size of box would you like to decrease? "))
                    if box == 50:
                        sell = int(input("How many units would you like to sell? "))
                        stock_on_sale = fifty_Box - sell
                        print(stock_on_sale)
                        each_screw[3] = stock_on_sale
                        if stock_on_sale < 0:
                            partsale = input("Your value you wish to reduce the stock by is currently more than the units in stock and cannot fully be on sale, would you like to continue: ")
                            if partsale == "no":
                                print("Order Cancelled")
                            elif partsale == "yes":
                                value_of_sale = float(each_screw[6]) * fifty_Box
                                value_of_sale = str(value_of_sale)
                                print("The final order cost: £"+value_of_sale)
                        elif stock_on_sale > 0:
                            Amount_of_sale = fifty_Box - stock_on_sale
                            Value_of_sale = float(each_screw[6]) * Amount_of_sale
                            Value_of_sale = str(Value_of_sale)
                            stock_on_sale = str(stock_on_sale)
                            print("The final order cost: £" + Value_of_sale)
                            print("Units in stock now equals " + stock_on_sale)
                    elif box == 100:
                        sell = int(input("How many units would you like to sell? "))
                        stock_on_sale = hundred_Box - sell
                        print(stock_on_sale)
                        each_screw[5] = stock_on_sale
                        if stock_on_sale < 0:
                            partsale = input("Your value you wish to reduce the stock by is currently more than the units in stock and cannot fully be on sale, would you like to continue: ")
                            if partsale == "no":
                                print("Order Cancelled")
                            elif partsale == "yes":
                                value_of_sale = float(each_screw[6]) * hundred_Box
                                value_of_sale = str(value_of_sale)
                                print("The final order cost: £"+value_of_sale)
                        elif stock_on_sale > 0:
                            Amount_of_sale = fifty_Box - stock_on_sale
                            Value_of_sale = float(each_screw[6]) * Amount_of_sale * 0.9
                            Value_of_sale = str(Value_of_sale)
                            stock_on_sale = str(stock_on_sale)
                            print("The final order cost: £" + Value_of_sale)
                            print("Units in stock now equals " + stock_on_sale)
                    elif box == 200:
                        sell = int(input("How many units would you like to sell? "))
                        stock_on_sale = twohundred_Box - sell
                        print(stock_on_sale)
                        each_screw[5] = stock_on_sale
                        if stock_on_sale < 0:
                            partsale = input("Your value you wish to reduce the stock by is currently more than the units in stock and cannot fully be on sale, would you like to continue: ")
                            if partsale == "no":
                                print("Order Cancelled")
                            elif partsale == "yes":
                                value_of_sale = float(each_screw[6]) * twohundred_Box
                                value_of_sale = str(value_of_sale)
                                print("The final order cost: £"+value_of_sale)
                        elif stock_on_sale > 0:
                            Amount_of_sale = fifty_Box - stock_on_sale
                            Value_of_sale = float(each_screw[6]) * Amount_of_sale * 0.85
                            Value_of_sale = str(Value_of_sale)
                            stock_on_sale = str(stock_on_sale)
                            print("The final order cost: £" + Value_of_sale)
                            print("Units in stock now equals " + stock_on_sale)
        return screwlist
    except:
        print("Something went wrong")



def feature_5(screwlist):
    try:
        screwlist
        unitstock = 0
        price = 0
        screw_on_sale = input("Would you like to put the current largest stock of screw on sale: ")
        if screw_on_sale == 'no':
            print("Discount not applied to this specific screw.")
        elif screw_on_sale == 'yes':
            print("You can now move on to see the discount on the screw.")

            for each_screw in screwlist:
                if each_screw[7] == 'yes':
                    fiftyS = int(each_screw[3])  # reading in the 50 box of screws which equals one unit
                    hundredS = int(each_screw[4]) * 2  # reading in the 100 box and converting it to the apppropriate untis
                    twohundredS = int(each_screw[5]) * 4  # doing the same with the 200 box
                    stock = fiftyS + hundredS + twohundredS  # finding the total stock
                    unitstock += stock
                    fifty = fiftyS
                    hundred = hundredS * 0.9
                    twohundred = twohundredS * 0.85  # calculating the total price
                    totalprice = fifty + hundred + twohundred  # with the correct discounts applied
                    totalvalue = float(each_screw[6]) * totalprice
                    discount = totalvalue * 0.9     #calculating the total price with the extra 10% discount applied
                    price += discount
                    price = price
                    print("This is the current screw on sale as it has the largest stock currently.")       #Shows the details
                    print("----------------------------------")                                             #of the stock which
                    print("Material:", each_screw[0])                                                       #currently has a discount applied
                    print("Head Type:", each_screw[1])
                    print("Length in MM:", each_screw[2])
                    print("Stock(Box of 50):", each_screw[3])
                    print("Stock(Box of 100):", each_screw[4])
                    print("Stock(Box of 200):", each_screw[5])
                    print("Cost Per Box of 50:", each_screw[6])
                    print("----------------------------------")
            print("------------------------------------------------------------------------------------")
            print("The total cost of this stock with the sale discount applied is", format(price, '.2f'))   #printing the new price with the extra sale
            print("------------------------------------------------------------------------------------")   #discount applied
    except:
        print("An error has occurred")  #try execpt loop for exception handling



def feature_6(screwlist):
    try:
        screwlist
        import matplotlib.pyplot as plt         #importing matplotlib
        import numpy as np
        twentyscrew = 0
        fourtyscrew = 0                         #creating variables
        sixtyscrew = 0

        for each_screw in screwlist:
            if each_screw[2] == '20':
                fifty_Box = int(each_screw[3])
                hundred_Box = int(each_screw[4]) * 2
                twoHundred_Box = int(each_screw[5]) * 4
                total = (fifty_Box+hundred_Box+twoHundred_Box)      #calculating the stock of each screwlength
                twentyscrew += total                                #category
            elif each_screw[2] == '40':
                fifty_Box = int(each_screw[3])
                hundred_Box = int(each_screw[4]) * 2
                twoHundred_Box = int(each_screw[5]) * 4
                total = (fifty_Box + hundred_Box + twoHundred_Box)
                fourtyscrew += total
            elif each_screw[2] == '60':
                fifty_Box = int(each_screw[3])
                hundred_Box = int(each_screw[4]) * 2
                twoHundred_Box = int(each_screw[5]) * 4
                total = (fifty_Box + hundred_Box + twoHundred_Box)
                sixtyscrew += total

        labels =['20MM', '40MM', '60MM']                          #creating the labels for the graph
        bar = [twentyscrew, fourtyscrew, sixtyscrew]
        left_edges=[0,10,20]
        plt.bar(left_edges, bar,9, color=('r','b','g'))           #creating the graph with the colors on each bar

        plt.title('Current stock of different screw lengths')     #setting the title

        plt.xlabel('Length in MM')
        plt.ylabel('Current Stock Units, 1 unit = box of 50')     #labelling the x and y axis
        plt.xticks([0,10,20], labels)

        plt.show()                          #displaying the graph
    except:
        print("An error occurred")                                #try except for error handling


main()