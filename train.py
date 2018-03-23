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
        description='''This program collects statistic on the source
        texts.''',
        epilog='''(c) March 2018, Kalmykov V.K.'''
    )
    parser.add_argument('--input-dir', help="Path to source directory",
                        type=str, nargs='?')
    parser.add_argument('--model', help='Path to result directory',
                        nargs=1,
                        type=str)
    parser.add_argument('--lc', help= 'Save texts in lowercase.')
    return parser


def get_filelist(commands):
    """
    Get list of source files.

    Get list of source files(according to command line arguments).
    :return filelist: List of source files.
    """
    filelist = list()
    filelist.append(sys.stdin)

    if commands.input_dir:
        filenames = os.listdir(commands.input_dir)
        filelist.clear()
        for filename in filenames:
            filelist.append(open(commands.input_dir + filename, "r"))
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
        elif good_line and good_line[-1] != ' ':
            good_line += ' '
    if commands.lc:
        good_line = good_line.lower()
    return list(good_line.split())


def write_model(model_to_write, result_file):
    """
    Write model.

    Write model to file.
    :param model_to_write: Model to write.
    """
    for first_word in model_to_write.keys():
        result_file.write(first_word + " " +
                          " ".join(model_to_write[first_word]) + "\n")


def add_pair(first_word, second_word, model):
    """
    Add pair of words.

    Add pair of connected words in model of text.
    :param first_word: First word.
    :param second_word: Second word.
    """
    if first_word not in model.keys():
        model[first_word] = list()
    model[first_word].append(second_word)


def run():
    """
    Run program.

    Main function that run all program.
    """
    parser = create_parser()
    commands = parser.parse_args()
    result_file = open(str(*commands.model), "w")
    list_of_files = get_filelist(commands)
    model = dict()
    for file in list_of_files:
        line = file.readline()
        prev_word = None
        while line != "":
            word_list = prepare_line(line)
            for word in word_list:
                if prev_word:
                    add_pair(prev_word, word, model)
                prev_word = word
            line = file.readline()
    write_model(model, result_file)


run()