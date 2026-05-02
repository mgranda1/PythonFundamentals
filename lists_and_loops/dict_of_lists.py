# Looping over a dictionary of lists
menus = { 'Breakfast': ['Eggs','Bagel','Coffee'],
          'Lunch'    : ['BLT','PB&J','Turkey sandwich'],
          'Dinner'   : ['Soup','Salad','Taco'] }

for title, food_list in menus.items():
    print('\n',title, 'menu:', sep='')
    for item in food_list:
        print('  ',item)