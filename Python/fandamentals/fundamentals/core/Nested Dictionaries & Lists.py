x = [ [5,2,3], [10,8,9] ] 
x[1] [0]=15
print (x)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]["last_name"] = "Bryant"
print (students[0])

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory ['soccer'] [0]="Andres"
print (sports_directory)


z = [ {'x': 10, 'y': 20} ]
z [0] ['y']=30
print (z)

#Iterate Through a List of Dictionaries#

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(some_list):
    for i in range(len(some_list)):
        for key in some_list[i].keys():
            print(key, some_list[i][key])

# Get Values From a List of Dictionaries

def iterateDictionary(some_list):
    for i in range(len(some_list)):
        name1 = []
        for key in some_list[i].keys():
            name1.append(key)
            name1.append(some_list[i][key])
            print(f"{name1[0]} - {name1[1]}, {name1[2]} - {name1[3]}")
            iterateDictionary(students) 


def iterateDictionary2(key_name, some_list):
    for ls in some_list:
        print(ls[key_name])


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2('first_name', students)

iterateDictionary2('last_name', students)



def printInfo(some_dict):
    for key, val in some_dict.items():
        val_length = len(some_dict[key])
        key_name = key.upper()

        print(val_length, key_name)

        for i in range(val_length):
            print(some_dict[key][i])


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)





