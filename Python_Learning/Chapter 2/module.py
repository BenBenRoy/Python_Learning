import random,sys  #importing modules; different modules are seperated by ,
for i in range(5):
    print(random.randint(1, 10))

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit() #Ending a program
    print('You typed ' + response + '.')

print('The program has ended') #This expression is not evaluated because of sys.exit
