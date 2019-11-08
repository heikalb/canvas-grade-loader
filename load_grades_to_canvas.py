"""
Load scores from scantron test results to a Canvas gradebook.
Heikal Badrulhisham, 2018 <heikal93@gmail.com>
"""
import argparse
import csv


def load_parameters(file_path):
    """
    Get parameters from parameter file
    :param file_path:
    :return: dictionary of parameters
    """
    # Read parameter file
    with open(file_path, 'r') as f:
        file_lines = f.read().split('\n')
        input_lines = [l for l in file_lines if l and l[0] != '#']

    # Build parameter dictionary
    parameter_names = [l.split(':')[0].strip() for l in input_lines]
    parameter_values = [l.split(':')[1].strip() for l in input_lines]
    parameters = dict(zip(parameter_names, parameter_values))

    # Type cast numerical parameters
    parameters['source_id_index'] = int(parameters['source_id_index'])
    parameters['target_id_index'] = int(parameters['target_id_index'])
    parameters['source_index'] = int(parameters['source_index'])
    parameters['target_index'] = int(parameters['target_index'])

    return parameters


def main():
    # Get user specified parameter file
    parser = argparse.ArgumentParser(description='Load scores from scantron test results to a Canvas gradebook.')
    parser.add_argument('-params', default='parameters.txt', help='.txt file containing task parameters')
    args = parser.parse_args()

    # Inputted parameters for current grade loading
    parameters = load_parameters(args.params)

    # Data file names
    source_file_path = parameters['source_file_path']
    target_file_path = parameters['target_file_path']
    save_file_path = parameters['save_file_path']

    # Positions of variables of interest in data files
    source_id_index = parameters['source_id_index']
    target_id_index = parameters['target_id_index']
    source_index = parameters['source_index']
    target_index = parameters['target_index']

    # Source file reader
    source_file_reader = csv.reader(open(source_file_path, 'r'))
    temp_target = list(csv.reader(open(target_file_path, 'r')))

    # Add scores to students with matching IDs
    for row in source_file_reader:
        score = row[source_index]
        print(row)

        for row_ in temp_target:
            if row[source_id_index] == row_[target_id_index]:
                row_[target_index] = score
                break

    # Save data
    with open(save_file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(temp_target)


if __name__ == '__main__':
    main()
    exit(0)
