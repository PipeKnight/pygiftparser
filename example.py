import argparse
from pygiftparser import parser


def parse_input_arguments():
    parser = argparse.ArgumentParser(description='GIFT Moodle file parser.')
    parser.add_argument('-f', '--file', dest='file', required=True,
                        help='GIFT Moodle file.')
    return parser.parse_args()


args = parse_input_arguments()
with open(args.file, 'r') as myfile:
    s = myfile.read()
    result = parser.parse(s)
    for q in result.questions:
        print(q)
