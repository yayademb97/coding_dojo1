x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(x[0][0])
z = [ {'x': 10, 'y': 20} ]
#1--Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)
#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[1]["last_name"]="Bryant"
print(students)
#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]="Andres"
print(sports_directory)
#Change the value 20 in z to 30
z[0]['y']=30
print(z)
#Iterate Through a list of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def Iterate_dictionary(students):
    yaya = ""
    for i in students:
        for key in i:
            yaya += f"{key} - {i[key]}, \n"
    print(yaya)
Iterate_dictionary(students)
#2-- iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
#3--Get Values From a List of Dictionaries
def Iterate_dictionary2(first_name,students):
    for i in students:
        for key,value in i.items():
            if key == first_name:
                print(value)
Iterate_dictionary2('first_name',students)
Iterate_dictionary2('last_name',students)
#4--Iterate Through a Dictionary with List Values
dojo = {
            'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
            'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info():
    for i in dojo:
        print("****************************************")
        for value in dojo[i]:
            print(f"{len(value)} {i.upper()}")
            print(value)
print_info()