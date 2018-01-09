import sys,os
from aligners import aligner,hisat, hisat2
from utils import runCommand, deleteFile

class protocol:
	"""docstring for protocol"""
	def __init__(self, parameters):
		super(protocol, self).__init__()
		#self.arg = arg
		self.parameters = parameters
		self.alignersList = []
		self.getAlignerList(self.parameters)
	
	def getAlignerList(self,parameters):
		for parameter in parameters:
			if parameter['enabled']==True:
				self.alignersList.append(parameter['name'])
	
	def run_protocol(self):
		#print("data",self.alignerList[0])
		#if not os.path.exists("indexes"):
		#	os.mkdir("indexes")
		#os.chdir("indexes")

		for genome in ["22_20_-21M","22","genome"]:
			for aligner in self.alignersList:
				
				if (genome == "genome"):
					dir = aligner
				else:
					dir = aligner + "_" + genome
				#if os.path.exists(dir):
				#	continue
				#os.mkdir(dir)
				#os.chdir(dir)
				if aligner.upper()=="HISAT":
					objhisat=hisat(inputfile="abc",workingpath="/data/")
					if(self.parameters[0]['build_index']):
						runCommand(objhisat.build_command)
						deleteFile(os.path.join("/workingpath/", "abc"))
					#print("if 1",aligner.upper())
					
					
					#print(cmd)
				
				elif aligner.upper()=="HISAT2":
					objhisat2=hisat2(inputfile="def",workingpath="/data/")
					if(self.parameters[1]['build_index']):
						runCommand(objhisat2.build_command)
						deleteFile(os.path.join("/workingpath/", "abc"))
				
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

				

