##   int   ##
"""
x = input("Num 1: ")
y = input("Num 2: ")

print(x+y)#this just concatinates the ints, output of x,y as 1,1 will result 11;

#for addition we need to tell that they are int not str

x = int(input("Num 1: "))
y = int(input("Num 2: "))

# z = int(x) + int(y)
print(x+y) # output of x,y as 1, will result 2;

# Q. if you have to write commas at places, what you will need to do? like, for 999+1 = 1000, but what if you have to write as 1,000?
print(f"{z:,}")

"""


#####################################################################################################################################################################
##    float   ##

x = float(input("Num 1: "))
y = float(input("Num 2: "))

z = (x+y) # Can also write as z = round(x+y)
print(round(z, 3)) #format round(num, no of digits after deci)

z = x/y # z = (x/y, 2)
print(f"{z:.2f}") #format f"{(num: .no_f)}"


####### return? how?

def main():
    x = int(input("Enter a number: "))
    print("x squared is: ", square(x))

def square(n):
    return n*n, n**3, pow(n, 4)

main()