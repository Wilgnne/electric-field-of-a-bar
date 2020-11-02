import math

def distance (a, b):
  return b - a

def sub_parts(init, end, subpartitions):
  width = distance(init, end)
  half_width = width / 2.0
  half_subpartitions = int(math.floor(subpartitions / 2))

  distance_between_particles = width / float(subpartitions)
  half_distance_between_particles = distance_between_particles / 2.0
  
  middle = init + half_width

  parts = []

  initial_step = half_distance_between_particles
  if subpartitions % 2 != 0:
    initial_step = distance_between_particles
    parts.append(middle)

  #Left
  current_point = middle - initial_step
  for i in range(half_subpartitions):
    parts.append(current_point)
    current_point -= distance_between_particles

  #Right
  current_point = middle + initial_step
  for i in range(half_subpartitions):
    parts.append(current_point)
    current_point += distance_between_particles

  parts.sort()
  return parts

def electric_field(q, d):
  k = 8.99e9
  E = (k * abs(q)) / float(d**2)
  return E


def electric_field_bar(init, end, subpartitions, q, origin):
  sub_q = q / float(subpartitions)

  particles = sub_parts(init, end, subpartitions)

  electric_fields = map(lambda particle: electric_field(sub_q, distance(0, particle)), particles)

  return sum(electric_fields)
