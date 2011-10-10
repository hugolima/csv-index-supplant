#!/usr/bin/python

from __future__ import with_statement
import sys, re

class CsvSupplant():
    def __init__(self, sourceFile, delimiter, template):
        self.sourceFile = sourceFile
        self.delimiter = delimiter
        self.template = template

    def supplant(self):
        with open(self.sourceFile, 'r') as source:
            outputText = ''
            for line in source:
                tokens = line.split(self.delimiter)
                result = self.template
                for strIndex in re.findall(r'\{[0-9][0-9]*\}', self.template):
                    index = int(strIndex.strip('{}'))
                    result = re.sub(r'\{' + str(index)  + '\}', tokens[index].strip('\n'), result)
                outputText += result + '\n'
        
        return outputText

if __name__ == '__main__':
    parser = CsvSupplant(sys.argv[1], sys.argv[2], sys.argv[3])
    print parser.supplant()