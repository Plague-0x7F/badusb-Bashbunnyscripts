#!/usr/bin/env python3

import sys
import argparse

# Define the argument parser
parser = argparse.ArgumentParser(description="Script to process payloads for Bunny or Ducky devices")

# Add arguments
parser.add_argument('-f', '--file', type=argparse.FileType('r'), required=True, help='File to load')
parser.add_argument('-o', '--out', type=str, help='Output file')
parser.add_argument('-d', '--device', choices=['bunny', 'ducky'], required=True, help='Device type: bunny or ducky')

# Parse arguments
args = parser.parse_args()

# Read the payload from the input file
if args.file:
    with args.file as file:
        payload_lines = file.readlines()
else:
    print("No file loaded")
    sys.exit(1)

# Determine the output file name
outfile_name = args.out if args.out else 'output.txt'

n = 50

# Define the function for generating Bunny payloads
def GenBunny(payload_lines, outfile):
    for line in payload_lines:
        line = line.rstrip()  # Strip trailing whitespace
        if len(line) > n:
            for i in range(0, len(line), n):
                outfile.write("Q STRING " + line[i:i+n] + "\n")
                outfile.write("Q DELAY 200\n")
        else:
            outfile.write("Q STRING " + line + "\n")
            outfile.write("Q DELAY 200\n")

# Define the function for generating Ducky payloads
def GenDucky(payload_lines, outfile):
    for line in payload_lines:
        line = line.rstrip()  # Strip trailing whitespace
        if len(line) > n:
            for i in range(0, len(line), n):
                outfile.write("STRING " + line[i:i+n] + "\n")
                outfile.write("DELAY 200\n")
        else:
            outfile.write("STRING " + line + "\n")
            outfile.write("DELAY 200\n")

# Write to the output file
with open(outfile_name, 'w') as outfile:
    if args.device == 'bunny':
        GenBunny(payload_lines, outfile)
    elif args.device == 'ducky':
        GenDucky(payload_lines, outfile)

print(f"Output written to {outfile_name}")
