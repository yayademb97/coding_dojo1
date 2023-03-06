# Print all integers from 0 to 150.
val = 150
for unicorn in range (1, 151, 1):
    print(unicorn)
print("----------------------------------------------------")
# Print all the multiples of 5 from 5 to 1,000
resultat1=0
for i in range(5, 1001):
    if i%5 == 0:
        resultat1 += i
print(resultat1)
print("------------------------------------------------------")
# Print integers 1 to 100. 
# If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".
val2 = 1000
for i in range (1, 1001):
    if i%10==0:
        print("COding Dojo")
    elif i%5 == 0:
        print("coding")
    else :
        print(i)    
print("------------------------------------------------------")
# Add odd integers from 0 to 500,000, and print the final sum.
# sum =0
for i in range (0, 500000, 1):
    if i%2==1:
        sum+=1
print(sum)
print("------------------------------------------------------")
# # Print positive numbers starting at 2018, counting down by fours
for i in range(2018, -1, -4):
        print(i)
print("------------------------------------------------------")
# flexible Counter - Set three variables: lowNum, highNum, mult.
#  Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult.
#  lowNum 
#  highNum
# mult
def init(Low,High,Mult):
# print('aaaaaaaaaaaaaa')
    for i in range(Low, High+1, 1):
        if i%Mult==0:
            print(i)

init(2,9,3)