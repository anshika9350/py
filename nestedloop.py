# list1=[1,2,3,4]
# list2=["Why","When"]
# for i in list1:
#     for j in list2:
#         print(i,j)

# list1=[1,2,3,4]
# list2=["Why","When"]
# for i in list1:
#     print(i)
# for j in list2:
#     print(j) 

# list1=[1,2,3,4]
# list2=["Why","When"]
# for i in list1:
#     print(i)
#     for j in list2:
#         print(j)

#accessing list within list
# list1 = [[1,2,3,4],["Why","When"]]
# for i in list1:
#     # print(i)
#     for j in i:
#         print(j)

# multiply the places by 10 and 100
list1 = [[1,2],[3,4]]
# print(list1[0][0])
l2=[]
l3=[]
l4=[]
for i in range(0,2):
    for j in range(0,2,2):
        x=list1[i][j]*10
        l2.append(x)
        y=list1[i][j+1]*100
        l3.append(y)
print(l2,l3)
l4.append(l2) 
l4.append(l3)
print(l4)   