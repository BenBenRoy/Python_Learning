Trial = 1
Trial_Limit = 3
print('Hi there, when is Roy' +"'" + 's birthday')
while True:
    Birthday = input()
    if Birthday == '12/09/1992':
        print('That is right, Welcome Roy')
        break    # when reaches 'break', out of loop
    elif Trial < Trial_Limit:
        Trial = Trial + 1
        print('not correct, please try again')
    else:
        print('Maximum trial limit reached, Goodbye')
        break


##Trial = 1
##print('Hi there, when is Roy' +"'" + 's birthday')
##while Trial < 4:
##    Birthday = input()
##    if Birthday == '12/09/1992':
##        print('That is right')
##        break
##    else:
##        Trial = Trial + 1
##        print('not correct, please try again')
##
##if Trial == 4:
##    print('maximum trial limit reached')
