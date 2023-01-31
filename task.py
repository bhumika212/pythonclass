# # colors = ["yellow","red","orange", "blue", "violet", "red", "white"]
# # colors_to_remove = ["red","violet"]
# # # result=colors = ["yellow","orange", "blue", "white"]

# # fruits = ["apple", "guava", "grapes", "banana", "orange"]
# # # replace "guava" and "grapes" with watermelon
# # #["apple", "watermelon", "banana", "orange"]





# colors = ["yellow","red","orange", "blue", "violet", "red", "white"]
# while colors.count("red",) > 0:
#     colors.remove("red")


# colors.remove("violet")
# print(colors)





# fruits = ["apple", "guava", "grapes", "banana", "orange"]
# fruits.remove("guava")
# fruits.remove("grapes")
# fruits.insert(1,"watermelon")
# print(fruits)



profile = {
    "name": "Ram",
    "gender": "Male",
    "education": [
        {"college": "ABC College", "level": "+2"},
        {"college": "ABC College", "level": "Bachelor"},
    ],
    "addresses":[
        {
            "temporary": {
                "ward": 1,
                 "city": "kathmandu",    
            },
            "permanent": {
                "ward": 2,
                "city":"kavre",
            }
        }
    ]
}

print(f"Name:{profile.get('name')}")
print(f"Gender:{profile.get('gender')}")
educations = profile.get("education")
for education in educations:
    print(f"college: {education.get('college')} and level: {education.get('level')}")

addresses = profile.get("addresses")
for address in addresses:
    print(f"Temporary: {address.get('temporary')}" )
    print(f"Permanent: {address.get('permanent')} ")



addresses = profile.get("addresses")
for address in addresses:
    for key, val in addresses.items():
        print(key, val.get)







