print('Hi there, who are you')
name = input()
if name == 'Roy':
    print('Welcome, Roy.')
else:
    print('How old are you, ' + name)
    age = input()  #input() evaluate to a string
    if int(age) < 18:
        print('Go Away!')
    elif int(age)<25:
        print('Welcome, ' + name)
    else:
        print(name + ', you are too old for this shit')
        
