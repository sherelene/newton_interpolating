import numpy as np
from decimal import *


def coeff(xs, ys, cs, num):
    print(num)
    for i in range(num):
        cs[i] = ys[i]
        print(f'cs {i} {cs[i]}')
    print("number", num)

    for j in range(1, num):
        for i in range(num-1, j, -1):
            print(f'i {i} - j {j} = {i - j}')
            print(f'x{i}({cs[i]}) - x{i-1}({cs[i - 1]}) / y{i}({xs[i]}) - y{i-j}({xs[i-j]})')
            cs[i] = (cs[i] - cs[i-1]) / (xs[i] - xs[i-j])
            print("=", i, cs[i])

    eval_newton(xs, cs, num)


def eval_newton(xs, cs, num):
    z = 0
    print("num", num)
    user_input = input("Please enter a value to evaluate: ")
    try:
        if user_input == 'q':
            exit()
        z = float(user_input)
    except ValueError:
        print("Error, should have been a number or 'q'")
        exit()

    result = cs[num - 1]
    for i in range(num-1, -1, -1):
        result = result * (z - xs[i]) + cs[i]

    print(result)



def create_arrays(num_of_variables, file_list):

    # initialize new array to store the solved coefficients
    x = np.zeros(num_of_variables, dtype=np.dtype(Decimal))
    y = np.zeros(num_of_variables, dtype=np.dtype(Decimal))
    c = np.zeros(num_of_variables, dtype=np.dtype(Decimal))

    for j in range(num_of_variables):
        x[j] = file_list[0][j]
        y[j] = file_list[1][j]
    print("x", x)
    print("y", y)

    coeff(x, y, c, num_of_variables)



def main():
    filename = "testCase.txt"
    with open(filename) as file:
        # declare array we're going to get from the file
        content = []

        # reads the rest of the lines within the file
        lines = file.readlines()

        cnt = 0
        row =2
        # takes each line read from file and inputs each number in the line into an element into the file content array
        for line in lines:
            content.append(line.split())  # split ignores all unnecessary characters like \n or whitespace

        n = int(len(len(content) * content[0]) / len(lines))  # gets number of variables

        num_list = [[0 for x in range(n)] for y in range(2)]

        for i in range(n):
            num_list[0][i] = float(content[0][i])
            num_list[1][i] = float(content[1][i])

        print(n)
        create_arrays(n, num_list)



if __name__ == '__main__':

    main()

