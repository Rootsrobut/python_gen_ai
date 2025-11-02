chai_order=dict(type='Masala chai',size='Large',sugar=2)
print(f'chai order : {chai_order}')

print(f"Is sugar in the order ? { 'sugar' in chai_order}")

chai_recipe={}
chai_recipe['base']='black tea'
chai_recipe['liquid']='milk'

print(f'Recipe base : {chai_recipe['base']}')
print(f'Recipe : {chai_recipe}')
del chai_recipe['liquid']
print(f'Recipe : {chai_recipe}')

# print(f'Order details (keys): {chai_order.keys()}')  
# print(f'Order details (values): {chai_order.values()}')  
# print(f'Order details (Items): {chai_order.items()}')  

last_item=chai_order.popitem()
print(f'Removed last item:{last_item}')

extra_spices = {"'cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print (f"Updated chai recipe: {chai_recipe}")

customer_note=chai_order.get('note','No Note')
print(f"customer_note is : {customer_note}")