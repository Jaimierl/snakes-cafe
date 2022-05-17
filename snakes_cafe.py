intro = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
# Three Quotes are needed to print something with its existing formatting. 

print(intro)

menu = ['Wings', 'Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears' ]
    # Menu of options in a list
order = []
    # Menu of what the user chooses in a list

party_on=True
# This is the variable set to run the program while there are inputs and quit if quit is called from the elif. 
while party_on:
    food = input("> ") # Lets have this cool prompt icon for the user to input their choices

    if food in menu:
        order.append(food)
        #Add the user choice to the user choice list
        times=order.count(food)
        print ('** ' + str(times) +' order(s) of '+ food +' has been added to your meal**')

        print ('So far you have ordered: ')
        print (order)

    if food == 'quit':
        party_on = False
        print('Goodbye')
        exit()

    elif food not in menu:
        print ('Sorry, that is not on the menu.')