from sre_parse import parse_template


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
    
def increase_pets_sold(pet_shop, npets):
    pet_shop["admin"]["pets_sold"] += npets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])   
    
# def get_pets_by_breed(pet_shop, breed):
#     for pet in pet_shop["pets"]:
#         if pet_shop["pets"]["breed"] == "British Shorthair":
#             return pet_shop["pets"]["breed"]
#         else:
#             pass

# def get_pets_by_breed(pet_shop, breeds):
#     for pet in pet_shop["pets"]:
#         same_breed = []
#         breeds = pet_shop["pets"]["breed"]
#         if same_breed in breeds:
#             same_breed.append(breeds)
#             return len(same_breed)
#         else:
#             pass

# go through each pet's breed
# if the breed found is equal to our parameter, add it to same_breed
# return length of same breed
# My solution:
# def get_pets_by_breed(pet_shop, breed_to_find):
#     same_breed = []
#     for pet in pet_shop["pets"]:
#         if pet["breed"] == breed_to_find:
#             same_breed.append(pet["breed"])
#     return same_breed

# Correct solution:
def get_pets_by_breed(pet_shop, breed_to_find):
    same_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_to_find:
            same_breed.append(pet)
    return same_breed

# def find_pet_by_name(pet_shop, pet_x):
#     pet_x = None
#     for pet in pet_shop["pets"]:
#         if pet_x == pet["name"]:
#             return pet_x

# def find_pet_by_name(pet_shop, pet_x):
#     for pet in pet_shop["pets"]:
#         if pet["name"] == pet_x:
#             return pet_x
#     return pet_x

# def find_pet_by_name(pet_shop, pet_x):
#     for pet in pet_shop["pets"]:
#         if pet["name"] == pet_x["name"]:
#             return pet_x["name"]
#     return pet_x["name"]

# def find_pet_by_name(pet_shop, name_pet):
#     for pet in pet_shop["pets"]:
#         if pet["name"] == name_pet:
#             return name_pet
#         else:
#             pass
#     return name_pet
       
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if find_pet_by_name(pet_shop,name) == pet:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

# def remove_customer_cash(customers, cash_left):
#     for customer in customers:
#         cash_left = customer["cash"] - new_pet["price"]
#     return cash_left
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)



# OPTIONAL

# My solution: (it works, it's ok)
# def customer_can_afford_pet(customer, new_pet):
#     if customer["cash"] >= new_pet["price"]:
#         return True

# def customer_can_afford_pet(customer, new_pet):
#     if customer["cash"] >= new_pet["price"]:
#         return True
#     else:
#         return False

# def customer_can_afford_pet(customer, new_pet):
#     if customer["cash"] >= new_pet["price"]:
#         return True
#     elif customer["cash"] == new_pet["price"]:    WE ACTUALLY DON'T NEED THE ELIF, CAUSE EQUAL IS CONTAINED IN THE PREVIOUS IF STATEMENT
#         return True
#     else:
#         return False

# Solutions:
def customer_can_afford_pet(customer, new_pet):
    return customer["cash"] >= new_pet["price"]