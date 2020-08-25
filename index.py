import argparse
from validate import validate
from generate import generate

parser = argparse.ArgumentParser()

parser.add_argument("number", type=str, help="The binary number to be used")
parser.add_argument("functionality", choices=["generate", "validate"], type=str)

args = parser.parse_args()

if(args.functionality == 'validate'):
    validate(args.number)
else:
    print(f'Generated sequence: {generate(args.number)}')