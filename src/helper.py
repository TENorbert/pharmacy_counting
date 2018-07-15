#!/user/bin/python

from argparse import ArgumentParser


def command_line_parser():
    """command line passing arguments"""
    ap = ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="inputfile:  itcont.txt")
    ap.add_argument("-o", "--output", required=True, help="output file: top_cost_drug.txt")
    #ap.add_argument('-i', '--input_file', nargs='?')
    #ap.add_argument('-o', '--output_file', nargs='?')
    #print(args); inputfile = args["input"]; outputfile = args["output"];
    return vars(ap.parse_args())


def get_data(filename):
    data = {}
    with open(filename, 'r') as fobj:
        next(fobj) # skip first line!
        lines = fobj.readlines()
        for line in lines:
            id, last_name, first_name, drug_name, drug_cost = line.strip().split(',')
            drug_properties = (last_name, first_name, drug_name, drug_cost)
            data[id] = list(drug_properties)
    return data





def read_input_data(input_filename):
    """Reads data from file into list"""
    data_list = []
    try:
        with open(input_filename, 'r') as fhandle:
            for lines in fhandle.readlines():
                lines = lines.strip().split(',')
                data_list = [line for line in lines]
        return data_list
    except Exception as e:
        print(type(e) + " Unable to read input file: {}".format(input_filename))


def write_output_data(list_data,output_filename):
    """prints data to output file"""
    try:
        with open(output_filename, 'w') as fhandle:
            for index in range(len(list_data)):
                if list_data[index] == '\n':
                    fhandle.write(str(list_data[index]))
                else:
                    if index < 4:
                        fhandle.write(str(list_data[index]) + ',')
                    else:
                        fhandle.write(str(list_data[index]) + '\n')
    except Exception:
        print("unable to write to file {}".format(output_filename))
        exit(0)



def print_lines(data_list):
    """reads and spit out items read"""
    try:
        for index in range(len(data_list)):
            if data_list[index] == '\n':
                print(str(data_list[index]))
            else:
                if index < 4:
                    print(str(data_list[index]) + ',')
                else:
                    print(str(data_list[index]) + '\n')
    except:
        if(len(data_list) == 0):
            print("Oops! data list empty")
            exit(0)
        else:
            print("Error: Reading Data list!")
            exit(0)
