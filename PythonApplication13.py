
# -*- coding: cp1251 -*-


class Cassa:

 summa=6816654

 def top_up(self, pokup):

  self.pokup=pokup

  pokup+=Cassa.summa

  return f"� ����� {pokup}"

 def count_1000(self):

  print(Cassa.summa//1000)

 def take_away(self, x):

  if x<=self.summa:

   self.summa-=x

  else:

   return f"�� ���������� �����"

r=Cassa()

print(r.top_up(125))
print()




class Turtle:

 def __init__(self, x, y, s):

  self.x = x

  self.y = y

  self.s = s

 def go_up(self):

  self.y += self.s

  return self.y

 def go_down(self):

  self.y -= self.s

  return self.y

 def go_left(self):

  self.x -= self.s

  return self.x

 def go_right(self):

   self.x += self.s

   return self.y

 def evolve(self):

  self.s += 1

  return self.s

 def degrade(self):

  if self.s <= 0:

   print('s = 0')

  return

  self.s -= 1

  return self.s

 def count_moves(self, x2, y2):

  return self.x-x2, self.y- y2

r=Turtle(5, 15, 26)

print(r.go_up())

print(r.go_down())

print(r.go_left())

print(r.go_right())

print(r.evolve())

print(r.degrade())

print(r.count_moves(12,10))