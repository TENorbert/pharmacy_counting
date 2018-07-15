
#!/usr/bin/python

import os, sys, re

from helper import *


def main():
    """main function"""
    try:

        readfiles = command_line_parser()
        input_file = readfiles['input']
        output_file = readfiles['output']


        data = read_input_data(input_file)

        print_lines(data)

        #write_output_data(data, output_file)

        data_dict = get_data(input_file)
        for key in data_dict.keys():
            print(str(key) + " : " + str(data_dict[key]))



    except IOError:
        print('main cannot run!')






if __name__ == '__main__':

    main()
