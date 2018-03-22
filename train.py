import sys
import argparse
import os

def create_parser():
    """Create command line parser.

    Create parser what can process all arguments.
    :return parser: Parser with parameters.
    """
    parser = argparse.ArgumentParser(
        prog="Script for collecting statistics to generation new text.",
        description= '''This program collects statistic on the source texts.''',
        epilog= '''(c) March 2018, Kalmykov V.K.'''
    )
    parser.add_argument('--input-dir', help= "Path to source directory", nargs= '?')
    parser.add_argument('--model', help= 'Path to result directory', nargs= 1)
    parser.add_argument('--lc', help= 'Save texts in lowercase.', nargs= '?')
    return parser


parser = create_parser()
commands = parser.parse_args()

sys.stdout = commands.model

def get_filelist():
    """
    Get list of source files.

    Get list of source files(according to command line arguments).
    :return filelist: List of source files.
    """
    filelist = list()
    filelist.append(sys.stdin)

    if commands.input_dir != None:
        filenames = os.listdir()
        filelist.clear()
        for filename in filenames:
            filelist.append(open(filename, "r"))
    return filelist

def prepare_line(line):
    """
    Prepare one line.

    Prepare one line for processing.
    :param line: Line of source text
    :return: List of words in this line.
    """
    good_line = str("")

    for char in line:
        if char.isalpha():
            good_line += char
        else:
            good_line += ' '

    return list(good_line.split())

def write_model(model_to_write):
    """
    Write model.

    Write model to file.
    :param model_to_write: Model to write.
    """
    for first_word in model_to_write.keys():
        print(first_word, *model_to_write[first_word])

list_of_files = get_filelist()  # This list includes only stdin if user wants read from stdin
model = dict()                  # Here's a model of input text.

def add_pair(first_word, second_word):
    """
    Add pair of words.

    Add pair of connected words in model of text.
    :param first_word: First word.
    :param second_word: Second word.
    """
    if first_word in model.keys():
        model[first_word].append(second_word)
    else:
        model[first_word] = list(second_word)

for file in list_of_files:
    line = file.readline()
    prev_word = None
    while not line == "":
        word_list = prepare_line(line)
        for word in word_list:
            if prev_word != None:
                add_pair(prev_word, word)
            prev_word = word

write_model(model)