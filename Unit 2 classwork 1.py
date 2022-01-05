# Unit 2 classwork 1

# 1
list1 = [1,2,3,4,5,6,7]
list2 = [2,4,6,8]
list3 = [1,2,4,5,7]

# 2

def function(anylist):
    print(anylist)
function()
# 3

def Function(anylist):
    count = 0
    newlist = []
    while (count<len(anylist)):
        new = anylist[count]+7
        newlist.append(new)
        count = count + 1
    print(newlist)
Function()
# 4

def function1(anylist):
    count = 0
    smallest_num = anylist[0]
    while (count<len(anylist)):
        if (anylist[count]<smallest_num):
            smallest_num = anylist[count]            
        count = count + 1
    print(smallest_num)
function1()
# 5

def function2():
    done = False
    while (done == False):
        print ("hey user! what's your favourite food")
        food = input()
        if (food == "banana"):
            done = True
            print ("goodjob")
        else:
            done = False

# 6

def function3():
    done = False
    while (done == False):
        print("hey user! what's your lucky number")
        luckynum = int(input())
        if (luckynum == 7):
            done = True
            print("okay, bye")
        else:
            done = False
# Tim_Was_Here



print("hello")
