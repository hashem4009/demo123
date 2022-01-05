# def outer_func(message):
# 	def inner_func():
#  		print(message)

#  		return inner_func

# new_var=outer_func('hello')

# new_var()

# def decorator_func(func):
# 	def wrapper_func():
# 		print('hello world')
# 		return func()
# 	return wrapper_func
# @decorator_func
# def display():
	
# 	print('this is a display func')
# @decorator_func
# def about():
# 	print ('this is an about func')
# display()
# about()


# dec_disp = decorator_func(display)
# dec_disp()

# about_func = decorator_func(about)
# about_func()

def decorator_func(func):
	def wrapper_func(*args):
		print('hello world!')
		return func(*args)
	return wrapper_func

@decorator_func
def display():
	print('this is a display func')

@decorator_func
def display_info(name,age):
	print(f'display_info ran with args({name}, {age})')

	display_info('john' , 26)


# def demo(*z):
# 	print(z)
# demo(1,2,34,5)






