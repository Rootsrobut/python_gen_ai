# import arrow
from collections import namedtuple
# brewing_time = arrow.utcnow()
# brewing_time_rome = brewing_time.to("Europe/Rome")
# print(f"Brewing time in Rome: {brewing_time_rome}")
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])
my_chai = chaiProfile(flavor="spicy", aroma="earthy")
# Access fields
print(f"Flavor: {my_chai.flavor}")
print(f"Aroma: {my_chai.aroma}")