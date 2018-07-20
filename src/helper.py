#!/user/bin/python

from argparse import ArgumentParser
import os, sys, re

def command_line_parser():
    """command line passing arguments"""
    ap = ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="inputfile:  itcont.txt")
    ap.add_argument("-o", "--output", required=True, help="output file: top_cost_drug.txt")
    #print(args); inputfile = args["input"]; outputfile = args["output"];
    return vars(ap.parse_args())



def get_data_lines(input_filename):
    """
    reads a single line from file avoiding loading all lines at once!
    :param filename:
    :return:
    """
    try:
        with open(input_filename, 'r') as fobj:
            next(fobj)  #skip title line!
            lines = fobj.readlines()
        return lines
    except FileNotFoundError:
        print("Err! File with name = {}, Not Found!".format(input_filename))
        exit(0)


def extract_drug_properties(lines):
    """
    Extract drug data from lines read
    :param lines:
    :return:
    """
    try:
        drug_name_list = []
        drug_cost_list = []
        drug_prescriber_list = []
        drug_id_list = []  # Unique drug id
        for line in lines:
            line = line.strip().split(',')
            if len(line) == 5:
                drug_id = line[0]
                prescriber_name = line[1] + " " + line[2]
                drug_name = line[3]
                drug_cost = line[4]
                #get interested drug properties
                drug_id_list.append(drug_id)
                drug_name_list.append(drug_name)
                drug_cost_list.append(drug_cost)
                drug_prescriber_list.append(prescriber_name)

        return drug_name_list, drug_cost_list, drug_prescriber_list
    except Exception as e:
        print(e, type(e))


def compute_drug_outputs(drug_name_list, drug_cost_list, drug_prescriber_list,unique_prescriber_names, drug_costs):
    """
        Computes drug properties(Total cost, Number of Prescribers) using set and list DS:
    :param drug_name_list:
    :param drug_cost_list:
    :param drug_prescriber_list:
    :param unique_prescriber_name:
    :param drug_costs:
    :return: Drug Name, Number of Prescribers, Total cost
    """
    '''
    ## Get list of unique Prescriber for each drug
    for item in drug_name_list:
        print('Drug Name = %s' %item)
    for item in drug_prescriber_list:
        print('Drug Prescriber = %s' %item)
    for item in drug_cost_list:
        print('Drug Cost = %s' %item)
    '''
    try:
        for drug, prescriber in zip(drug_name_list, drug_prescriber_list):
            #print('Drug = %s & Drug Prescriber = %s' % (drug, prescriber))
            if drug not in unique_prescriber_names:
                unique_prescriber_names[drug] = set() # unique prescriber name
            unique_prescriber_names[drug].add(prescriber)

        for drug, cost in zip(drug_name_list, drug_cost_list):
            #print('Drug = %s & Drug Cost = %s' % (drug,cost))
            if drug not in drug_costs:
                drug_costs[drug] = list() #multiple costs!
            drug_costs[drug].append(cost)
    except Exception as e:
        print(e, type(e))



