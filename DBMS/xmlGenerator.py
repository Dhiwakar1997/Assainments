from faker import Faker

import pandas as pd	

import xmltodict

# For student id
from random import randint	

fake = Faker()

def input_data(x):

	# dictionary
	student_data =[]
	#print(dir(fake))
	for i in range(1, x+1):
		temp={}
		temp['id']= randint(1, 100)
		temp['firstName']= fake.first_name()
		temp['lastName']= fake.last_name()
		temp['address']= fake.address()
		temp['schoolEmail']= str(fake.company_email())
		temp['email']= str(fake.safe_email())
		student_data.append(temp)
        
	return {"school":{"student":student_data}}
	
number_of_records = 50
data = input_data(number_of_records)

file=open("student.xml","w")
xmltodict.unparse(data,output=file)

df = pd.DataFrame.from_dict(data["school"]['student']) 
df.to_csv (r'student.csv', index = False, header=True)
