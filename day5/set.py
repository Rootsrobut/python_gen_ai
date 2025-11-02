# 1. Create a sample set
my_set = {1, 2, 3, 'a', 'b'}

essential_spices={"Salt","Black Pepper","Turmeric","Star Anise", "Cardamom", "Nutmeg","ginger"}
optional_spices={"Bay Leaf", "Fennel Seed","Star Anise", "Cardamom", "Nutmeg","ginger"}




all_spices=essential_spices | optional_spices

print(f"All spices : {all_spices}")

common_spices=essential_spices & optional_spices

print(f"common spices : {common_spices}")

only_in_essential=essential_spices - optional_spices

print(f"only in essential : {only_in_essential}")


# mylist = ['apple', 'banana', 'cherry']
# x = frozenset(mylist)
# x[1] = "strawberry"







