sugar_amount=2
print(f"first Initial sugar:{sugar_amount}")

sugar_amount=12
print(f"Second Initial sugar:{sugar_amount}")

print(f'ID of 2:{id(2)}')
print(f'iD of 12:{id(12)}')




spicemix = set()  
print(f'Before insert some value id is {id(spicemix)}')
spicemix.add('cardamon') 
spicemix.add('Ginger')   
print(f'After insert some value id is {id(spicemix)}')