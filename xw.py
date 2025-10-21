# so, if I want to write something that is not part of code, you write it like this....by putting # in front of sentence, ok?
#understood? you also write like that...
#yes
#okay, good
# so, here I write a simple statement

#print("Hello Xiaoqing!")
#can you see the output?, okay
#yes
# we can also write numbers as
# print(10000+10000)
#see, it adds it....we can also write it like this,
# A = 10
# B = 20
# print(A+B)
# it is also adding it, means it can read from references, ok?
#yes
# , good.....!your task is, divide 10000 by 10, by using references, do it...
# a=10000
# b=10
# print(10000/10)
#like this?yes, like this...so, you understand, you can write numbers directly, for words, you need to use these, "", and you write words in side these
#understood? for example, print("Hello Xiaoqing!")yes, good...
# now, lets write it little differently
# name = "Xiaoqing"
# age = 18
# print("Hello, ", name)
# print("You are ", age, "years old!")

#---------------------------------------------------------------------------------------------#

#can you find any problem in this code?okay, fix the problem, good girl..., now run the code
# you are running different file...choose correct file and then run it , no no, the file you are running is Lec1, so, change it
#wait let me explain  ok, I sent you a photo, see it, choose current file , understand it? did you find option? yes , okay, run it working
#okay, good....so, you understand how it is working?yeah, good....there is another way to run the python file....
#can you see the terminal windows?can you?  where, okay.....so, here, you can also run this file, how? see in terminal
#see?yeah, good, so when you write python and write file name, which you want to run, it runs that file...understood  ok, good...
#hi, hi miss, welcome to nitish's classes!!!  hhh, so today we will try to learn in a structured way....
#today, you will learn names, and some terms.....! ok,got it
# so, computers work on diff data types, means, different types of data, computers mostly work on binary, like 0 and 1
#but we also have text, photos, all need to be interpreted by computer. so, before using them, we need to tell computer what type of data
#data it is and how to process it. but python gives us flexibiility to forget these things, instead, we collectively call them as variables.
#you can define variable as giving it a name, and its value, so
# name = "Xiaoqing"
# anothername = "nitish"


#-----------------------------------------------------------------------------------------------#

#so, here name & anothername, both are variables, also, if name = 10, is also valid, so, we can see, we can assign anything to it....
#understood? what variables are? anything emm...like a box can , umm, yes, you are getting it right, its like a bog, we can put anything in it.... got it, good.
# since we are giving a value to variable, we can chnage it later....for example....
#run file using terminal window  how to use, emm, you remember, you used it, open a window in bottom and write python followed by file name
#do you remember?where is the file name, um press, Alt+F12....did it open?click option + F12..  emmm...no.....umm, then open it manually, let me show....you, check QQ
#what, umm, the command you need to write is python and file name, as python xw.py, understood? any question?then , just press enter to run...emm...why i cant use the green ...i want to speak chinese, speak or type?.........yes, you can also use green button to run, I just wanted ypu to remember the command as well, because you will not get the button always
#i mean can i use the green 标志，在右上方那个像三角形的图标, yes you can use it, I just wanted you to learn, you might not get it always....for example, let me show you something...
#coming, good run the code using the button or terminal......good, as you can see, first we assigned x = 100, and later x = 50, so, we can do reassigning in python...ok...whenever there is a need we do it
#got it maybe, umm, ask questions whenever you want to...
#now, I think you know maths well, like basic maths, Addition symbol, multiply, division, percentage etc...right?emm..., I mean, you know all symbols, +, -, *, /, **, right?forget **, this is for exponent, means power

# x = 3**2 #ans = 9, means 3*3, okay?got it
# y = 2**10 #ans = 1024, okay?ok good
# so miss Xiaoqing, you have a task, you need to tell me how many seconds are there in a year, calculate using python....use diff variables and assign year, months, days, hours and multiple by seconds, okay...
#emm... okay, don't get confused, just tell me, how would you do it generally...in maths
# x = 100
# print(x)
# x = 50
# print(x)
# x=365
# y=24
# a=3600
#print(x*y*a)#seconnds in a year, umm, okay, by syntax, its correct, but not by logic....first of all, when you are writing code, always use meaningful variable names. second, dom't do calculation yourself....

