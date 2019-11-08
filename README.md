# Canvas Grade Loader

## Background story
This program was written to help with my work as a TA for large undergraduate linguistics classes.
The scores of scantron exams are returned in a CSV file, and those scores had to be inputted into
the Canvas gradebook of the class, which is also a CSV file. However, the students in the two files are often not
 arranged the same way for reasons like students being absent from the exam or errors in specifying first and last
  names. So it's not a matter of copy and pasting a CSV column in a spreadsheet software.

This program inputs a file containing scores and loads them in a class' Canvas gradebook
by matching students based on their university IDs.

## How to use
The simplest way to use this program is to edit the parameter values in the default
parameter file, `parameters.txt`. The parameters required and their meanings can be found
therein. These include the names of the source and destination files. Parameter values are written after the
 ':' symbol in the lines therein. Then run the program in an IDE or a command line.

To use a different parameter file, you can run the program in a command line and specify the file
as an argument with the `-params` flag like so:

``python3 load_grades_to_canvas.py -params other.txt``

## Caveat
This program matches students in the two files by their student IDs. The motivation for this
is that ID numbers are less likely to be erred with. However, a score will not be loaded if
a student's ID in the source file does not match the one in the destination file.