"""
Continous User Input Task
"""

"""
Task 1) Keep asking the user for an 
input until they give you -1. 
Once you get -1, stop the loop.
"""

#Intent: Through a while loop, go through and check if 
#the value of the input = -1. If it doesn't, loop through
#Once the value gets -1, break out and print: "you broke out!"


# #Solution: 1) 
# #Initializing variables: breakout = -1 
# breakout = False 
# while breakout == False: 
#     user = int(input("ENTER A NUMBER: "))
#     if user != - 1:
#         continue
#     else: 
#         breakout = True 


""" 
Task 2) Take the user input, turn it into a number 
(cast it into an int or a float) and add it to 
an ongoing total sum. After the loop is 
broken/stopped, print out the sum.
"""
"""
#Initialize my variables: End, Numberlist 
addto = 0
end = False

 
#Figure out logistics, then add it into a while loop! 
#1) Feeling through for i in range 
# for i in range(3):
#     useri = float(input("input a number: "))
#     addto += useri
# print(addto)

#2) While loop initiation
while end == False: 
    useri = float(input("enter a number: "))
    addto += useri 
    checker = input("Do you want to continue? (Y/N): ")
    if checker == "Y" or checker == "y": 
        continue 
    elif checker == "N" or checker == "n":
        break
print(addto)
"""

""" 
Task 3: Keep track of how many numbers the user inputted 
"""
# addto = []
# end = False
# counter = 0 
# number = 0
# while end == False: 
#     useri = float(input("enter a number: "))
#     addto.append(useri)
#     counter += 1 
#     checker = input("Do you want to continue? (Y/N): ")
#     if checker == "Y" or checker == "y": 
#         continue 
#     elif checker == "N" or checker == "n":
#         break
# #Doing averages: 
# #Firstly, take the sum of everything in the list 
# for num in addto: 
#     number += num

# print(number)
# print(f"you added: {addto}",f"counter: {counter}")

# end = True

# for i in range(10): 
#     userinput = float(input("Enter No.: "))

# runs=0
# end = False 
# while end == False: 
#     user = input("Do you want to continue?")
#     runs += 1
#     print(runs)
#     if user == "n":
#         end = True

addto = []
end = False
counter = 0 
number = 0


while end == False: 
    useri = float(input("enter a number: "))
    if useri == -1:
        break
    elif useri != -1:
        addto.append(useri)
        counter += 1 
    checker = input("Do you want to continue? (Y/N): ")
    if checker == "Y" or checker == "y": 
        continue 
    elif checker == "N" or checker == "n":
        break

#Doing averages: 
#Firstly, take the sum of everything in the list: DONE!
for num in addto: 
    number += num
average = number / counter

#Task 5: 




# average = number / counter

# print(f"This represents the sum: {number}, This = List {addto}, This = item in list count {counter}")

#Finding the averages of numbers: 
#Step: average is equal to: sum of numbers divided by number of item in list
#STep 2: I have "counter", so I really divide by number/counter

# print(average) (see above) 


#Task 5: min & max number 
minimum = addto[0]
maximum = 0
for comparison in addto:
    if comparison > maximum:
        maximum = comparison 
    elif comparison < minimum:
        minimum = comparison 
 # maximum is found: 
# print(maximum,minimum)

#Task 6: Find the product of all numbers multiplied 
#meaning:
#Example list=[1,2,2,4] it would be: 1*2, then product of that * (1*2)*2, then (1*2*2)*4
#Thinking: for loop 

product_num = 1
for multiply in addto: 
    product_num = multiply * product_num


#Task 7: Find the median in the list: 
addto.sort()
lengthad = len(addto)//2

if lengthad % 2 !=0:
    print(addto[lengthad])
elif lengthad % 2== 0: 
    print(
        (
            (addto[lengthad-1]+addto[lengthad])/2)
    )

#Task 8: Find isPrime

for items in addto: 
    for itemrange in items:
        print(items)






