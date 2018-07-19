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

    except Exception:
        print("Err! Unable to write to file {}".format(input_filename))
        exit(0)


def extract_drug_properties(lines):

    """
        extract drug data from lines read
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



        ## Get list of drug cost for each drug
        for drug, cost in zip(drug_name_list, drug_cost_list):
            #print('Drug = %s & Drug Cost = %s' % (drug,cost))
            if drug not in drug_costs:
                drug_costs[drug] = list() # multiple costs!
            drug_costs[drug].append(cost)

    except Exception as e:
        print(e, type(e))



def write_pharmacy_counting(drug_costs, unique_drug_prescribers,output_file):
    """
        Takes drug_costs and uniqiue_drug_prescribers and computes:
            -- Total drugs
            -- Number of Unique Prescribers
            -- Total cost of drug
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
    #TO DO:
    # -- Write output in DESCENDING drug PRICE
    # -- If Same Price, in alphabet order of drug name!

    try:
        fhandle = open(output_file, 'w')
        fhandle.write("drug_name,num_prescriber,total_cost \n")

        if len(drugs_from_drug_costs) == len(drugs_from_unique_drug_prescribers):
            drug_keylist = drug_costs.keys()
            #drug_keylist.sort() # sort by drug name alphabet!
            for drug in drug_keylist:
                if drug in unique_drug_prescribers.keys():
                    total_drug_cost = get_sum(drug_costs[drug])
                    total_drug_cost = int(total_drug_cost)
                    prescriber_count = len(unique_drug_prescribers[drug])

                    fhandle.write(drug + "," + str(prescriber_count) + "," + str(total_drug_cost) + "\n")
                    #write_output(output_file, drug,prescriber_count,total_drug_cost)
                    #print("Drug Name = {}, Total Cost = {} , Number of Unique Prescribers = {}"\
                    #      .format(drug, total_drug_cost, prescriber_count))
        else:
            print("Alora! Houston! Siamo Problema! Not same number of drugs on cost and prescribers dicts!")
        fhandle.close()

    except Exception:
        print("Err! Unable to write to file {}".format(output_file))
        exit(0)


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

def write_output(output_filename, *parameters):
    """
     writes data to output file

    :param parameters:
    :param output_filename:
    :return:
    """
    data_list = list(parameters)
    try:
        fhandle = open(output_filename, 'w')
        for index in range(len(data_list)):
            if data_list[index] == '\n':
                fhandle.write(str(data_list[index]))
            else:
                if index < 3:
                    fhandle.write(str(data_list[index]) + ',')
                else:
                    fhandle.write(str(data_list[index]) + '\n')

        fhandle.close()
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