def drug_counting(drug_costs, unique_drug_prescribers, drug_list, output_file):
    """
        Takes drug_costs and uniqiue_drug_prescribers and computes:
            -- Total drugs
            -- Number of Unique Prescribers
            -- Total cost of drug
            -- Sort dictionary and write output to file
    :param drug_costs:
    :param unique_drug_prescribers:
    :param pharmacy_dict:
    :param output_file:
    :return:
    """
    drugs_from_drug_costs = [key for key in drug_costs.keys()]
    drugs_from_unique_drug_prescribers = [key for key in unique_drug_prescribers.keys()]
    '''
    print("length of drug cost = {} & length of unique prescribers = {}\n"\
        .format(len(drugs_from_drug_costs),len(drugs_from_unique_drug_prescribers)))
    print("-----Drug Costs-----")
    for key, value in drug_costs.items():
        print("Key = {}, Value = {}".format(key, value))
    print("\n")
    print("-----Drug Prescribers------")
    for key, value in unique_drug_prescribers.items():
        print("Key = {}, Value = {}".format(key, value))
    print("\n")
    '''
    try:
        if len(drugs_from_drug_costs) == len(drugs_from_unique_drug_prescribers):
            for drug in drug_costs.keys():
                if drug in unique_drug_prescribers.keys():
                    total_drug_cost = get_sum(drug_costs[drug])
                    total_drug_cost = int(total_drug_cost)
                    prescriber_count = len(unique_drug_prescribers[drug])
                    drug_list.append(Drug(drug,prescriber_count,total_drug_cost))
        else:
            print("Alora! Houston! Siamo Problema! Unequal drugs keys length on cost and prescribers dicts!")
        write_output(output_file, sort_pharmacy_drugs(drug_list))
    except Exception as e:
        print(e, type(e))
        exit(0)



def sort_pharmacy_drugs(drug_list):
    """
     Sort dictionary  by value in Descending order!
     if values are the same then sort by key(TO DO)
    :param drug_list:
    :return: sorted list
    """
    '''
       Do some optimization by not returning an entire list!
       might wanna call sort instead?
    '''
    return sorted(drug_list, key=lambda drug: drug.compare(), reverse=True)




def  get_sum(cost_list):
    """
    sums up items in a list
    :param cost_list:
    :return: sum_total
    """
    total_cost = 0.0
    try:
        for cost in cost_list:
            total_cost += float(cost)
        return total_cost
    except Exception as e:
        print(e, type(e))



def write_output(output_filename, sorted_drug_list):
    """
     writes sorted drug list to output file
    :param sorted_drug_list:
    :param output_filename:
    :return:
    """
    try:
        '''
        for drug in sorted_drug_list:
            #print(drug)
            #print(value[0] + "," + str(value[1][1]) + "," + str(value[1][0]) + "\n")
            print(drug.drug_name + "," + str(drug.drug_count) + "," + str(drug.drug_cost) + "\n")
        '''
        fhandle = open(output_filename, 'w')
        fhandle.write("drug_name,num_prescriber,total_cost\n")
        for drug in sorted_drug_list:
            fhandle.write(drug.drug_name + "," + str(drug.drug_count) + "," + str(drug.drug_cost) + "\n")
        fhandle.close()
    except FileExistsError:
        print("Err! Unable to write to file {}".format(output_filename))
        exit(0)



class Drug(object):
    """
     Drug Blueprint
    """
    def __init__(self,name,count,cost):
        self.drug_name = name
        self.drug_count = count
        self.drug_cost = cost

    def __repr__(self):
        return repr((self.drug_name, self.drug_count, self.drug_cost))

    def __lt__(self,other):
        if self.drug_cost < other.drug_cost:
            return True
        elif self.drug_cost == other.drug_cost:
            if self.drug_name < other.drug_name:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.drug_cost > other.drug_cost:
            return True
        elif self.drug_cost == other.drug_cost:
            if self.drug_name > other.drug_name:
                return True
            else:
                return False
        else:
            return False

    def compare(self):
        """
         Compare two Drugs in sorted list algorithm
        :return:
        """
        return self.drug_cost, self.drug_name


#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
def get_data(filename):
    """
     reads drugs data from file and returns dict with drug_id as key
     and the rest items as list of tuples.
    :param filename:
    :return: drug data as dict
    """
    data = {}
    try:
        with open(filename, 'r') as fobj:
            next(fobj)  #skip first line!
            lines = fobj.readlines()
            for line in lines:
                id, last_name, first_name, drug_name, drug_cost = line.strip().split(',')
                drug_properties = (last_name, first_name, drug_name, drug_cost)
                data[id] = list(drug_properties)
        return data
    except Exception:
        print("Err! Unable to write to file {}".format(filename))
        exit(0)



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