# no_of_years = 1
# no_of_days = 365
# no_of_hours_in_a_day = 24
# no_of_mins_in_hour = 60
# no_of_seconds_in_minute = 60
#
# total_seconds = no_of_years*no_of_days*no_of_hours_in_a_day*no_of_mins_in_hour*no_of_seconds_in_minute
# print(total_seconds)
#understand? write meaningful words, because you are writing the code, doesn't mean, you are the only one in future to read it, someone else might read it as well, so he/she should understand it
#got it, see ,it makes more sense....run?yes, run..ok emm... i have a question,what is the meaning of no_of_ must use it ? no no, its not must to use....you can write it however you want
#like, noOfDays, etc...can give any name...okay?just need make other can understand....can you quickly recall what we learned in last class?
#variable emm...hunh? can you explain a bit?explain what?variable, yes, little bit via example.a container that can store various types of items, okay...
# so, now we will understand functions, ok? should we start?yep, okay



#____________________________________FUNCTION______________________________________#
#functions are nothing but a piece of code, that is written to do specific task or give an output by using other things.
#to define a function, we use word, "def" and then write function name, like "def addition", for example:

# def addthree(inputnumber):
#     ans = inputnumber+3
#     return ans

#so, what we are doing is, we are taking a number from outside and we are adding 3 to it, so, out function does this, the good part of function is that, we can use it multiple times, so
#that we don't have to add it everytime. we can call function anywhere in our code. leave it, lets understand practically, here below I'm calling the function.

# result = addthree(500)
# print(result)
#here you can see we have created a variable (result) and storing ans of "addThree" function into it and then printing it....
#def addThree(inputNumber): in this, we have written addThree and then in bracket we are saying to function that you need this number or variable....so, whenever the function will run,
#it will call for that variable into bracket and then use it and give ans. ok? try running the code.....ok503, got the ans? yes, its 503, are you understanding the flow of the code and relevance of the function?
#maybe understand, can you write your own function for division? write it....any function i can ?, umm,yes, you can write any function, for division, subtraction, exponent, anything....

#hey don't write same function name, you can't do that, it prohibited in python or any other language...don't write same function means i need change , yes you need to write some diff function
#change 'inputnumber'? umm, you can use same variable, but can't use other function's name....emm..you need show more , okay....
#lets say I want to write function to say hello to given username, lets say, I want to say hello to you...., umm, lets take simple example...its it bit advanced

# def expo (anynumber):#this line is, here I;m defining function name, and the variable its need from outside
#     ansofnumber = anynumber**anynumber #in this line, I'm doing the calculation and saving it into variable
#     return ansofnumber                 #and here I'm returning the result outside of function scope...
#
# resultofnum = expo(200)              #here, I'm calling function and giving it the value of variable "anynumber" as 200, and saving the result into resulttonum variable
# print(resultofnum)                   #and here I;m prinnting it to see the result

#can you explain what I wrote here? in words..., understood now?yeeep, now can you write your own function with a completely new function name and variable name.let me see, okay, ask if you don't understand anything
#how to use it to say "你好，nitish"same?, umm, yes, but the implementation is little diff, you want to learn it now?yeah  , okay.....
#for that, you need to learn two things, "f" and use of { }.....
#I'm writing a example

# def hello (name):
#     print(f"你好, {name}!") #here, the f allows use to use variables into sentence in the quotes using { }, these curly brackets....
#
# hello("nitish") #this is calling the function and printing what you wanted....can you see the output? on terminal, we have square of 200 by 200, and also hello function output?
#yep, so, you understood the function now?some question .why name need {}, okay, do you remember when I said, that when we write number, we write it directly, and when we write string we use
#"", and since I;m using theese " ", and name is a variable from outside, not directly part of string, so explicitely, we need to tell python about it....ok? so we use this { }
#got it , okay, I want to show another example...lets say, you want to write, "hello, nitish from xiaoqing!", so, we have teo things now...two names

