#Local Scopes Cannot Use Variables in Other Local Scopes

# eggs = 99
def spam():
    eggs = 99
    bacon()
    print(eggs)

    
def bacon():
    ham = 101
    eggs = 0

spam()

# eggs = None
def spam():
    eggs = bacon()
    print(eggs)

    
def bacon():
    eggs = 0
spam()

# eggs = 0
def spam():
    eggs = bacon()
    print(eggs)

    
def bacon():
    return 0
spam()


#Local and Global Variables with the Same Name
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)
eggs = 'global'
bacon()
print(eggs)
