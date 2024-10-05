tYear = str(input('Введите дату в календаре Тимея в формате <номер олимпиады.год)>: '))
tYearNums = [0, 0]
gYear = -780
isOlimp = False

#yYear.split()
for i in range(len(tYear) - 1, -1, -1):
    if tYear[i] == '.':
        print(i, 'Dot')
        isOlimp = True
        i-=1
        continue
    elif isOlimp:
        tYearNums[0] += int(tYear[i]) * (10 ** (len(tYear) - (i+3)))
        print(i, tYearNums[0])
    elif not isOlimp:
        tYearNums[1] = int(tYear[i])
        print(i, tYearNums[1])
    else:
        print('Error: Stupid charecter in it')

print(-780 + tYearNums[0] * 4 + tYearNums[1])
gYear += (tYearNums[0] * 4) + tYearNums[1]
print(gYear)
if(gYear < 0):
    print(f'{gYear * -1} до н.э.\nИли {gYear * -1 + 1}, если после Июля')
else:
    print(f'{gYear} н.э.\nИли {gYear + 1}, если после Июля')