# def greeting(myname, hername):
#     print(f"你好, {myname} from {hername}!")
#
# greeting("nitish", "Xiaoqing") #got it?yep, good, now, write your own function....try to play with it......


def praise(name):
    print(f"你真棒，{name}")

praise("xiaoqing") # CooL, you are awesome Xiaoqing....hhhhh,hhhh, understood?yeah, write one more function while using 4 outside variables, this is your task.let me try,
# sure...!
def register(name,age,sex,nationality):
    print (f"基本信息：{name} {age} {sex} {nationality}")#here?, no...

register("王小青", "18", "女", "中国")#why , you are not using "," between variables, here............!like this?, haha, like this.got it, good....

#you have made 2 mistakes, find & rectify them, now you get some idea, how code is used in services, techonolgies, and what it can do in real life tasks?yep,def and use

#so, by using function you can very complex task, very easily...got it.....nice.....want to learn more?of course.....haha, good, impressing me......hhh  hhh

#______________________________using If and Else statements_____________________________________#wait a min, going to washroom.....!ok, I'm back...if you want to go
# what i see?emoji.....hhh, I wrote it because the line I wrote was deleted......hhhhhhhhh

#so, lets start, so, If and else are conditions, lets say, you are getting married, but you can't get married below the age of 21, so, someone need to check by taking input.....
#so, we write, if Xiaoqing is above 21, let her marry, otherwise, don't

# def cangetmarried(age):
#     if age > 21:
#         return "Yes, you can get married"
#     else:
#         return "You can't get married now"
#
# answ = cangetmarried(18)
# print(answ)

#understand.....?yeah

#another example, lets say, North Korea allows child marriages, but other countries don't, so, lets write for this condtion

def checkeligibility(age, country):
    if country == "North Korea":
        return "Yes, Since you are north korean, you can get married"
    elif age > 21:
        return "Yes, You can get married, you are above 21"
    elif age<21:
        return "You can't get married!"

#eligibilitystatus = checkeligibility(19, "North Korea")ok
eligibilitystatus = checkeligibility(19, "China")
print(eligibilitystatus)
#got it , good......so, you understand, these are very helpful....emm i remmember “if” can use in 循环语句, yes, loops are there too, if and else can be used anywhere depending on needs..
#got it, okay, since you have mentioned loops, lets learn them....but first lets understand, "and" and "or" operations

#_______________________________and or_______________________________________#
#and is used to define, both, means, if some condition is fulfilling two or more conditons, lets say, you will only get married to someone, if you have a business and above age of 25
#and you will get married, if you are either older than 25 or have business irrespctive of age.....

def canigetmarried(age, occupation):
    if age>=25 and occupation=="business": #here, I'm saying, only get married if both condition are fulfilling, otherwise don't, so "and" needs both conditions to be true.
        return "yes, you can get married!"
    else:
        return "you can't get married"
cangetmarriedornot = canigetmarried(25, "business")

print(cangetmarriedornot)

def anotherexample(age, occupation):
    if age>=25 or occupation=="business": #here, I am saying if any of these 2 condtion is true, you are good to get married, so "or" gets used in these type of conditions.....
        return "yes, you can get married!"
    else:
        return "you can't get married"

exampleresult = anotherexample(19, "business")
print(exampleresult) #okay?ok....

#Task: Write a function, that check the eligibility to apply for VISA for different countries
#Task requirement: Only let the user apply if he is applying to India, China, Germany and Switzerland, and also, he/she must be 18 years old....otherwise, return "you can't apply";what wrong, I think connection got lost...
#write now...
#do it...feel free to ask any clarifications
def canapplyvisa(age,country):
    if age>=18 and (country=="India" or country=="China" or country=="Germany" or country=="Switzerland"):    #wrong? yes....why, think for a min, make use of "or" for diff countries, you can't just write directl
        return "yes,you can apply"
    else:
        return"you can't apply"

