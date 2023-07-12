# -*- coding: cp1251 -*-


def f(i): 
    return 1 if i == 1 else i * f(i - 1)
n = int(input('n: '))
spisok = [f(n - i) for i in range(n)]
print(spisok)



import collections

pets = {
    1:{
            "Ìóõòàð": {
                "Âèä ïèòîìöà": "Ñîáàêà",
                "Âîçðàñò ïèòîìöà": 9,
                "Èìÿ âëàäåëüöà": "Ïàâåë"
            },
        },
    2:{
            "Êàà": {
                "Âèä ïèòîìöà": "æåëòîðîòûé ïèòîí",
                "Âîçðàñò ïèòîìöà": 14,
                "Èìÿ âëàäåëüöà": "Ñàøà"
            },
        },
}


def get_suffix(age):
    if age == 1:
        return "ãîä"
    elif age > 1 and age < 5:
        return "ãîäà"
    else:
        return "ëåò"


def create():
    print("### Êîììàíäà create")
    key = input("Êëè÷êà ïèòîìöà: ")

    fields = ["Âèä ïèòîìöà", "Âîçðàñò ïèòîìöà", "Èìÿ âëàäåëüöà"]
    temp = {key: dict()}
    for field in fields:
        res = input(f"{field}: ")
        temp[key][field] = int(res) if res.isnumeric() else res

    last = collections.deque(pets, maxlen=1)[0]
    pets[last+1] = temp


def read():
    print("### Êîììàíäà read")
    ID = int(input("Ââåäèòå ID: "))

    pet = get_pet(ID)
    if not pet:
        print(f"Íåò ïèòîìöà ñ òàêèì ID:{ID}")
        return

    key = [x for x in pet.keys()][0]
    string = f'Ýòî {pet[key]["Âèä ïèòîìöà"]} ïî êëè÷êå "{key}". ' \
           f'Âîçðàñò ïèòîìöà: {pet[key]["Âîçðàñò ïèòîìöà"]} {get_suffix(pet[key]["Âîçðàñò ïèòîìöà"])}. ' \
           f'Èìÿ âëàäåëüöà: {pet[key]["Èìÿ âëàäåëüöà"]}'
    print(string)


def update():
    print("### Êîììàíäà update")
    ID = int(input("Ââåäèòå ID: "))
    pet = get_pet(ID)
    if not pet:
        print(f"Íåò ïèòîìöà ñ òàêèì ID:{ID}")
        return
    kkey = [x for x in pet.keys()][0]
    print("Ââåäèòå äàííûå èëè îñòàâüòå ïîëå ïóñòûì. Íàæìèòå Enter")

    temp = dict()
    for key, value in pet[kkey].items():
        res = input(f"{key}: ")
        if res:
            temp[key] = int(res) if res.isnumeric() else res

    pet[kkey].update(temp)


def delete():
    print("### Êîììàíäà delete")
    ID = int(input("Ââåäèòå ID: "))
    pets.pop(ID, None)


def get_pet(ID):
    return pets.get(ID, False)


def pets_list():
    for key, val in pets.items():
        print(f"ID:{key}", val)


commands = {
    "create": create,
    "read": read,
    "update": update,
    "delete": delete,
    "list": pets_list,
    "stop": 0
}

def print_commands():
    print("Ñïèñîê äîñòóïíûõ êîììàíä:")
    for key in commands:
        print("> ", key)

while True:
    print_commands()
    command = input("Ââåäèòå êîìàíäó: ")

    if command not in commands.keys():
        continue

    if command == "stop":
        break
    commands[command]()
    input("Ïðîäîëæèòü...")
