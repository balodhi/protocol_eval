import subprocess
import os
'''
aligner class the base parent class to implement function on basic lcass levels
while each aligner is a child of the aligner class
'''

class aligner:
    """Class to represent an aligner"""
    #def __init__(self,inputfile=None,outputfile=None):
    	
    @property
    def num_examples(self):
        """Return qtty of examples in dataset"""
        raise NotImplementedError

    def next_batch(self, batch_size):
        """Return batch of required size of data, labels"""
        raise NotImplementedError
 
class hisat(aligner):
    def __init__(self,inputfile,outputfile=None,workingpath=None):
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.workingpath = workingpath
     #   self.workingpath=21
    @property
    def build_command(self):
        filename = os.path.join(self.workingpath, self.inputfile)
        name, extension = os.path.splitext(self.inputfile)
        cmd = ["hisat-build",filename,name] 
        return cmd

class hisat2(aligner):
    def __init__(self,inputfile,outputfile=None,workingpath=None):
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.workingpath = workingpath
 		#inial
 	
    @property
    def build_command(self):
        filename = os.path.join(self.workingpath, self.inputfile)
        name, extension = os.path.splitext(self.inputfile)
        cmd = ["hisat-build2",filename,name]
        return cmd


class bowtie(aligner):
 	#def __init__(self):
 		#inial
 	
 	def build_command(self,inputfile):
 		cmd = "bowtie-build ../data/%s %s" %(inputfile,inputfile)


class star(aligner):
 	#def __init__(self):
 		#inial
 	
 	def build_command(self,genome):
 		cmd = "../../aligners/bin/STAR --runMode genomeGenerate --genomeDir . --genomeFastaFiles ../../data/%s.fa" % (genome)

class gsnap(aligner):
 	#def __init__(self):
 		#inial
 	
 	def build_command(self,genome):
 		cmd = "../../aligners/bin/gmap_build -B ../../aligners/bin -D . -d %s ../../data/%s.fa" % (genome, genome)
 
