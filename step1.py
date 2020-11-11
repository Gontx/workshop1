def calculate():

    #user input
    operation = input('''
    Enter the operation you would like to perform: 
    + for addition
    - for subtraction
    x for multiplication
    / for division
    ^ for power
    ''')

    num_A = int(input('Enter your first number: '))
    num_B = int(input('Enter your second number: '))

    #addition
    if operation == '+':
        print(num_A , '+' , num_B, '=')
        print(num_A + num_B)

    #subtraction
    elif operation == '-':
        print(num_A , '-' , num_B, '=')
        print(num_A - num_B)

    #multiplication
    elif operation == 'x':
        print(num_A , 'x' , num_B, '=')
        print(num_A * num_B)

    #division
    elif operation == '/':
        print(num_A , '/' , num_B, '=')
        print(num_A / num_B)

    #power
    elif operation == '^':
        print(num_A , '^' , num_B, '=')
        print(num_A ** num_B)

    #no option in list chosen
    else:
        print('You entered an invalid operation!')

while True:
    calculate()
    cont = input('''
    Would you like to do more operations? 
    Type Y or N
    ''')
    if cont == 'Y':
        continue
    elif cont == 'N':
        break
    else:
        print('You entered an invalid answer! Shutting down calculator...')
        break
