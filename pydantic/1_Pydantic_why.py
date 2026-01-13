

# def insert_patient_data(name: str, age: int):  
#     print(f"Patient Name: {name}, Age: {age}")
#     print("Data inserted successfully.")

# insert_patient_data("John Doe", "thirty")    # This will not raise an error, even though age should be an integer. type huting is not enforced.


def insert_patient_data(name: str, age: int):
    if type(age) != int:
        raise TypeError("Age must be an integer")
    if type(name) != str:
        raise TypeError("Name must be a string")
    print(f"Patient Name: {name}, Age: {age}")
    print("Data inserted successfully.")
try:
    insert_patient_data("John Doe", "thirty")  # This will raise a TypeError
except TypeError as e:
    print("Type Error:", e)



from pydantic import BaseModel, ValidationError

# step 1: Define a Pydantic model for patient data
class Patient(BaseModel):
    name: str
    age: int
    
# step 2: Use the Pydantic model for data validation
def insert_patient_data(patient: Patient):
    print(f"Patient Name: {patient.name}, Age: {patient.age}")
    print("Data inserted successfully.")
try:
    patient = Patient(name="John Doe", age="thirty")  # This will raise a ValidationError
    insert_patient_data(patient)    
except ValidationError as e:
    print("Validation Error:", e) 