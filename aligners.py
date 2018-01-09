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
    def prepare_directory(self,alignerName):
        cwd = os.getcwd()
        cwd = os.path.join(cwd,"aligners")
        cwdAligner = os.path.join(cwd,alignerName)
        if not (os.path.exists(cwd)) :
            os.mkdir(cwd)
        if not (os.path.exists(cwdAligner)):
            os.mkdir(cwdAligner)

class hisat(aligner):
    def __init__(self,inputfile,outputfile=None,workingpath=None):
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.workingpath = workingpath
        self.prepare_directory("HISAT")
     #   self.workingpath=21
    @property
    def build_command(self):


        #os.chdir(self.workingpath)
        indexFolder = os.path.join(self.workingpath,"INDEX")
        
        if not os.path.exists(indexFolder):
            os.mkdir(indexFolder)

        #print("Copying input file from main to index directory")
        #os.rename(self.inputfile,os.path.join(indexFolder,self.inputfile))

        print("Start building the index")
        #os.chdir(indexFolder)
        #print(os.getcwd())
        name, extension = os.path.splitext(self.inputfile)
        name = os.path.join(indexFolder,name)
        cmd = ["hisat-build","-q",self.inputfile,name] 
        
        return cmd
    @property
    def get_index_directory():
        pass


class hisat2(aligner):
    def __init__(self,inputfile,outputfile=None,workingpath=None):
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.workingpath = workingpath
        self.prepare_directory("HISAT2")
 		#inial
 	
    @property
    def build_command(self):


        #os.chdir(self.workingpath)
        indexFolder = os.path.join(self.workingpath,"INDEX")
        
        if not os.path.exists(indexFolder):
            os.mkdir(indexFolder)

        #print("Copying input file from main to index directory")
        #os.rename(self.inputfile,os.path.join(indexFolder,self.inputfile))

        print("Start building the index")
        name, extension = os.path.splitext(self.inputfile)
        name = os.path.join(indexFolder,name)
        cmd = ["hisat2-build","-q",self.inputfile,name] 
        
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
 
