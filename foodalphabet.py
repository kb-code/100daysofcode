foods = [['apple'], ['banana'], ['carrot'], ['date'], ['eggplant'], ['fennel'], ['gourd'], ['honey'], ['iceburg lettuce'], ['jalapeno'], ['kale'], ['lemon'], ['mango'], ['nutmeg'], ['orach'], ['pinto bean'], ['quince'], ['rambutan'], ['spinach'], ['tomato'], ['ugli fruit'], ['vanilla'], ['watermelon'], ['xouba'], ['yam'], ['zucchini']];

player = input('What is your first name?')

print('Hello, and welcome to the food alphabet game ' + player +'!')
print('Here is the objective...')
print('You will be asked to name a food starting with each letter of the alphabet.')
print('When possible, please enter the singular form of that food. Ex: bean, not beans.')
print('If you name a food that is already in the list, the game progresses but you do not get a point.')
print('If you name a food not already in the database, you get a point!')
print('If you cannot answer at all, you lose a point.')
getstarted = input('Type y when you are ready to start: ')

def playgame(player):
    userpoints = 0;
    newwords = 0;
    print('All right, ' + player + ', answer each question to proceed...')

    for i in range(0, 26):
        print('Your current score is: ', userpoints)
        firstletter = foods[i][0][0];
        userfood = input('Name a food that begins with ' + firstletter + ': ')
        userfood = userfood.lower()

        if(len(userfood) == 0):
            print('You did not provide an answer. You lose a point.')
            userpoints = userpoints - 1
        elif (userfood[0] != firstletter):
            print(userfood.capitalize() + ' was not a valid answer. You lose a point.')
            userpoints = userpoints -1
        elif (userfood in foods[i]):
            print(userfood.capitalize() + ' is already in the database. You do not get a point.')            
        elif (userfood not in foods[i]):
            print('You have guessed a new food! ' + userfood.capitalize() + ' will be added. You get a point!')
            userpoints = userpoints + 1
            newwords = newwords + 1
            foods[i].append(userfood)
    
    print('Well done, you have completed the game.')
    print('Your total score is: ', userpoints)
    print('You added a total of ' + str(newwords) + ' to the database!')
    getstarted = input('if you would like to play again, press y')

    if (getstarted == 'y'):
        playgame(player)

if (getstarted == 'y'):
    playgame(player)


