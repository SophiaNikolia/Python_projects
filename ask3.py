print("Exersice 3\n")
x={"juice":2,"bread":3,"cheese":4,"chips":5} #the dict with the items and their price
print ("The items that you can purchase and their price are the following: \n" ,x,"\n")
foros = 24/100
# creating an empty list for the user
lst1 = [ ]
#the lenght of the list
n = int(input("Enter the number of items you would like to buy from the list above: \n"))
for i in range (0,n):
    #filling the list
    ele1 = [input("According to the list above enter the name of the item you would like to purchase: \n")]
    lst1.append(ele1)
#creating a second list with the price of the item(s) that the user has already select to buy
input_string = input("According to the list on top enter the price(s) of the item(s) you chose for purchase separated by space: \n")
userlist = input_string.split()

def lista(userlist,foros): #creating a function that calculates the sum of element of input list and the total amount of the purchase including the tax
    sum = 0
    for num in userlist:
        sum += int(num)
        f=sum+sum*foros #final amount of payment
    return f

result = lista(userlist,foros)
print("The item(s) that you chose for purchase are/is", lst1 , "and the total amount of your purchase is", result ,"$\n")
