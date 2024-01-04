def addAnimal(zoo, myName):
    animal = dict()
    found = False
    for a in zoo:
        if myName in a.keys():
            a[myName] += 1
            found = True
            #break
        if not found:
            animal[myName] =1
            zoo.append(animal)

zoo = [{"kecske": 1}, {"béka": 1}]
animal = dict()

print("Ez egy állatkert.")
print("Állat hozzáadása (1) - elvétele (2) - kilépés (0)")
select = None
while select != "0":
    select = input("Mit szeretnél tenni? ")
    if select != "0":
        if select == "1":
            name = input("A dög neve: ")
            addAnimal(name)
        elif select == "2":
            removeName = input("Eltávolítandó állat neve: ")
            for a in zoo:
                if name in a.keys():
                    if a[name] > 0:
                        a[name] -= 1
                    else:
                        del a[name]

print(f"Második: {zoo}")

                


