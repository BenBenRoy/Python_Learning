#Each data type has its own set of 『methods』.

#Python uses 'references' whenever variables must store values of mutable data types,
#such as 'list' or 'dictionary', For immutable data types ('strings, integers, tuples'),
#Pytho variables will store the value itself.

def eggs(someParameter):
    return 'Hello' +someParameter
    


#deepcopy
import copy
spam = ['A','B','C','D',]
cheese = copy.copy(spam)
cheese[1] = 42


listoflist = [[1,2,3],['A','B','C']]
apple = copy.copy(listoflist)

apple[0][0] = 4          #listoflist is updated, use deep.copy instead

banana = copy.deepcopy(listoflist)
banana[0][0] = 1         #listoflist is not updated



