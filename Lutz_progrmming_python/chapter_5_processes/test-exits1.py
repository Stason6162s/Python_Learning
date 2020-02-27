import sys

try:
	sys.exit(42)
except SystemExit:
	print(f'\n\tIgnored exit func')