name = str(input("Введите своё ФИО: "))

def PrintCString(list):
    for i in range(0, len(list)):
        print(list[i], end='')
    print('')

upperName = [char.upper() for char in name]
PrintCString(upperName)
lowerName = [char.lower() for char in name]
PrintCString(lowerName)

print(sum(ord(char) for char in upperName))
print(sum(ord(char) for char in lowerName))