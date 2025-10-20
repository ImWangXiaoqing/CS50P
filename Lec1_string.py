#my very first py code

#printing, input, passing, variable, comments, Syntax and Quotes, (sep'', end='/n', *Objects = named parameters),

name = input("What's your name? ").strip().title()
surname = input("What's your surname? ")

name = name.strip() #remove whitespaces from str
name = name.capitalize() #capitalise the str, but only first word
name = name.title()

first, second = name.split(" ")# can split and save into different vars

# can also write as print("Hello,", name)
#concatination is joining or connecting 2 args, texts, num or text etc.
print("Hello, " + name, surname) # we can call variable by comma seperated vars
print(f"Hello, {first}") #writing f makes python knows there is variable calling in the statement


##########################################################################################################################
#### defining and making your fn

def main():
    name = input("What's your name? ").strip().title()
    hello(name)


def hello(to):## if we write it as def hello(to="world"), it will still output print(f(hello, {name})) #we can also write it as def hello(to="Nitish"), in case I'm not taking anything from outside
    print("Hello,", to)

main() #without calling main function the code will print nothing, so, we have to call it by main so that main can call hello!

####what is an scope? scope is the defining and calling of a var defined in the same function where it is being
# called or using where it is being called.....................