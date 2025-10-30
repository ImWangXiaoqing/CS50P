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


# def praise(name):
#     print(f"你真棒，{name}")
#
# praise("xiaoqing") # CooL, you are awesome Xiaoqing....hhhhh,hhhh, understood?yeah, write one more function while using 4 outside variables, this is your task.let me try,
# # sure...!
# def register(name,age,sex,nationality):
#     print (f"基本信息：{name} {age} {sex} {nationality}")#here?, no...
#
# register("王小青", "18", "女", "中国")#why , you are not using "," between variables, here............!like this?, haha, like this.got it, good....

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

# def checkeligibility(age, country):
#     if country == "North Korea":
#         return "Yes, Since you are north korean, you can get married"
#     elif age > 21:
#         return "Yes, You can get married, you are above 21"
#     elif age<21:
#         return "You can't get married!"

#eligibilitystatus = checkeligibility(19, "North Korea")ok
# eligibilitystatus = checkeligibility(19, "China")
# print(eligibilitystatus)
#got it , good......so, you understand, these are very helpful....emm i remmember “if” can use in 循环语句, yes, loops are there too, if and else can be used anywhere depending on needs..
#got it, okay, since you have mentioned loops, lets learn them....but first lets understand, "and" and "or" operations

#_______________________________and or_______________________________________#
#and is used to define, both, means, if some condition is fulfilling two or more conditons, lets say, you will only get married to someone, if you have a business and above age of 25
#and you will get married, if you are either older than 25 or have business irrespctive of age.....

# def canigetmarried(age, occupation):
#     if age>=25 and occupation=="business": #here, I'm saying, only get married if both condition are fulfilling, otherwise don't, so "and" needs both conditions to be true.
#         return "yes, you can get married!"
#     else:
#         return "you can't get married"
# cangetmarriedornot = canigetmarried(25, "business")
#
# print(cangetmarriedornot)
#
# def anotherexample(age, occupation):
#     if age>=25 or occupation=="business": #here, I am saying if any of these 2 condtion is true, you are good to get married, so "or" gets used in these type of conditions.....
#         return "yes, you can get married!"
#     else:
#         return "you can't get married"
#
# exampleresult = anotherexample(19, "business")
# print(exampleresult) #okay?ok....

#Task: Write a function, that check the eligibility to apply for VISA for different countries
#Task requirement: Only let the user apply if he is applying to India, China, Germany and Switzerland, and also, he/she must be 18 years old....otherwise, return "you can't apply";what wrong, I think connection got lost...
#write now...
#do it...feel free to ask any clarifications
# def canapplyvisa(age,country):
#     if age>=18 and (country=="India" or country=="China" or country=="Germany" or country=="Switzerland"):    #wrong? yes....why, think for a min, make use of "or" for diff countries, you can't just write directl
#         return "yes,you can apply"
#     else:
#         return"you can't apply"
#
# example=canapplyvisa(18,"India") #oh,no how to copy words use keyboard, in Mac you can use, "Command + C" to copy and "Command+V" to pastei  i do it but appear something wrong,you see, yes, I saw...I don't know what happened, but I will check and tell you later....ok
# print(example)
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
while count<3:
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

# def birthdaycountdown(days):
#     seconds = int(days * 24 * 60 * 60)
#     return seconds
#
# total_seconds = birthdaycountdown(42)  # ~86 seconds for demo, now real 42 days simulation...
# secondcount = 0
#
# while secondcount < total_seconds:
#     print(f"{secondcount + 1} seconds passed...")
#     time.sleep(1)  # pause for 1 second
#     secondcount += 1
#
# print("🎉 Happy Birthday, Xiaoqing! 🎂")

#did you see? it works on real time...because it imports time from your laptop, haha, and we simulated for 86 seconds......if we do complete 42 days, it will keep running until your birthday....haha
#got it?emm......it will now run for 42 days....haha, because I changed days to 42....hhh,see it,, want to wait it finish?😅🤣....
# hhhhhhh,why you can use emotion (emoji), because windows have a shortcut, window key + . (so, it will show a box for gifs, stickers and emoji's), haha, idk if mac have it.....oh,no,🥹，, owh you can use it.......hhhhhhh, CooL🤣，but just i use pinyin拼音，hhhh, got it miss👏👌hhhh, got it....I want to eat dinner....🫶🏼☠️，and i will learn "for"tommorrow,hhh....okay, since you are on periods .....byebyebye💗love you




