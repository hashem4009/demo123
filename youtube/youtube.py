class Cat:
  hair_color = 'red'
  weight = 0.5
  def say_meow(self):
    print('Meow')
  def set_name(self, name):
    self.name = name
    print(self.hair_color,'cat got a name:', self.name)

cat = Cat()
cat.say_meow()
cat.hair_color = 'white'
cat.set_name('Princess')


