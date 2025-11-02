# List

menu = [
"Masala Chai",
"Iced Lemon Tea",
"Green Tea",
"Iced Peach Tea",
"Ginger chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)

# set
favourite_chais=[
    'Masala Chai','Green Tea','Masala chai',
    'Lemon Tea','Green Tea','Elaichi chai'
]
unique_chai={chai for chai in favourite_chais if len(chai)>8}
print(unique_chai)


recipes = {
    'masala chai': ['tea leaves', 'milk', 'water', 'sugar', 'cardamom', 'ginger', 'cinnamon', 'cloves'],
    'green tea': ['green tea leaves', 'water', 'honey'],
    'black tea': ['black tea leaves', 'water', 'lemon', 'sugar'],
    'oolong tea': ['oolong tea leaves', 'water'],
    'herbal tea': ['chamomile flowers', 'water', 'mint leaves']
}
unique_chai={spice for ingredients in recipes.values() for spice in ingredients}
print(unique_chai)



tea_prices_inr = {
    'masala chai': 400,
    'green tea': 500,
    'black tea': 100,
    'oolong tea':200,
    'herbal tea': 432,
}
tea_prices_usd={tea:price/80 for tea,price in tea_prices_inr.items()}
print(tea_prices_usd)

# Generator comprehension
daily_sales=[5,6,7,8,9,12,32,43,45,65,76,78,98]
total_cups_size=sum(sale for sale in daily_sales if sale > 50)
print(total_cups_size_morethen_50)