#____________________FOR LOOP__________________#
#so, should we start?yep, okay....emm, you have reviewed everything before, right?emm...learn from the 视频，
#ok

#So, A for loop, lets you repeat something to a fixed number of time, its useful when you know the number of times you need to traverse.
#or in range, lets say, you have box, with 8 items, so go through all of them, till range.....

#just for clraification, range in programming starts from 0, not 1, so, when I say index till 8, that means, 0-8, means 9 indexs in total.

#got it?wait got it....you will understand more by examples....

#lets understand basic structure:
#for i in range(5):#what is "i" doing? "i" is basically a pointer, do you know, when we were child, we used to put our finger under words, while reading them? that's exactly same, i is everything inside range, but takes one at a time, I will teach it well....ok
    #print("Hello Xiaoqing!")

#here, range takes a number, until which the loop will run, so this will 5 times, means, 0,1,2,3,4.....and then stop,got it

# for i in range(5):
#     print("Loop is running!")
#     print(f"Right now: i is at {i}")#i didnt understand f",{}"why need add it , f is to tell python that there is a foreign object is coming in this, between string, and {} handles it, and seperates from string, so, that it can be executed well with stirng., so, f told there is something from outside, and {} takes it from outside, and print alongside with string.
#     print("This is end of this round")
#ok, okay, see the output, you will understand the loop as well as relevance of i as a pointer为啥运行后顺序不一样, emm, order is same, where is it diff?sorry saw wrong, ok ok....
#got it?take your time to go through,got it, okay....lets see, what other things we can out in range()

# for i in range(1, 6):
#     print(f"Right now: i is at {i}")

#here, if we put twp numbers, it will run, between them, it will inlcude first number, lets say we have put (a,b). so, it will run from a to b-1, okay?ok
#loop will always run, (b-a) times, got it

#here we have another variation

for i in range(1,10,2):
    print(f"Right now: i is at {i}")

#this takes 3, (a,b,c), a is start point runs till b-1, and c is steps, means, it will run from 1 to 9, but with a gap of 2...1 3 5 7 9? yes yes....run the code, and you will see
#ok, okay, my internet disconnect for a few moments, hhh....sorry,hhh,i see a icon to call, hunh? option to call? owh, yes, via this we can call, and share screen as well..
#wow, want to try?but you maybe also need make texts here,i cant promise understand what you say,ha h owh, okay....we can try and if not works well, will end

#so, these were
#let me go to friend's room, because he is in class....hhh,ok,ok?yes, done...emm...anything wrong?speak something...can you hear ?
# nope...can you hear me?i can hear you ,but you cant hear , maybe your microphone is off....try turning it on, from settings
#i can hear , nice....you speak something as well.,can hear me now?nope....why, idk....why....wait, let me remove my earbuds, speak something,i say, hhh, nope....
#what wrong ?why why why , no idea....ok,there ies other way maybe ,we can talk by qq...owh, okay...maybe, let me end call here...
#you also leave the call...,go on ? umm, okay....are you alone in dorm today?umm, my throat is bit bad today, don't mind,emm...

#lets take word Xiaoqing....
for letter in "Xiaoqing":
    print(letter)
#write the output here: hhh, why your voice is so low....hhhhh🤣 🤣so funny....hhhh
#so, so, output will look like: X, i, a, o ,q, i, n and g,anything wrong?i cant hear you clearly,texts please....hh, I'm saying, try to run the file again, you will
#lets start with nested loops:

# for i in range(1,4):
#     for j in range(1,4):
#         print(f"{i}x{j} = {i*j}")
#what ?  you first had to run it own your own, in mind, without using computer...hhhh, so you will understand it better,got it

#okay, so, you understood, how this nested loop is working? like completely....??hhhh, our talking is so funny🤣
#owh, okay....let do a dry run for you, dry run means, doing something before running the code, step by step to understand the flow

