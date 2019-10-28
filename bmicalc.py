weight = float(input('what is your weight? '))
height = float(input('what is your height? (in inches or 5\'5\" would be 5.5) '))

if height < 10:
    height_inches = height * 12
    rnd_height_inches = round(height_inches, 2)
print("Your height in inches is", rnd_height_inches,'inches') 

bmi = ((weight / (height_inches ** 2)) * 703)
rnd_bmi = round(bmi, 2)
print('Your body mass index is', rnd_bmi)

if rnd_bmi > 40:
    print('that is a little high!')
elif rnd_bmi < 20:
    print('that is a little low there bucko!')
else:
    print('yeaaaaahhh your bmi is juuuust righhhhttttt')