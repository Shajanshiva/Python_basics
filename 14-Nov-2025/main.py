# task 1
# class TodoList:
#     def __init__(self):
#         self.task = []

#     def add_task(self, id, task, status):
#         current_task = {"id": id, "task": task, "status": status}
#         self.task.append(current_task)
    
#     def view_all_task(self):
#         print(self.task)

    
    
# shajan = TodoList()
# shajan.add_task(id = 1, task = "Put fuel for bike", status = "pending")
# shajan.view_all_task()

# hanisah = TodoList()
# hanisah.add_task(id = 2, task = "speak properly with shajan", status = "pending")
# hanisah.view_all_task()


# task 2
# class orders:
#     def __init__(self):
#         self.cart =[]
    
#     def add_new_items(self, id, product_name, quantity, price):
#         current_item = {"id" : id, "product" : product_name, "quantity" : quantity, "price" : price}
#         self.cart.append(current_item)

#     def remove_an_item(self,id):
#         for i in range(0, len(self.cart), 1):
#             if id == i["id"]:
#                 self.cart.remove(i)

#     def view_total_cost(self):
#         print(self.cart)

# shajan = orders()
# shajan.add_new_items(id = 1, product_name = "iphone", quantity = 1, price = 80000)
# shajan.view_total_cost()

# task 3
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        value = {"name":name, "phone":phone_number, "email":email}
        self.contacts.append(value)

    def get_phone(self, name):
        for el in self.contacts:
            if name == el["name"]:
                print(el["phone"])

    def update_phone

shajan = ContactBook()
shajan.add_contact(name = "shajan", phone_number = "9788924044", email = "shajan@28.com")
shajan.get_phone(name = "shajan")