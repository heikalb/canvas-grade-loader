"""
Add scores from scantron test results to a Canvas gradebook
"""

import csv


def main():
    # Data file names
    source_file_path = 'canvas.csv'
    target_file_path = '2019-06-27T1809_Grades-LING111_D100.csv'
    save_file_path = '2019-06-27T1809_Grades-LING111_D100_.csv'

    # Positions of variables of interest in data files
    source_index = 5
    target_index = 6
    source_id_index = 2
    target_id_index = 2

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