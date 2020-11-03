from electric_field import electric_field_bar, coulomb_law_bar, distance

def diff(a, b):
  return ((b-a)/a)

print('Electric Field of a bar:')
print('1 - to calculate the electric field of a bar in relation to a point with n subdivisions')
print('2 - to calculate the number of subpartitions needed to achieve a minimum pressure')

option = input()
while (option not in ['1', '2']):
    print('invalid option, try again')
    option = input()

point = float(input('insert the point: '))
init = float(input('insert the start of the bar: '))
end = float(input('insert the end of the bar: '))
q = float(input('insert the bar charge: '))

#Campo elétrico por integração da lei de Coulomb
print("Calculating electric field by integrating Coulomb's law...")
iE = coulomb_law_bar(q, distance(point, init), distance(init, end))

if option == '1':
    subpartitions = int(input('insert the number of subpartitions of bar: '))

    print(f"Calculating the electric field for {subpartitions} point charges...")
    E = electric_field_bar(init, end, subpartitions, q, point)

    print('The electric field of this bar in relation to the point {:e} is {:e}'
        .format(point, E))
    print(f'and the percentage error is {diff(E, iE)*100}%')

elif option == '2':

    minDiff = float(input('insert the minimum accuracy in %: ')) / 100.0
    #Campo elétrico atual
    x = 1
    #subpartições atuais
    subpartitions = 0

    print("{}\t   {}\t\t    {}\t\t\t    {}"
        .format('n', 'x', 'E', 'diff'))

    while(diff(x, iE) > minDiff):
        subpartitions = subpartitions + 1
        x = electric_field_bar(init, end, subpartitions, q, 0)
        print("{}\t - {:e}\t == {:e}\t ~= {}%"
            .format(subpartitions, x, iE, diff(x, iE)*100))

    print(f"The number of subpartitions to achieve a minimum accuracy of {minDiff*100}% is {subpartitions}.")
