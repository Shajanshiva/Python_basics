# import json

# #loads - json to python
# data = '{"name" : "Alex","age" : 25,"isStudent": true,"skills": ["python","SQL"],"address" : {"city":"Mumbai","pin code" : 400001} }'
# a = json.loads(data)
# print(a)

# print(a["address"])
# print(a["address"]["city"])
# print(a["skills"][1])
# print(type(a))


# #dumbs - python to json
# data = {"name" : "Alex","age" : 25,"isStudent": True,"skills": ["python","SQL"],"address" : {"city":"Mumbai","pin code" : 400001}}
# a = json.dumps(data)
# print(a)
# print(type(a))

# import json
# import requests
# # Step 1: Make a GET request to the API
# response = requests.get("https://randomuser.me/api/")
# # Step 2: Convert response JSON → Python dict
# data = response.json()
# # Step 3: Extract some values
# user = data["results"][0]
# name = user["name"]["first"]
# email = user["email"]
# city = user["location"]["city"]
# print("Name:", name)
# print("Email:", email)
# print("City:", city)

class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        print(self.a + self.b)
        
    def sub(self):
        print(self.a - self.b)
        
    def multiply(self):
        print(self.a * self.b)
    
    def divide(self):
        print(self.a / self.b)
        
call_num = calculator(10,20)
call_num.add()
call_num.sub()