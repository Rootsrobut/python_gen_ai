chai_type='Ginger chai'
customer_name='Priya'
print(f"order of {customer_name} : {chai_type} please!")

chai_description='Aromatic and Bold'
print(f'First word {chai_description[:8]}')
print(f'Last word {chai_description[12:]}')
print(f'Reverse the hole string {chai_description[::-1]}')

label_text = 'chai special ha'
encoded_label = label_text.encode('utf-16')
print(f'Non Encoded label : {label_text}')
print(f'Encoded label : {encoded_label}')
decoded_label = encoded_label.decode('utf-16')
print(f'Decoded label : {decoded_label}')
