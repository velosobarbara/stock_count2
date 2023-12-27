menu = ['Steak Frites', 'Avocado Toast', 'Curry and Rice', 'BLT Sandwich']

stock = { 'Steak Frites' : 4,
         'Avocado Toast' : 3,
         'Curry and Rice' : 5,
         'BLT Sandwich' : 6}

price = { 'Steak Frites' : 10.99,
         'Avocado Toast' : 8.60,
         'Curry and Rice' : 12.00,
         'BLT Sandwich' : 9.00}

#take stock and price values
#multiply both values using range[] funct
#loop through the dictionary to display all items
#display the total worth of each stock (confusion with brief: OR total of all stocks?)

item_value_sf = round((stock['Steak Frites'] * price['Steak Frites']), 2)
item_value_at = round((stock['Avocado Toast'] * price['Avocado Toast']), 2)
item_value_cr = round((stock['Curry and Rice'] * price['Curry and Rice']), 2)
item_value_blt = round((stock['BLT Sandwich'] * price['BLT Sandwich']), 2)

#for loop to display all items in menu (total worth of each stock)
stock_worth = list((x, y * stock[x]) 
                   for x, y in price.items())

print(f"Each item's total stock worth is as displayed below: \n{stock_worth}\n")

#calculation for the total of all stocks (total worth of ALL stocks)
total_stock_worth = item_value_sf, item_value_at, item_value_cr, item_value_blt
final_stock_calcu = sum(total_stock_worth)

print(f"The total worth of all your current stock is as displayed below: \n£{final_stock_calcu}")