#, outer loop runs first, with 1, inner loop runs then, 1, so output becomes, 1*1=1
#similarly, outer loop runs first, with 1, inner loop runs then, 2, so output becomes, 1*2=2
#similarly, outer loop runs first, with 1, inner loop runs then, 3, so output becomes, 1*3=3

#, outer loop runs second, with 2, inner loop runs then, 1, so output becomes, 2*1=2
#similarly, outer loop runs second, with 2, inner loop runs then, 2, so output becomes, 2*2=4
#similarly, outer loop runs first, with 2, inner loop runs then, 3, so output becomes, 2*3=6

#, outer loop runs third, with 3, inner loop runs then, 1, so output becomes, 3*1=3
#similarly, outer loop runs third, with 3, inner loop runs then, 2, so output becomes, 3*2=6
#similarly, outer loop runs third, with 3, inner loop runs then, 3, so output becomes, 3*3=9

#good...hhhh, you are so smart as well....hhhh

#hhhhh, no no....

#_________________________lists_____________________#
#lets learn list and we will work with it with other things, like function, loops etc....
#list are nothing but, a set of multiple items, like list of food items....how to use it

#in python, we can make lists like this:
gifts = ["flower","heart","love","car","hug"]
#so, this right here is a list of gifts, lets say I want to give you....we can put as many items in it as we want...ook

# to access the elements inside the list, you use indexes, you know what are indexes?
#indexes get assigned automatically, from left to right, in every list, for examples, flower is at index, 0, and hug is at index, 4, ok?
print(gifts[0])
print(gifts[2])

#got it?hhhh...so, we can change the items in it as well...like
gifts[2] = "bed"

#print(gifts) #see, now it have bed instead of love, got it?.....hhh. thanks for correction.....nice...
#we can also add items
gifts.append("ring")#texts please, okay, append is a method, by which you can add items in your list...
print(gifts) #got it? cool....if i want to add something among flower and heart , owh, we can do that...

gifts.insert(1, "cat") #got it? so, insert takes two things, one is index where we want to add, and what we want to add...
print(gifts)

#we can also remove
gifts.remove("flower") #this is to remove an item.got it, okay...
print(gifts)

#we can also loop through the list

for gift in gifts:
    print(gift)

#got it? we can print gifts using it...using loop to iterate over gift items. got it?hhh, maybe...umm, okay...

#if you want to print with respect to each index, we have a method "enumerate()"
#this will output both, index and value at that index

for index, gift in enumerate(gifts):
    print(f"this {gift} is at index {index}")

#got it? what are you saying?got it nice....umm, your roommates are in room?yep, hhh, are you sitting in table?.no,on my bed, why not study on table?messy
#private space .....hhhh, okay...your friend might see you learning python...hhhh, maybe get jealous
#hunh? what did you say? the lunch is in main campus today, because of classes, I will have it at 12:30...

#umm, one more example:
compliments = ["smart", "loving", "kind", "curious"]

for i in compliments:
    print(f"Xiaoqing is {i}")

#got it?okay, got it

#example with numbers:
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum = 0
for i in nums:
    sum += i
    #sum = sum+i#sum+=i, yes we can do this as well...see, same result...got it
print(sum) #see, we can do operations as well.

#umm, I think this is enough for now, I have to shower and eat before class.....umm, I can show you how I push to github...I'm sharing the screen.here, can you see the screen?no, click on call in pycharm and open call window, you can see it there...
#no?here

#____________________________Welcome__________________________#
# can you wait for 5 mins? just 5....sure
#back...ok.here

#today, we will first learn slicing.....it is helpful for getting some specific items from a list, without afffecting whole list
#there are multiple ways, like via indexing or negative indexing...its same as cutting a loaf of bread from a complete bread....just via clean code, so that we don't have to change the whole list
#It helps us preserve the original list, Example

#newlist = ["socks", "undergarments", "buttons", "keyboard", "book", "school", "pencil"]
#so, we can write this to slice, you have written ratios, right?1:2, 3:5 etc???emm, mathematics ratios....100/500, can be written as 1:5, means numerator is 1/5 of denominator
#got it, yes, so we can use the ratio method to get the part of a list

