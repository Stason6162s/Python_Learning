def later():
	import sys
	print('Bye sys world!')
	sys.exit(43)
	print('Never reached') # This nevre reached


if __name__ == '__main__':
	later()