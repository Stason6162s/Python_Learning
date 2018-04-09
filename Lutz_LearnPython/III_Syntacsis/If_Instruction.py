if 1:
    print(True)
print('\n\t Multiple cases')
choice = 'ham'
print({'eggs': 1,
       'toast': 27,
       'ham': 1.99,
       'spam': 43}[choice])  # analog case or switch
# or using if\elif\else


# while True:
#     choice = input('Enter your choice: ')
#     if choice == 'spam':
#         print('spam')
#         break
#     elif choice == 'eggs':
#         print(choice)
#         break
#     elif choice == 'toast':
#         print(choice)
#         break
#     elif choice == 'ham':
#         print(choice)
#         break
#     elif choice == 'fuck':
#         print(choice)
#         break
#     else:
#         print('bad choice')
#         choice = ''
#         continue

# examples
# if 1:
#     A = Y
# else:
#     A = Z
# print(A)

# may be A=Y if X else Z

A = 't' if 'spam' else 'f'
print(A)

A = 'T' if '' else 'spam'
print(A)