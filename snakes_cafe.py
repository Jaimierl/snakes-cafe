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

print(intro)

party_on=True
while party_on:
    food = input("> ")

    menu = ['Wings', 'Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears' ]


    if food in menu:
        print ('**1 order of '+ food +' has been added to your meal**')

    if food == 'quit':
        party_on = False
        print('Goodbye')

    elif food not in menu:
        print ('Sorry, that is not on the menu.')