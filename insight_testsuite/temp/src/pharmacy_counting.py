
#!/usr/bin/python

import os, sys, re

from helper import command_line_parser, \
    get_data_lines,extract_drug_properties,\
    compute_drug_outputs,write_pharmacy_counting


def main():
    """main function"""
    try:

        readfiles = command_line_parser()
        input_file = readfiles['input']
        output_file = readfiles['output']

        unique_prescriber_names = {}  # unique prescriber of a drug type
        drug_costs = {}  # list of costs for each drug

        """
        #data = read_input_data(input_file)
        print_lines(data)
        #write_output_data(data, output_file)
        data_dict = get_data(input_file)
        for key in data_dict.keys():
            print(str(key) + " : " + str(data_dict[key]))
        """
        lines = get_data_lines(input_file)

        drug_name_list, drug_cost_list, drug_prescriber_list = extract_drug_properties(lines)

        print("drugs_name length = {}, costs_length= {}, prescriber_length = {}\n" \
              .format(len(drug_name_list), len(drug_cost_list), len(drug_prescriber_list)))

        compute_drug_outputs(drug_name_list, drug_cost_list,\
                             drug_prescriber_list,\
                             unique_prescriber_names, drug_costs)

        write_pharmacy_counting(drug_costs, unique_prescriber_names, output_file)

    except IOError:
        print('main cannot run!')






if __name__ == '__main__':

    main()
