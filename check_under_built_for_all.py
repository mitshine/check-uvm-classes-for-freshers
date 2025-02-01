# import OS module
import os

import re
import glob

class Format:
    end = '\033[0m'
    underline = '\033[4m'

# Get the list of all files and directories
path = "uvm_files"
#print(path)

print("\n")
print(Format.underline + "SEE DETAILS BELOW" + Format.end)
print("\n")
print(Format.underline + "INHERITED CLASSES" + Format.end)

a = ["uvm_test", "uvm_driver", "uvm_monitor", "uvm_agent", "uvm_sequencer", "uvm_subscriber", "uvm_sequence", "uvm_sequence_item", "uvm_env", "uvm_scoreboard", "uvm_analysis_port", "uvm_analysis_imp", "uvm_report_object", "uvm_report_handler", "uvm_report_server"]

#b = "extends "
#a = [b + direction for direction in a]

print("\nChecking for: ", a, " in uvm hierarchy files.\n")

existing_classes = []

#for i in dir_list:
for i in glob.glob(path + '/*.sv'):
    #print(i)
    # string to search in file
    with open(i, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
            for word in a:
               #print(word)
               #r = re.compile('|'.join([r'\b%s\b' % w for w in words]), flags=re.I)
               #print(row.find(word))
               # find() method returns -1 if the value is not found,
               # if found it returns index of the first occurrence of the substring
               if "extends" in row:
                   if row.find(word) != -1:
                       print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                       existing_classes.append(word)

print("\nFound these classes in the uvm hierachy: ", existing_classes)
print("\nNeed these classes to be defined in the uvm hierarchy: ", list(set(a) - set(existing_classes)), "\n")

print(Format.underline + "CONSTRAINTS" + Format.end)

a = ["constraint"]

print("\nChecking for: ", a, " in uvm hierarchy files.\n")

existing_classes = []

#for i in dir_list:
for i in glob.glob(path + '/*.sv'):
    #print(i)
    # string to search in file
    with open(i, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
            for word in a:
               #print(word)
               #r = re.compile('|'.join([r'\b%s\b' % w for w in words]), flags=re.I)
               #print(row.find(word))
               # find() method returns -1 if the value is not found,
               # if found it returns index of the first occurrence of the substring
               if row.find(word) != -1:
                   print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                   #existing_classes.append(row.strip("\n"))
                   print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

#print("\nFound these constraints in the uvm hierachy: ", existing_classes)
#print("\nNeed these classes to be defined in the uvm hierarchy: ", list(set(a) - set(existing_classes)))

print((Format.underline + "RANDOMIZATIONS" + Format.end).rstrip())

a = ["randomize"]

print("\nChecking for: ", a, " in uvm hierarchy files.\n")

existing_classes = []

#for i in dir_list:
for i in glob.glob(path + '/*.sv'):
    #print(i)
    # string to search in file
    with open(i, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
            for word in a:
               #print(word)
               #r = re.compile('|'.join([r'\b%s\b' % w for w in words]), flags=re.I)
               #print(row.find(word))
               # find() method returns -1 if the value is not found,
               # if found it returns index of the first occurrence of the substring
               if row.find(word) != -1:
                   print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                   #existing_classes.append(row.strip("\n"))
                   print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

#print("\nFound these randomizations in the uvm hierachy: ", existing_classes)
#print("\nNeed these classes to be defined in the uvm hierarchy: ", list(set(a) - set(existing_classes)))

print(Format.underline + "FACTORY METHODS" + Format.end)

a = ["uvm_component_utils", "uvm_object_utils"]

print("\nChecking for: ", a, " in uvm hierarchy files.\n")

existing_classes = []

#for i in dir_list:
for i in glob.glob(path + '/*.sv'):
    #print(i)
    # string to search in file
    with open(i, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
            for word in a:
               #print(word)
               #r = re.compile('|'.join([r'\b%s\b' % w for w in words]), flags=re.I)
               #print(row.find(word))
               # find() method returns -1 if the value is not found,
               # if found it returns index of the first occurrence of the substring
               if row.find(word) != -1:
                   print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                   #existing_classes.append(row.strip("\n"))
                   print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

#print("\nNeed these classes to be defined in the uvm hierarchy: ", list(set(a) - set(existing_classes)))

print(Format.underline + "FUNCTIONS AND CREATE_METHODS" + Format.end)

a = ["virtual", "new", "type_id", "uvm_config_db", "p_sequencer", "m_sequencer", "start_item", "finish_item", "raise_objection", "drop_objection", "task"]

print("\nChecking for: ", a, " in uvm hierarchy files.\n")

existing_classes = []

#for i in dir_list:
for i in glob.glob(path + '/*.sv'):
    #print(i)
    # string to search in file
    with open(i, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
            for word in a:
               #print(word)
               #r = re.compile('|'.join([r'\b%s\b' % w for w in words]), flags=re.I)
               #print(row.find(word))
               # find() method returns -1 if the value is not found,
               # if found it returns index of the first occurrence of the substring
               if row.find(word) != -1:
                   print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                   #existing_classes.append(row.strip("\n"))
                   print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

print(Format.underline + "FUNCTIONS AND CREATE_METHODS" + Format.end)

a = ["build", "connect", "end_of_elaboration", "start_of_simulation", "run", "extract", "check", "report", "final"]

print("\nChecking for: ", a, " in uvm hierarchy files.\n")

existing_classes = []
existing_phases = []

#for i in dir_list:
for i in glob.glob(path + '/*.sv'):
    #print(i)
    # string to search in file
    with open(i, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
            for word in a:
               #print(word)
               #r = re.compile('|'.join([r'\b%s\b' % w for w in words]), flags=re.I)
               #print(row.find(word))
               # find() method returns -1 if the value is not found,
               # if found it returns index of the first occurrence of the substring
               if not "super" in row:
                   if row.find(word) != -1:
                       print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                       existing_phases.append(row.strip("\n"))
                       print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

print("Need these phases to be defined in the uvm hierarchy: ", list(set(a) - set(existing_phases)), "\n")

print(Format.underline + "SUPER METHODS" + Format.end)

a = ["super"]

print("\nChecking for: ", a, " in uvm hierarchy files.\n")

existing_classes = []
existing_phases = []

#for i in dir_list:
for i in glob.glob(path + '/*.sv'):
    #print(i)
    # string to search in file
    with open(i, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
            for word in a:
               #print(word)
               #r = re.compile('|'.join([r'\b%s\b' % w for w in words]), flags=re.I)
               #print(row.find(word))
               # find() method returns -1 if the value is not found,
               # if found it returns index of the first occurrence of the substring
               if row.find(word) != -1:
                   print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                   existing_phases.append(row.strip("\n"))
                   print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

print(Format.underline + "RANDOM VARIABLES IN UVM_SEQUENCE_ITEM" + Format.end)

a = ["rand"]

print("\nChecking for: ", a, " in uvm hierarchy files.\n")

existing_classes = []
existing_phases = []

#for i in dir_list:
for i in glob.glob(path + '/*.sv'):
    #print(i)
    # string to search in file
    with open(i, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
            for word in a:
               #print(word)
               #r = re.compile('|'.join([r'\b%s\b' % w for w in words]), flags=re.I)
               #print(row.find(word))
               # find() method returns -1 if the value is not found,
               # if found it returns index of the first occurrence of the substring
               if not "randomize" in row:
                   if row.find(word) != -1:
                       print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                       existing_phases.append(row.strip("\n"))
                       print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

#OUTPUT:
#
#
#SEE DETAILS BELOW
#
#
#INHERITED CLASSES
#
#Checking for:  ['uvm_test', 'uvm_driver', 'uvm_monitor', 'uvm_agent', 'uvm_sequencer', 'uvm_subscriber', 'uvm_sequence', 'uvm_sequence_item', 'uvm_env', 'uvm_scoreboard', 'uvm_analysis_port', 'uvm_analysis_imp', 'uvm_report_object', 'uvm_report_handler', 'uvm_report_server']  in uvm hierarchy files.
#
#"uvm_sequence"  exists in the file:  "uvm_files\constraints.sv"  in line number:  2
#"uvm_sequence_item"  exists in the file:  "uvm_files\constraints.sv"  in line number:  2
#"uvm_driver"  exists in the file:  "uvm_files\driver1.sv"  in line number:  2
#"uvm_test"  exists in the file:  "uvm_files\test1.sv"  in line number:  3
#
#Found these classes in the uvm hierachy:  ['uvm_sequence', 'uvm_sequence_item', 'uvm_driver', 'uvm_test']
#
#Need these classes to be defined in the uvm hierarchy:  ['uvm_sequencer', 'uvm_report_server', 'uvm_monitor', 'uvm_report_handler', 'uvm_agent', 'uvm_report_object', 'uvm_analysis_port', 'uvm_analysis_imp', 'uvm_subscriber', 'uvm_scoreboard', 'uvm_env']
#
#CONSTRAINTS
#
#Checking for:  ['constraint']  in uvm hierarchy files.
#
#"constraint"  exists in the file:  "uvm_files\constraints.sv"  in line number:  6
#Found:  "constraint addr {addr > 0; addr < 10};"
#
#"constraint"  exists in the file:  "uvm_files\constraints.sv"  in line number:  8
#Found:  "soft constraint data {data inside [0:100]};"
#
#RANDOMIZATIONS
#
#Checking for:  ['randomize']  in uvm hierarchy files.
#
#"randomize"  exists in the file:  "uvm_files\constraints.sv"  in line number:  10
#Found:  "assert.randomize(txn1);"
#
#"randomize"  exists in the file:  "uvm_files\packet.sv"  in line number:  11
#Found:  "pkt.randomize() with { addr == 8;};"
#
#FACTORY METHODS
#
#Checking for:  ['uvm_component_utils', 'uvm_object_utils']  in uvm hierarchy files.
#
#"uvm_component_utils"  exists in the file:  "uvm_files\constraints.sv"  in line number:  4
#Found:  "`uvm_component_utils(txn1)"
#
#FUNCTIONS AND CREATE_METHODS
#
#Checking for:  ['virtual', 'new', 'type_id', 'uvm_config_db', 'p_sequencer', 'm_sequencer', 'start_item', 'finish_item', 'raise_objection', 'drop_objection', 'task']  in uvm hierarchy files.
#
#"virtual"  exists in the file:  "uvm_files\driver1.sv"  in line number:  6
#Found:  "virtual function run_phase()"
#
#"virtual"  exists in the file:  "uvm_files\driver1.sv"  in line number:  10
#Found:  "virtual function void build_phase(uvm_phase phase);"
#
#"type_id"  exists in the file:  "uvm_files\driver1.sv"  in line number:  12
#Found:  "s0 = uvm_sequencer#(Item)::type_id::create("s0", this);"
#
#"m_sequencer"  exists in the file:  "uvm_files\driver1.sv"  in line number:  12
#Found:  "s0 = uvm_sequencer#(Item)::type_id::create("s0", this);"
#
#"new"  exists in the file:  "uvm_files\packet.sv"  in line number:  8
#Found:  "pkt = new();"
#
#FUNCTIONS AND CREATE_METHODS
#
#Checking for:  ['build', 'connect', 'end_of_elaboration', 'start_of_simulation', 'run', 'extract', 'check', 'report', 'final']  in uvm hierarchy files.
#
#"run"  exists in the file:  "uvm_files\driver1.sv"  in line number:  6
#Found:  "virtual function run_phase()"
#
#"build"  exists in the file:  "uvm_files\driver1.sv"  in line number:  10
#Found:  "virtual function void build_phase(uvm_phase phase);"
#
#Need these phases to be defined in the uvm hierarchy:  ['build', 'run', 'end_of_elaboration', 'connect', 'extract', 'start_of_simulation', 'check', 'report', 'final']
#
#SUPER METHODS
#
#Checking for:  ['super']  in uvm hierarchy files.
#
#"super"  exists in the file:  "uvm_files\driver1.sv"  in line number:  11
#Found:  "super.build_phase(phase);"
#
#RANDOM VARIABLES IN UVM_SEQUENCE_ITEM
#
#Checking for:  ['rand']  in uvm hierarchy files.
#
#"rand"  exists in the file:  "uvm_files\driver1.sv"  in line number:  4
#Found:  "rand bit  in;"
#
#"rand"  exists in the file:  "uvm_files\packet.sv"  in line number:  2
#Found:  "rand bit [3:0] addr;"
#
#