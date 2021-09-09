#!/usr/bin/env python3

import argparse, os
import qrcode.console_scripts as qr

# Change to script directory:
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

filename = f'{current_path}/authenticator.txt'

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="path to Google Authenticator exported text file")
args = parser.parse_args()
if not args.file == None:
    filename = args.file

# get lines from file into list:
with open(filename, 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

# generate qr codes from each line in lines list:
number_of_codes = len(lines)
current_number = 0
for line in lines:
    current_number += 1
    print('-------------------------------------------------------------------')
    print(f'QR CODE [{current_number} of {number_of_codes}]:')
    print(line)
    qr.main(args=[line])
    if current_number != number_of_codes:
        input('Press Enter to continue...')
