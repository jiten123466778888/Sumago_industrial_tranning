# Write a python program to multiplies all the items in the list.

def multiplying_List(user_List) :
     
    # Multiply elements one by one
    result = 1
    for x in user_List:
         result = result * x
    return result
     
# importing list 
list2 = [10,20,30,40,50,60,70,80,90]

# return the multiplied result
print(multiplying_List(list2))