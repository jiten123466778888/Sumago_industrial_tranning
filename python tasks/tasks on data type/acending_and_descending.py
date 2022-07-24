#write a python program to sort (ascending and descending) a dictionary by value.

y={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10} 
                                         
l=list(y.items())   #convet the given dict. into list
l.sort()            #sort the list
print('Ascending order is',l) #this print the sorted list 

l=list(y.items())
l.sort(reverse=True) #sort in reverse order
print('Descending order is',l)

dict=dict(l) # convert the list in dictionary 

print("Dictionary",dict) #the desired output is this sorted dictionary