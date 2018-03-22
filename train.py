import sys
import argparse
import os

def create_parser():
    """Create command line parser.

    Create parser what can process all arguments.
    """
    parser = argparse.ArgumentParser(
        prog="Script for collecting statistics to generation new text.",
        description= '''This program collects statistic on the source texts.''',
        epilog= '''(c) March 2018, Kalmykov V.K.'''
    )
    parser.add_argument('--input-dir', help= "Path to source directory")
    parser.add_argument('--model', help= 'Path to result directory')
    parser.add_argument('--lc', help= 'Save texts in lowercase.')
    parser.add_argument('--length', help= 'Length of generation sequence.')
    return parser


parser = create_parser()
commands = parser.parse_args()

def get_filelist(commands):
    filelist = list()
    filelist.append(sys.stdin)

    if commands.input_dir != None:
        filenames = os.listdir()
        filelist.clear()
        for filename in filenames:
            filelist.append(open(filename, "r"))
    return filelist

def process_line(line):
    '''Process one line.'''

    '''Remove non-alphabetic symbols(and transform to lowercase'''

filelist = get_filelist()