#print(newlist[1:3]) #this means range,  this will print, items from index 1 to 3, similarly there are multiple methods
#print(newlist[:3]) #this means count from start, means index 0 to 2
#print(newlist[5:]) #also count from back, index, index 2 to 6, inclusive of both....this why start from 2, emm, it starts from 5th index, counted form ending, like, seven indexes
#let me explain by examople: a = [10,20,30,40,50,60,70], using [5:] will give ans as [60,70] only
#but [-5:] = will give, [30,40,50,60,70]....

#do you know inclusive and exclusive ranges? no, inclusive means, including the leftmost and rightmost, means, in range of 2-6, we are including 2 and 6 as well with 3,4,5
#and in exclusive, we don't, it remains, 3,4,5, so these methods work in inclusive...got it, okay, few more mthods are there.

#print(newlist[::2]) #this means, step, means, take every second index, means, index, 0,2,4,6 etc.... ok
#print(newlist[1::2]) #means first number is deciding start index from left, and then step by 2, so since it is 1, we leave one index, which is 0, and then we do, 1,3,5,7 etc, got it?yep
#we also have negative indexes
#print(newlist[-3:]) #means, print last 3....its same, but a little diff, no specific usecase,this.give me an example, [1,2,3,4,5,6,7,8,9] , applying on this will give, [7,8,9],
# owh, I just got the context why you are asking, because I just told you that - reverse, but, its not always true, emm, it depends on the colons,
# if we have dual "::" colons then reverse works, otherwise it starts from last, but in increasing indexes, like, 3 but from last, 7,8,9 not 9,8,7, ::-3 will give this. sorry for confusion
#we can also reverse a list directly
#print(newlist[::-1]) #this will completely covert the list, 0 to 7, 6-1,5-2,4-3....etc...wait , okay, you didn't understand this?yea, here I'm writing that,
# lets say we have 8 elements in a list, 0 becomes index 7, 1 becomes index 6, 2 becomes index 6, and so on....just reversed, example, we have [1,2,3,4,5] becomes [5,4,3,2,1]
#print(newlist[::-2])#what is diff , this will also do stepping, but from ending, like, we have [1,2,3,4,5] and if we use [::2] it will do, 1,3,4 and [::-2] will do, 5,3,1, ok
#so "-"just 颠倒顺序, yes, it just reverses the order...got it
#why we use slicing, when we can do same thing by combining loops and range methods, because this clean, modular, more easier to edit aftee implementation as well directly reverse, without
#extra effort and less lines of code....

#should we move ahead?ok, sorry for confusion, try not to do it again....I could have explained better.hhh.nothing.i can find what i cant understand ,and you will express,so i can understand it better

#okay, happy happy 🫶🏼....you may ask again if you don't understand....ok

#_______________key value pairs_____________#
#so, let say, you have birthday, and you are inviting your friends, but you need complete details about them, so, how do you arrange it in a list,
#like previously, when you only needed name, you can make a list, like [nitish, wxq, Jay chou, jack ma, Xi jinping] so, these are arriving at the party of yours, here you can store directly in list
#you also need extra details about each person, then how do you store it with everyname....? then there comes concept of key-value pairing system

#so, do you understand the problem we have currently?need add some details about each person,like age , yes, age, profession etc things...take your time to process...
#so how to write by key value pairs,what is key?

#so, first of all, we have a existing solution from what we have learnt yet, its is like, we want to save 2 things, we make 2 list of same length
#[nitish, wxq, Jay chou, jack ma, Xi jinping] and make another list, [student, student, Singer , Founder/Entrepreneur, President] ,jay chou is singer, right?yep周杰伦

#so, we have this solution, but this is not very good, we have to create and maintain new lists, if we want to store more items, or details, not very good solution, right?yep
#so, we came up with a new solution....key value pairs....

# we can make use of them....lets see examples: first, lets understand key value concept

# we make a dictionary like thing, that is very similar to dictionary.

#remembeer, when writing key value pairs, we use {} curly brackets...
# exampledictionary = {}
#     "key1":value1,
#     "key2":value2
# understand? we store them like this, this allow us to maintain details at one place, how? this we will see....got it till here?yep, okay...

