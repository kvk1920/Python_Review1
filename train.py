import sys
import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        prog="Script for collecting statistics to generation new text.",
        description= '''This program collects statistic on the source texts.''',
        epilog= '''(c) March 2018, Kalmykov V.K.'''
    )
    parser.add_argument('--input-dir', help= "Path to source directory")
    parser.add_argument('--model', help= 'Path to result directory')
    parser.add_argument('-lc', help= 'Save texts in lowercase.')
    parser.add_argument('--length', help= 'Length of generation sequence.')
    return parser

cl_parser = create_parser()
cl_comands = cl_parser.parse_args()