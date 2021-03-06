import sys
import argparse
import os
import collections


def create_parser():
    """Create command line parser.

    Create parser what can process all arguments.
    Input directory
    It's path to input directory, the files in this directory
    will be used for making model.
    Model file name
    It's name of model file, in this file will been writen the model.
    Convert to lowercase
    If user wants to convert all words to lowercase.
    :return parser: Parser with parameters.
    """
    parser = argparse.ArgumentParser(
        prog="Script for collecting statistics to generation new text.",
        description='''This program collects statistic on the source
        texts.''',
        epilog='''(c) March 2018, Kalmykov V.K.'''
    )
    parser.add_argument('--input-dir', help="Path to source directory",
                        type=str)
    parser.add_argument('--model', help='Path to result directory',
                        type=str)
    parser.add_argument('--lc', action='store_true',
                        help='Save texts in lowercase.')
    return parser


def get_filelist(input_directory):
    """
    Get list of source files.

    Get list of source files(according to command line arguments).
    If there isn't input directory, filelist will contain only stdin.
    In another case filelist will contain all open files from filenames.
    :param input_directory: Input directory.
    :return filelist: List of source files.
    """
    filelist = list()
    filelist.append(sys.stdin)
    if input_directory:
        filenames = os.listdir(input_directory)
        filelist.clear()
        for filename in filenames:
            filelist.append(open(input_directory + filename, "r"))
    return filelist


def prepare_line(line, is_lower):
    """
    Prepare one line for appending into model.

    This function takes all words from line.
    :param line: Line of source text.
    :param commands: Command line arguments.
    :return: List of words in this line.
    """
    good_line = \
        ''.join(list(map(lambda c: c if c.isalpha() else ' ', line))).split()
    if is_lower:
        good_line = good_line.lower()
    return list(good_line.split())


def write_model(model, result_file):
    """
    Write model.

    Write model to file in this format:
    In one line first word is the first word of pair, and then there is list of
    word-number_of_this_word.
    :param model: Model to write.
    :param result_file: Output file(ot stdout).
    :return: None.
    """
    for first_word in model.keys():
        line = first_word
        for word, counter in model[first_word].items():
            line += ' ' + word + ' ' + str(counter)
        result_file.write(line + '\n')


def add_pair(first_word, second_word, model):
    """
    Add pair of words.

    Add pair of connected words in model of text.
    :param first_word: First word.
    :param second_word: Second word.
    :param model: Model of text.
    """
    model.setdefault(first_word, collections.Counter())
    model[first_word][second_word] += 1


def run(args):
    """
    Run program.

    Main function that run all program.
    1. Creating parser of command line arguments.
    2. Reading list of files.
    3. Reading all files.
    4. Writing model to file.
    :param args: Command line arguments.
    """
    parser = create_parser()
    commands = parser.parse_args(args)
    result_file = open(commands.model, "w")
    list_of_files = get_filelist(commands.input_dir)
    model = dict()
    for file in list_of_files:
        line = file.readline()
        prev_word = None
        while line != "":
            word_list = prepare_line(line, commands.lc)
            for word in word_list:
                if prev_word:
                    add_pair(prev_word, word, model)
                prev_word = word
            line = file.readline()
        file.close()
    write_model(model, result_file)


if __name__ == "__main__":
    run(sys.argv[1:])
