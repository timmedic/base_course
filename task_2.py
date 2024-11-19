name = str(input("Введите имя и фамилию: "))

name = ("_".join(name) + "_")
print(name)

name = name.upper()
print(name)

codes1 = list(map(ord, name))
print("Номера символов сверху", codes1)

name = name.lower()
print(name)

codes2 = list(map(ord, name))
print("Номера символов сверху", codes2)

print("Наибольшие номера из списков:", list(map(max, [codes1, codes2])))
print("Наименьшие номера из списков:", list(map(min, [codes1, codes2])))