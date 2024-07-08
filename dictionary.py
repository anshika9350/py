dict1={
    "Name": "Anshika",
    "Rollno.":21,
    "Subject":"Science"
}

# # showing keys of dictionary
# print(dict1.keys())

# #showing values in a dictionary
# print(dict1.values())

#updating item in a dictionary
# dict1.update({"model":"hi","marks":90})
# print(dict1)
# dict1["Name"]="Me"
# print(dict1)

#printing the values of keys in the dictionary
# for i in dict1.keys():
#    print(i)

#printing the values of value in dictionary:
# for i in dict1.values():
#     print(i)

# printing the item in dictionary
for i in dict1.items():
    print(i)

#nested dictionary
# students={
#     "riya":{
#         "marks":21,
#         "subject":"eng"
#     },
#     "siya":{
#         "marks":22,
#         "subject":"math"
#     }
# }
# print(students["riya"]["marks"])

#loop through nested dictionary
# for x,obj in students.items():
#     print(x)
#     for y in obj:
#         print(y,":",obj[y])
