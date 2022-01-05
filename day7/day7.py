def square(x):
	return x * x

def cube(x):
	return x * x * x
# result = square
# print(square(8))


# [1,2,3,4] ---> [1,4,9,16]

# for i in [1,2,3,4]: 
# 	print(i*i)



def my_sq(func, lst):
	for i in lst:
		print(func(i))

my_sq(square, [1,2,3,4])

def my_sq(func, lst):
	result = []
	for i in lst:
		result.append(func(i))
		return result 

print(my_sq(square, [1,2,3,4]))
print(my_sq(cube, [1,2,3,4]))

# def outer_func():
# 	message = 'hi'

# 	def inner_func():
# 		print(message)

# 	return inner_func()

# outer_func()