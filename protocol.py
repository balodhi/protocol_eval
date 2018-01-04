import sys,os
from aligners import hisat, hisat2

class protocol:
	"""docstring for protocol"""
	def __init__(self, alignerList):
		super(protocol, self).__init__()
		#self.arg = arg
		self.alignerList = alignerList
	
	def build_indexes(self):
		#print("data",self.alignerList[0])
		#if not os.path.exists("indexes"):
		#	os.mkdir("indexes")
		#os.chdir("indexes")

		for genome in ["22_20_-21M","22","genome"]:
			for aligner in self.alignerList:
				
				if (genome == "genome"):
					dir = aligner
				else:
					dir = aligner + "_" + genome
				#if os.path.exists(dir):
				#	continue
				#os.mkdir(dir)
				#os.chdir(dir)
				if aligner.upper()=="HISAT":
					#print("if 1",aligner.upper())
					cmd = hisat.build_command(self,"abc")
					print(cmd)
				elif aligner.upper()=="HISAT2":
					#print("if 2",aligner.upper())
					cmd = hisat2.build_command(self,"def")
					print(cmd)
				elif aligner=="BOWTIE":
					cmd = "bowtie-build ../data/%s %s" %(genome,genome)
				elif aligner=="STAR":
					cmd = "../../aligners/bin/STAR --runMode genomeGenerate --genomeDir . --genomeFastaFiles ../../data/%s.fa" % (genome)
				elif aligner=="GSNAP":
					cmd = "../../aligners/bin/gmap_build -B ../../aligners/bin -D . -d %s ../../data/%s.fa" % (genome, genome)
				else:
					print("Aligner:",aligner," does not exist.")
					assert False
					
	def print_data(self):
		for item in self.alignerList:
			print("data",item)

				

