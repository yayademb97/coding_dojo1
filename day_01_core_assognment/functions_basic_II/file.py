#Countdown
def Countdown(num):
    dojo = []
    for i in range(num, -1, -1):
        print(dojo)
        dojo.append(i)

Countdown(8)
# #Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def Receve(list):
    return list[ 1 ]
print(Receve([2,3]))
# #First Plus Length
def Long(list):
    max = list[0]
    for i in range(len(list)):
        if max < list[i]:
            max = list[i]
    print(max+1)
Long([1,4,10])
#4---Valeurs supérieures à la seconde
def greater(list):
    new_list=[]
    for i in range(0,len(list)-1):
        if list[i]>list[i+1]:
            new_list.append(list[i])
    return new_list
example = greater([8,3,5,7,2])
print(len(example))
print(example)
def Lenght_Value(size,val):
    new_list = []
    for i in range(size):
        new_list.append(val)
    return new_list
examp = Lenght_Value(6,2)
print(examp)



