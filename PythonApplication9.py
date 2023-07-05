# -*- coding: cp1251 -*-


def fac(n):

 if n == 0:

  return 1

 return fac(n-1) * n

y=int(input())

for i in range(y,0,-1):

 print(fac(i))




import collections

pets = {
    1:{
            "������": {
                "��� �������": "������",
                "������� �������": 9,
                "��� ���������": "�����"
            },
        },
    2:{
            "���": {
                "��� �������": "���������� �����",
                "������� �������": 14,
                "��� ���������": "����"
            },
        },
}


def get_suffix(age):
    if age == 1:
        return "���"
    elif age > 1 and age < 5:
        return "����"
    else:
        return "���"


def create():
    print("### �������� create")
    key = input("������ �������: ")

    fields = ["��� �������", "������� �������", "��� ���������"]
    temp = {key: dict()}
    for field in fields:
        res = input(f"{field}: ")
        temp[key][field] = int(res) if res.isnumeric() else res

    last = collections.deque(pets, maxlen=1)[0]
    pets[last+1] = temp


def read():
    print("### �������� read")
    ID = int(input("������� ID: "))

    pet = get_pet(ID)
    if not pet:
        print(f"��� ������� � ����� ID:{ID}")
        return

    key = [x for x in pet.keys()][0]
    string = f'��� {pet[key]["��� �������"]} �� ������ "{key}". ' \
           f'������� �������: {pet[key]["������� �������"]} {get_suffix(pet[key]["������� �������"])}. ' \
           f'��� ���������: {pet[key]["��� ���������"]}'
    print(string)


def update():
    print("### �������� update")
    ID = int(input("������� ID: "))
    pet = get_pet(ID)
    if not pet:
        print(f"��� ������� � ����� ID:{ID}")
        return
    kkey = [x for x in pet.keys()][0]
    print("������� ������ ��� �������� ���� ������. ������� Enter")

    temp = dict()
    for key, value in pet[kkey].items():
        res = input(f"{key}: ")
        if res:
            temp[key] = int(res) if res.isnumeric() else res

    pet[kkey].update(temp)


def delete():
    print("### �������� delete")
    ID = int(input("������� ID: "))
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
    print("������ ��������� �������:")
    for key in commands:
        print("> ", key)

while True:
    print_commands()
    command = input("������� �������: ")

    if command not in commands.keys():
        continue

    if command == "stop":
        break
    commands[command]()
    input("����������...")