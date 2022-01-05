# def outer_func(message):
# 	def inner_func():
#  		print(message)

#  		return inner_func

# new_var=outer_func('hello')

# new_var()


# def decorator_func(func):
# 	def wrapper_func():
# 		return func()
# 	return wrapper_func

# def display():
# 	print('hello world')
# 	print('this is a display function')
# def about():
# 	print('this is an about func')
# 	print('hello world')

# dec_disp= decorator_func(display)
# dec_disp()

# about_func = decorator_func(about)
# about_func()
# display()
# about()






# def decorator_func(func):
# 	def wrapper_func():
# 		print('hello world')	
# 	return func()
# return wrapper_func

# @decorator_func(name,age):
# def display_info(name,age):
# 		print(f'display_info ran with args({name},{age})')
# 		display_info('john',26)

# display()
# about()


def demo(*z):
	print(z)
demo(1,2,3,4,5)