example=canapplyvisa(18,"India") #oh,no how to copy words use keyboard, in Mac you can use, "Command + C" to copy and "Command+V" to pastei  i do it but appear something wrong,you see, yes, I saw...I don't know what happened, but I will check and tell you later....ok
print(example)
#so, understood all concepts?I'm closing the session for now, going to eat dinner. will teach somethings later, are you ok with it?ok byebye i will miss you,hhhh, hhhhh, thank you!



#write ahead....question == =  diff? Ans: = is used for numbers, and == for strings.....




######################################################################################
#                           Welcome Xiaoqing!                       (10.21.2025)
#topics we will learn today:
#                  1. Loops
#                  2. Lists
######################################################################################

#ready? or want a few mins to review code?ready, okay, nice

#______________________________Loops_________________________#
#i think you know little bit about these? since you mentioned it once...emm...i remmember a little ,"for"loop, s
#okay, we can start.....

#Loops are nothing but simple function, built into python, that provides us do recurring tasks simply using word "for"
#for is named because it works on conditions, like count 5, then stops etc.
#While loop is also there, both can do same tasks, but sometimes one is better, sometimes another one is....

#first, lets start with while loop, its simple to understand

count = 0
while count<10:
    print("Love you!")
    count = count+1
    #count +=1

#can you guess why I wrote this line? count+=1?meybe,if count=5,print love,then loop 5+1=6,still print love you untill >=10, hmm, you get the idea
#if we don't write count +=1, means we are not increasing count, so it will never become 10, and then loop keep running infintly until the laptop crashes or pycharm stops
#count += 1, is same as count = count+1, you can also write it like that..., so loop runs first, count is zero, but +1 is there,so it becomes 1, and runs again and so on, and reaches 10 and stops
#ok?ok, let me show you.....can you see it keeps running?yeah, and now I run again with +1, it printed exactly 10 times....do you want to try it yourself?yeah 10 times, yea, nice..

#lets do something interesting.....can you tell me how many days left for your birthday? are you counting?42, yes, 42....
#lets make a date countdown....

# def birthdaycountdown (days):
#     day = days
#     return day
# totaldays = birthdaycountdown(42)
# daycount = 0
#
# while daycount<totaldays:
#     print(f"{daycount} days passed!")
#     daycount +=1
#
# print("Happy Birthday Xiaoqing! ❤️")

#wow, want to write something? I'm waiting.....meme🤣hhhhhi want learn it laternono, owh, later.....hunh? want to stop today?
#nono,i meam i am curcious how the emoticon appear here, haha....nice...
# .so, since your birtday is so long and if we put seconds, it will take forever to run...so, we use days, instead of seconds, hhaha, want to run?oh,it appeared happy birthday
#something wrong? no, nothing is wrong, since machine doesn't know differnce between days or seconds, it works on execution...haha, so, the function was just to demonstrate.....
#it won't take 42 days to run....for you and me, its days, but for machine its just a number....umm, if you want to simulate it, I have something, that I leared before....
#let me paste....
import time

def birthdaycountdown(days):
    seconds = int(days * 24 * 60 * 60)
    return seconds

total_seconds = birthdaycountdown(42)  # ~86 seconds for demo, now real 42 days simulation...
secondcount = 0

while secondcount < total_seconds:
    print(f"{secondcount + 1} seconds passed...")
    time.sleep(1)  # pause for 1 second
    secondcount += 1

print("🎉 Happy Birthday, Xiaoqing! 🎂")

#did you see? it works on real time...because it imports time from your laptop, haha, and we simulated for 86 seconds......if we do complete 42 days, it will keep running until your birthday....haha
#got it?emm......it will now run for 42 days....haha, because I changed days to 42....hhh,see it,, want to wait it finish?😅🤣....
# hhhhhhh,why you can use emotion (emoji), because windows have a shortcut, window key + . (so, it will show a box for gifs, stickers and emoji's), haha, idk if mac have it.....oh,no,🥹，, owh you can use it.......hhhhhhh, CooL🤣，but just i use pinyin拼音，hhhh, got it miss👏👌hhhh, got it....I want to eat dinner....🫶🏼☠️，and i will learn "for"tommorrow,hhh....okay, since you are on periods .....byebyebye💗love you
