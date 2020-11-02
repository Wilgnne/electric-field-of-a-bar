from electric_field import electric_field_bar

def diff(a, b):
  return ((b-a)/a)
init = 1
end = 3

q = 16e-6
subpartitions = 256

Q256 = electric_field_bar(init, end, subpartitions, q, 0)

#Campo eletrico por integração da lei de Coulomb
E = 8.99 * (16/3.0) * 1e3
#Campo eletrico atual
x = 1
#subpartições atuais
subpartitions = 0

while(diff(x, E) > 1e-2):
  subpartitions = subpartitions + 1
  x = electric_field_bar(init, end, subpartitions, q, 0)
  print("{}\t - {:e}\t == {:e}\t ~= {:.5f}%"
    .format(subpartitions, x, E, diff(x, E)*100))

print(f"O numero de subpartição para atingir uma precisão mínima de 1% é {subpartitions}.")
