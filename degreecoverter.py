choice = input('select what you\'re converting from c or f? ')
temp = int(input('what is the current temperature you need to convert? '))

if choice == 'c':
    tempconversion = (((temp * 9)/5)+32)
    rndtempconversion = round(tempconversion, 0)
    print(rndtempconversion)
if choice == 'f':
    tempconversion = ((temp - 32)*5/9)
    rndtempconversion = round(tempconversion, 0)
    print(rndtempconversion)