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

print(Format.underline + "FUNCTIONS AND TASKS TYPE" + Format.end)

#a = ["virtual", "task"]
a = ["function", "task"]

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
               #print(word)
               if word in row.split(" "):
                   #if row.find(word) != -1:
                   print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                   #existing_classes.append(row.strip("\n"))
                   print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

print(Format.underline + "FUNCTIONS AND CREATE_METHODS" + Format.end)

a = ["new", "build", "connect", "end_of_elaboration", "start_of_simulation", "run", "extract", "check", "report", "final"]

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
                   if "function" in row:
                       if row.find(word) != -1:
                           print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                           existing_phases.append(row.strip("\n"))
                           print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

print("Need these phases to be defined in the uvm hierarchy: ", list(set(a) - set(existing_phases)), "\n")

print(Format.underline + "INITIATION OF TESTCASES" + Format.end)

a = ["start_item", "finish_item", "raise_objection", "drop_objection"]

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

print(Format.underline + "CREATE METHODS" + Format.end)

a = ["type_id", "uvm_config_db"]

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

print(Format.underline + "USAGE OF p_sequencer AND m_sequencer" + Format.end)

a = ["p_sequencer", "m_sequencer"]

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
               if word in row.split(" "):
                   #if row.find(word) != -1:
                   print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                   existing_phases.append(row.strip("\n"))
                   print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

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
#Need these classes to be defined in the uvm hierarchy:  ['uvm_scoreboard', 'uvm_sequencer', 'uvm_subscriber', 'uvm_env', 'uvm_report_server', 'uvm_monitor', 'uvm_agent', 'uvm_analysis_imp', 'uvm_report_object', 'uvm_analysis_port', 'uvm_report_handler']
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
#"randomize"  exists in the file:  "uvm_files\driver1.sv"  in line number:  16
#Found:  "call_randomize(txn);"
#
#"randomize"  exists in the file:  "uvm_files\driver1.sv"  in line number:  22
#Found:  "assert.randomize(txn);"
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
#FUNCTIONS AND TASKS TYPE
#
#Checking for:  ['function', 'task']  in uvm hierarchy files.
#
#"function"  exists in the file:  "uvm_files\driver1.sv"  in line number:  9
#Found:  "virtual function void build_phase(uvm_phase phase);"
#
#"function"  exists in the file:  "uvm_files\driver1.sv"  in line number:  14
#Found:  "virtual function run_phase1();"
#
#"function"  exists in the file:  "uvm_files\driver1.sv"  in line number:  20
#Found:  "virtual function run_phase();"
#
#"task"  exists in the file:  "uvm_files\driver1.sv"  in line number:  26
#Found:  "virtual task task_name();"
#
#FUNCTIONS AND CREATE_METHODS
#
#Checking for:  ['new', 'build', 'connect', 'end_of_elaboration', 'start_of_simulation', 'run', 'extract', 'check', 'report', 'final']  in uvm hierarchy files.
#
#"build"  exists in the file:  "uvm_files\driver1.sv"  in line number:  9
#Found:  "virtual function void build_phase(uvm_phase phase);"
#
#"run"  exists in the file:  "uvm_files\driver1.sv"  in line number:  14
#Found:  "virtual function run_phase1();"
#
#"run"  exists in the file:  "uvm_files\driver1.sv"  in line number:  20
#Found:  "virtual function run_phase();"
#
#Need these phases to be defined in the uvm hierarchy:  ['run', 'connect', 'build', 'start_of_simulation', 'end_of_elaboration', 'check', 'report', 'final', 'new', 'extract']
#
#INITIATION OF TESTCASES
#
#Checking for:  ['start_item', 'finish_item', 'raise_objection', 'drop_objection']  in uvm hierarchy files.
#
#"raise_objection"  exists in the file:  "uvm_files\driver1.sv"  in line number:  15
#Found:  "phase.raise_objection();"
#
#"drop_objection"  exists in the file:  "uvm_files\driver1.sv"  in line number:  17
#Found:  "phase.drop_objection();"
#
#"start_item"  exists in the file:  "uvm_files\driver1.sv"  in line number:  21
#Found:  "start_item();"
#
#"finish_item"  exists in the file:  "uvm_files\driver1.sv"  in line number:  23
#Found:  "finish_item();"
#
#CREATE METHODS
#
#Checking for:  ['type_id', 'uvm_config_db']  in uvm hierarchy files.
#
#"type_id"  exists in the file:  "uvm_files\driver1.sv"  in line number:  11
#Found:  "s0 = uvm_sequencer#(Item)::type_id::create("s0", this);"
#
#USAGE OF p_sequencer AND m_sequencer
#
#Checking for:  ['p_sequencer', 'm_sequencer']  in uvm hierarchy files.
#
#"p_sequencer"  exists in the file:  "uvm_files\driver1.sv"  in line number:  6
#Found:  "p_sequencer sqr1;"
#
#"m_sequencer"  exists in the file:  "uvm_files\driver1.sv"  in line number:  7
#Found:  "m_sequencer sqr2;"
#
#SUPER METHODS
#
#Checking for:  ['super']  in uvm hierarchy files.
#
#"super"  exists in the file:  "uvm_files\driver1.sv"  in line number:  10
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
