import random

flowers = ["Мак", "Тюльпан", "Колокольчик", "Ромашка", "Роза"]
colours = ["Красный", "Сиреневый", "Белый", "Розовый", "Голубой", "Жёлтый"]
random.shuffle(colours)

dic = dict(zip(flowers, colours))
print(dic)