# A helper script so that rule developers can quickly determine the next available rule number
from os import listdir
from os.path import isfile, join

rule_files = []
rule_directories = ["./scripts/rules/active", "./scripts/rules/passive"]
for rule_directory in rule_directories:
    for entry in listdir(rule_directory):
        if isfile(join(rule_directory, entry)):
            rule_files.append(entry.split(".")[0])
rule_files.sort(key=int)
print("Next rule number is: {}".format(int(rule_files[len(rule_files)-1])+1))