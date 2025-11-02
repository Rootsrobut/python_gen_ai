print('start of pydantic journey')

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id': 101, 'name': "Chaicode", 'is_active': True} #  'is_active': 23 #error  1 validation error

# This line is correct: ** unpacks the dictionary into keyword arguments.
user = User(**input_data) 

print(user)