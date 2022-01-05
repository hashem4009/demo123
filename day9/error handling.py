# f= open('day9.py')
# print(f.read())
# f.close()
# print(f.closed)



try:
	f = open('day9')

except FileNotFoundError as e:
		print(e)
except NameError as e:
	 print(e)

except Exception as e:
	print(e)
else:
	print(f.read())
	f.close()



	# new_var = old_var
# except FileNotFoundError:
# 	print('sorry file does mot exist')
# except ExceptION:
# 	print('somehing went worng')
# 	