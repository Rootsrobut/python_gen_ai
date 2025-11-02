import random

def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1
refill = infinite_chai()
for _ in range(3):
    print(next(refill))

recipes = {
    'masala chai': {'ingredients': ['tea leaves', 'milk', 'water', 'sugar', 'cardamom', 'ginger', 'cinnamon', 'cloves'], 'price': 5.0},
    'green tea': {'ingredients': ['green tea leaves', 'water', 'honey'], 'price': 3.5},
    'black tea': {'ingredients': ['black tea leaves', 'water', 'lemon', 'sugar'], 'price': 4.0},
    'oolong tea': {'ingredients': ['oolong tea leaves', 'water'], 'price': 6.0},
    'herbal tea': {'ingredients': ['chamomile flowers', 'water', 'mint leaves'], 'price': 4.5}
}

def infinite_tea_refills():
    count = 1
    tea_types = list(recipes.keys())
    while True:
        tea = random.choice(tea_types)
        yield f"Refill #{count}: {tea}"
        count += 1
tea_refill = infinite_tea_refills()
for _ in range(5): 
    print(next(tea_refill))
