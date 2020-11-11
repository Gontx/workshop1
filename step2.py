def calculate(operation,num_A,num_B):

    #addition
    if operation == '+':
        return (num_A + num_B)

    #subtraction
    elif operation == '-':
        return (num_A - num_B)

    #multiplication
    elif operation == 'x':
        return (num_A * num_B)

    #division
    elif operation == '/':
        return (num_A / num_B)

def calculate_line(line):
    calc, operation, num_A, num_B = line.split()
    return calculate(operation, int(num_A), int(num_B))

#open file
file = open('step_2.txt')
#split lines
list = file.read().splitlines()
#initialize result value
res = [calculate_line(line) for line in list]
result = sum(res)

print('The addition of all result lines is: ' ,result)