#!/usr/bin/python
# The purpose of this script is to extract list of WGS samples from the samples folder:

import os

class SampleExtractPlugin:
    def input(self, infile):
        inputfile = open(infile, 'r')
        self.parameters = dict()
        for line in inputfile:
            contents = line.strip().split('\t')
            self.parameters[contents[0]] = contents[1]

    def run(self):
        pass

    def output(self, outputfile):
       out_list = outputfile

       with open(out_list, 'w') as out:
           for f in os.listdir(self.parameters["abunddir"]):
               if self.parameters["suffix"] in f:
                   sample_name = f.split(self.parameters["suffix"])[0]
                   out.write(sample_name+"\n")
