symbols = 'ingot'
symbol_codes = [ord(symbol) for symbol in symbols]
print(symbol_codes)

symbols = 'ingot'
symbol_codes = (ord(symbol) for symbol in symbols)
print(symbol_codes)

for object in symbol_codes:
    print(object)