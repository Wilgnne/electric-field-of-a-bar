from electric_field import campo_eletrico_barra

init = 1
end = 3

q = 16*10e-6
subpartitions = 256

for i in range(1, 257):
  print("{}: {:e}".format(i, campo_eletrico_barra(init, end, i, q, 0)))

