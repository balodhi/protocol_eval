import subprocess
'''
aligner class the base parent class to implement function on basic lcass levels
while each aligner is a child of the aligner class
'''

class aligner:
    """Class to represent an aligner"""
    @property
    def num_examples(self):
        """Return qtty of examples in dataset"""
        raise NotImplementedError

    def next_batch(self, batch_size):
        """Return batch of required size of data, labels"""
        raise NotImplementedError
 
class hisat(aligner):
 	#def __init__(self):
 		#inial
 	
 	def build_command(self,genome):
 		cmd = "hisat-build ../data/%s %s" %(genome,genome)
 		
 		return cmd



class hisat2(aligner):
 	#def __init__(self):
 		#inial
 	
 	def build_command(self,genome):
 		cmd = "hisat2-build ../data/%s.fa %s" %(genome,genome)
 		
 		return cmd


class bowtie(aligner):
 	#def __init__(self):
 		#inial
 	
 	def build_command(self,genome):
 		cmd = "bowtie-build ../data/%s %s" %(genome,genome)


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
 