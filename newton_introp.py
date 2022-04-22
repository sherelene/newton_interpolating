import random
import numpy as np
from decimal import *
import time
import sys, getopt
import argparse
from argparse import ArgumentParser
import os


def coeff(xs, ys, n, z, ex):
    ex3_n = 'k'
    cs = np.zeros(n + 1, dtype=np.dtype(Decimal))
    for i in range(n + 1):
        cs[i] = ys[i]

    try:
        tic = time.perf_counter()
        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                cs[i] = (cs[i] - cs[i - 1]) / (xs[i] - xs[i - j])
        toc = time.perf_counter()
    except ZeroDivisionError:
        print("Program ran through a division by zero and could not be avoided")
    else:
        if ex == 4:
            inter_time = toc - tic
        elif ex == 3:
            inter_time = toc - tic
            ex3_n = 3
        else:
            inter_time = 'k'
        eval_newton(xs, cs, n, z, ex, inter_time, ex3_n)


def eval_newton(xs, cs, num, z, ex, interp_time, ex3_n):
    tic = time.perf_counter()
    result = cs[num]
    for i in range(num - 1, -1, -1):
        result = result * (z - xs[i]) + cs[i]
    toc = time.perf_counter()
    if ex == 4:
        eval_time = toc - tic
    elif ex == 3:
        eval_time = toc - tic
        ex3_n = 3
    else:
        inter_time = 'k'
    print_to_file(result, interp_time, eval_time, ex, num, ex3_n)


def print_to_file(solution, interpo_time, evalu_time, ex, n, ex3_n):
    input_filename = args.filename
    if ex3_n == 3:
        output_filename = str(n) + ".pnt"
    else:
        output_filename = os.path.splitext(input_filename)[0] + ".pnt"

    with open(output_filename, "w") as external_file:
        print(solution, file=external_file)
        if ex == 4 or ex3_n == 3:
            print('Duration of evaluation in seconds: {}'.format(interpo_time), file=external_file)
            print('Duration of evaluation in seconds: {}'.format(evalu_time), file=external_file)
        external_file.close()
        print("\nThis solution has been placed in an output file named {}".format(output_filename))

def clean_file_data(num_of_variables, file_list):
    ex = 4
    # initialize new array to store the solved coefficients
    x = np.zeros(num_of_variables + 1, dtype=np.dtype(Decimal))
    y = np.zeros(num_of_variables + 1, dtype=np.dtype(Decimal))

    for j in range(num_of_variables):
        x[j] = file_list[0][j]
        y[j] = file_list[1][j]

    z = 0
    user_input = input("Please enter a value to evaluate: ")
    try:
        if user_input == 'q':
            exit()
        z = float(user_input)
    except ValueError:
        print("Error, should have been a number or 'q'")
        exit()

    coeff(x, y, num_of_variables, z, ex)


def create_data_points(n):
    ex = 3
    x = []
    y = []

    for it in range(n + 1):
        x.append(round(random.uniform(0.1, 1000), 2))
        y.append(round(random.uniform(0.1, 1000), 2))
    z = random.randint(1, n - 1)
    print("n =", n)

    coeff(x, y, n, z, ex)

def exercise3():
    exercise = [10, 100, 1000]
    for i in exercise:
        create_data_points(i)

def check_argument(args):
    try:
        int(args.filename)
        return int(args.filename)
    except ValueError:
        return -1


def main(args):
    filename = check_argument(args)
    if args.ex3:
        exercise3()
    elif filename == -1:
        with open(args.filename) as file:
            # declare array we're going to get from the file
            content = []

            # reads the rest of the lines within the file
            lines = file.readlines()

            cnt = 0
            row = 2
            # takes each line read from file and inputs each number in the line into an element into the file content array
            for line in lines:
                content.append(line.split())  # split ignores all unnecessary characters like \n or whitespace

            n = int(len(len(content) * content[0]) / len(lines))  # gets number of variables

            num_list = [[0 for x in range(n)] for y in range(2)]

            for i in range(n):
                num_list[0][i] = float(content[0][i])
                num_list[1][i] = float(content[1][i])

            clean_file_data(n, num_list)

    else:
        create_data_points(filename)


if __name__ == '__main__':
    # start of getting arguments from command line
    parser = argparse.ArgumentParser(
        description='newton interpolation '
                    'an optional flag written as: python3 gaussian <optional-flag> '
                    '<int>')
    parser.add_argument('-n', '--n', type=int, help="creates random data points of size input int",
                        required=False)
    parser.add_argument('-ex3', '--ex3', action="store_true", help="calls function do do exercise 3 of homework",
                        required=False)
    parser.add_argument("filename", help="stores filename")

    args = parser.parse_args()  # stores all the arguments int the commandline

    main(args)
