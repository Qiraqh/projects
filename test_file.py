students =[{"name": "Hermione", "house": "Gryffindor"},{"name": "Harry", "house": "Gryffindor"},{"name": "Ron", "house": "Gryffindor"},{"name": "Draco", "house": "Slytherin"}]


gryffindors =[
    student["name"] for student in students if student["house"] == "Gryffindor"]

#for g in sorted(gryffindors):
print(*gryffindors)
