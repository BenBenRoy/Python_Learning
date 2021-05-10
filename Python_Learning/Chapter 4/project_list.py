''' List Practice Project
Spam = ['apple', 'bananas','tofu', 'cats']

Object:
1. Write a function
2. Take list value as argument
3. Return string with all the items seperated by a comma and a space, and and 'and'
   inserted before the last item
4. Returned value should be 'apples, bananas, tofu, and cats'
'''




def list_list(list_input):
    cardinality = len(list_input)
    if cardinality == 0:
        print('There is nothing')
    elif cardinality == 1:
        print_value = list_input[0]
        print(print_value)
    elif cardinality == 2:
        print_value = list_input[0]
        print(str(print_value) + " and "+ str(list_input[1]))
    else:
        print_value = list_input[0]
        for i in range(1, cardinality-2):
            print_value = str(print_value) + ", " + str(list_input[i])
        print_value = print_value + ", and " + str(list_input[cardinality-2])
        print(print_value)
    

        
    
