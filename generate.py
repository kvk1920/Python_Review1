import random
import argparse
import sys


def create_parser():
    """
    Create parser.

    Create parser that can take all command line arguments.
    :return parser: Created parser.
    """
    parser = argparse.ArgumentParser(prog="Text generator.",
                                     description="This program uses the model"
                                                 "of texts to generate it own"
                                                 "text.",
                                     epilog='''(c) March 2018, Kalmykov V.K.''')
    parser.add_argument("--model", nargs=1, help="Path to model file.",
                        type=str)
    parser.add_argument("--seed", nargs='?', help="Generation starts with this"
                                                "word", type=str)
    parser.add_argument("--length", nargs=1, help="Number of words in"
                                                  "generating text", type=int)
    parser.add_argument("--output", nargs="?", help="Name of file with result",
                        type=str)
    return parser


parser = create_parser()
commands = parser.parse_args()

output = sys.stdout

if commands.output:
    output = open(commands.output)

words = list()
model = dict()


def read_input():
    """
    Read model from file.

    Read model of text from file that created by train.py.
    """
    with open(str(*commands.model), "r") as istream:
        line = istream.readline().strip()
        while line:
            line = line.split()
            words.append(line[0])
            line = line[1:]
            model[words[-1]] = line
            line = istream.readline().strip()


def print_word(word):
    """
    Print word.

    Print word and choose the next word.
    :param word: Current word.
    :return: Next word.
    """
    if not word:
        word = random.choice(words)
    print(word, end=' ')
    if len(model[word]) == 0:
        word = None
    else:
        word = random.choice(model[word])
    return word;


read_input()
current_word = commands.seed

for i in range(int(*commands.length)):
    current_word = print_word(current_word)
print()