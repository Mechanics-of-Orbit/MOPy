import pandas
i = float(input('Enter the Value'))
unit1 = input('Which unit u want to convert from:')
unit2 = input('Which unit u want to convert to:')
out = 1
data = pandas.read_csv('C:/Python Course For App making/Final_Year_Project/.vscode/Major_and_Minor_Bodies.csv')
pl = input('Enter the planet name')

p = data.Major_Body
r = data.Radius
m = data.Mass

planet = list(p)
Radius = list(r)
Mass = list(m)

t = planet.index(pl)
print('{} Radius is {} and Mass is {}'.format(pl,Radius[t],Mass[t]))


if unit1 == 'km' and unit2 == 'km':
    out = i
    print(out)
elif unit1 == 'km' and unit2 == 'miles':
    out = 0.621371*i
    print(out)
elif unit1 == 'km' and unit2 == 'AU':
    out = (6.6846e-9)*i
    print(out)
elif unit1 == 'km' and unit2 == 'DU':
    out = i/Radius[t]
    print(out)

elif unit1 == 'miles' and unit2 == 'miles':
    out = i
    print(out)
elif unit1 == 'miles' and unit2 == 'km':
    out = (1/0.621371)*i
    print(out)
elif unit1 == 'miles' and unit2 == 'AU':
    out = (1.07578e-8)*i
    print(out)
elif unit1 == 'miles' and unit2 == 'DU':
    out = (i/0.621371)/Radius[t]
    print(out)

if unit1 == 'AU' and unit2 == 'AU':
    out = i
    print(out)
elif unit1 == 'AU' and unit2 == 'miles':
    out = (1/1.07578e-8)*i
    print(out)
elif unit1 == 'AU' and unit2 == 'km':
    out = (1/6.6846e-9)*i
    print(out)
elif unit1 == 'AU' and unit2 == 'DU':
    out = (1/6.6846e-9)*i/Radius[t]
    print(out)
