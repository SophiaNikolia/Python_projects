print("Exercise 9\n")
n=int(input("Give me a number : ")) #asking the user to give once an int number
s = 0#commencing with sumup being 0
p = bool(1) #having a variable p that is true
while p: #the loops stops when p becomes false
    if n==0: #if the number is 0 the sumup will always be 1
        s = 1
        break
    n=abs(n*3) + 1
    print("\nThe number is",n)
    while n!=0: #printing the digits of the number
        print (n%10)
        s+=(n%10)
        n=(n//10)
    if (s>=10): #if the sumup is not a single-digit number then the number becomes the sumup and the whole procedure is repeated
        print ("\nThe sumup is", s)
        n = s
        s = 0 #sumup becomes 0 again
    else:
        p = bool(0) #if the sumup is a single-digit number then p becomes false
print("\nThe final sumup is",s)
