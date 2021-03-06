import random
import argparse
import sys


def create_parser():
    """
    Create parser.

    Create parser that can take all command line arguments.
    Model
    File of model.
    Seed
    Test generate starts with this word.
    Length
    Size of generating sequence.
    Output
    Name of output file.
    :return parser: Created parser.
    """
    parser = argparse.ArgumentParser(prog="Text generator.",
                                     description="This program uses the model"
                                                 "of texts to generate it own"
                                                 "text.",
                                     epilog="(c) March 2018, Kalmykov V.K.")
    parser.add_argument("--model", help="Path to model file.",
                        type=str)
    parser.add_argument("--seed", help="Generation starts with this "
                                       "word", type=str)
    parser.add_argument("--length", help="Number of words in "
                                         "generating text", type=int)
    parser.add_argument("--output", help="Name of file with result",
                        type=str)
    return parser


def read_input(model_name):
    """
    Read model from file.

    Read model of text from file that created by train.py.
    :param model_name: Name of model file.
    :return: Read model.
    """
    model = dict()
    with open(model_name, "r") as istream:
        line = istream.readline().strip().split()
        while line:
            model[line[0]] = dict()
            for i in range(1, len(line), 2):
                model[line[0]][line[i]] = int(line[i + 1])
            line = istream.readline().strip().split()
    return model


def choose_next_word(word, model, generated_sequence):
    """
    Print word.

    Print word and choose the next word.
    :param word: Current word.
    :param model: Model of text.
    :param generated_sequence: List of generated words.
    :return: Next word.
    """
    if not word:
        word = random.choice(list(model.keys()))
    generated_sequence.append(word)
    if word not in model.keys() or not len(model[word]):
        return None
    else:
        word_list = list()
        for next_word, number in model[word].items():
            for k in range(number):
                word_list.append(next_word)
        return random.choice(word_list)


def print_output(word_list, output):
    for word in word_list:
        output.write(word, ' ')
    print()


def run(args):
    """
    Main function.

    Generate text.
    :param args: Command line arguments.
    :return: None
    """
    parser = create_parser()
    commands = parser.parse_args(args)
    output = sys.stdout
    if commands.output:
        output = open(commands.output)
    model = read_input(commands.model)
    current_word = None
    if commands.seed:
        current_word = commands.seed
        if current_word not in model.keys():
            raise ValueError("Start word isn't correct.")
    generated_sequence = list()
    for i in range(int(commands.length)):
        current_word = choose_next_word(current_word, model, generated_sequence)
    print_output(generated_sequence, output)


if __name__ == "__main__":
    run(sys.argv[1:])
