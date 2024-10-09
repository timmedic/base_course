tYear = str(input('Введите дату в календаре Тимея в формате <номер олимпиады.год)>: '))
tYearNums = [0, 0]
gYear = -780
isOlimp = False

#yYear.split()
for i in range(len(tYear) - 1, -1, -1):
    if tYear[i] == '.':
        isOlimp = True
        i-=1
        continue
    elif isOlimp:
        tYearNums[0] += int(tYear[i]) * (10 ** (len(tYear) - (i+3)))
    elif not isOlimp:
        tYearNums[1] = int(tYear[i])
    else:
        print('Error: Stupid charecter in it')

gYear += (tYearNums[0] * 4) + tYearNums[1]

if(gYear < 0):
    print(f'В Григорианском календаре эта дата - {gYear * -1} до н.э.\nИли {gYear * -1 + 1} до н.э., если после Июля')
else:
    print(f'В Григорианском календаре эта дата - {gYear} н.э.\nИли {gYear + 1} н.э., если после Июля')