wxq = {
    "name":"Xiaoqing",
    "age":18,
    "country":"china",
    "profession":"student",
    "contact":{"email":"wxq@gmail.com", "number":"1234567890"}
}
#got it? we can write like this....got it, okay....so, like this we can make multiple such profiles....and access it, let me show you how...
print(wxq["country"]) #this will give me country of wxq...so, in the key-value pairs, we saved the value as china against country, right? so, this gives us the value, using the key...ok?ok

#so, how does this solve our problem? we can make use of nested key value pairs....emm, first understand one more example:
#so, we have this, now, I want to get contact number of wxq, not email, only contact number,then how do we get it?
print(wxq["contact"])#how to add number in it ...so, like you wrote wxq then contact, means contact is inside wxq, and now, number is inside contact, we can do something similar

print(wxq["contact"]["number"]) #we can do same....and keep going inside...why cant write like this :print(wxq["contact"["number "]])
#hmm, I see how you are thinking, you are saying sinde, number is inside contact, we wrote it outside, the reason is scope, we have to take care of scope. scope is nothing but a boundary where each thing can be accessed.
#so, you first wrote wxq["contact"] means you are saying get the value of the key contact inside wxq, so, when we write "contact"["number"] then we are basically saying, get the value at key number, but key and values don't work like that
#they also work on indexes....like, we used to get the value in list as, for example, we have a list, numbers = [1,2,3,4,5], so, when we call, numbers[0] = 1, so, it expects a index inside, [], thus we can't paas a string inside, it expects a index or integer.
#got the idea? leave the scope for now....try to understand without it...got it maybe, are you sure? you may ask questions, promise you understand this?hhh, don't add maybe...emm, let me give example

#listA = [nitish, xiaoqing, personA, personB], so how do we write if we want name on index 1, listA[1], this will give us "xiaoqing", but you were saying why can't we write contact["number"]
#but python only excepts number in such situations, it will give string error... "string must be integers" it will give this error,okk understood?...
#please let me know if you have any questions....feel free,ok, okay...


#your task, make profile of yourself, where you have two email provider, google and qq and from each provider you have 2 emails, can you write it?just write contact ?emm,yea...
contact = {
    "number":"19329269209",
    "email":{"google":{"email1":"wxq@gmail.com", "email2":"wqx@gmail.com"},"qq":{"email1":"wxq1013922@qq.com", "email2":"wqx1013922@qq.com"}}#what is wrong? you forgot "," after writing one key value pair, you must write ","ok, done?yeah

}
#are you sure?emm...no, emm, no? why do you think so? read the task again, yes, 2 from each provider....should I write it for you?i think i need,okay
#like you make a key value pair inside email, we can make same for google....got it?hhh, both are diff...don't worry and even if the value is same, there is no problem,
# the key must be unique only..ok.got it, nice....

#so, now we can come back to our birthday problem, since now we can make profile of each birthday friend and save each profile into a list of key-value pairs...

invitations = [
    {"name":"Nitish", "age":20, "profession":"student"},
    {"name":"Xiaoqing", "age":18, "profession":"student"},
    {"name":"Jay chou", "age":50, "profession":"singer"},
    {"name":"Jack ma", "age":70, "profession":"founder of alibaba"},
    {"name":"Xi jinping", "age":65, "profession":"president"}
]

#got it? we saved all the participants of the birthday party in one list, previously, we were only able to store only names, now, we can save all others details as well....
#we can access details like:
for invitation in invitations:
    print(f"{invitation['name']} is a {invitation['profession']} aged {invitation['age']}")

#did you understand it xioaqing? take your time...ok, got it? really...?i think so, okay....would you like to do a task?i want to sleep🥱, emm...alright...leave a task as my homework, okay, I will,thannk you ♥️,hhhh, welcome....
#what are you thiking? wanna say something?wait my homework...😄 don't worry, I won't forget it...can i update it in mine now, yes, you can....try it.emm...dont work, this will work in yours, this is mine, you will get the code currently written,
#you can again update in morning and you will get homework...close the pycharm, and open again and open the project of CS50P, then update....let me know via QQ if there are any issus, try it,ok


#NOTE: I have shared HomeWork on QQ, let me know if you have any questions....! Good Morning!