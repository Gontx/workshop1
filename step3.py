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
        return (num_A // num_B)

file = open('step_3.txt')
list = file.read().splitlines()
res = 0
i = 0
j = 0
hist = []

while True:
    line = list[i].split()
    if line[0] == 'goto':
        if line[1] == 'calc':
            i = calculate(line[2] , int(line[3]) , int(line[4])) - 1
            hist.append(line)
        else:
            i = int(line[1])-1
            hist.append(line)
    if hist[j] in hist[0:-1]:
        print('Break line number: ' , i )
        print('Break statenemnt: ', hist[j])
        break

    
    
        
