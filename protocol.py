import sys,os
from aligners import aligner,hisat, hisat2
from utils import runCommand, deleteFile

class protocol:
	"""docstring for protocol"""
	def __init__(self, parameters,input):
		#super(protocol, self).__init__()
		#self.arg = arg
		self.parameters = parameters
		self.alignersList = []
		self.inputfile=input
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

		#for genome in self.inputfile:
		
		for aligner in self.alignersList:
			
		
			#if os.path.exists(dir):
			#	continue
			#os.mkdir(dir)
			#os.chdir(dir)
			if aligner.upper()=="HISAT":
				objhisat=hisat(inputfile=self.inputfile,workingpath="aligners/HISAT")
				if(self.parameters[0]['build_index']):
					runCommand(objhisat.build_command) #go to the specific directory and run the build command
					
					print("Building index file completed.")
					deleteFile(os.path.join("/workingpath/", "abc")) #delete the inputfile to save the space
				#print("if 1",aligner.upper())
				
				
				#print(cmd)
			
			elif aligner.upper()=="HISAT2":
				objhisat2=hisat2(inputfile=self.inputfile,workingpath="aligners/HISAT2")
				if(self.parameters[1]['build_index']):
					runCommand(objhisat2.build_command)
					
					print("Building index file completed.")
					deleteFile(os.path.join("/workingpath/", "abc")) #delete the inputfile to save the space
			
			elif aligner=="BOWTIE":
				cmd = "bowtie-build ../data/%s %s" %(self.inputfile,self.inputfile)
			
			elif aligner=="STAR":
				cmd = "../../aligners/bin/STAR --runMode genomeGenerate --genomeDir . --genomeFastaFiles ../../data/%s.fa" % (self.inputfile)
			
			elif aligner=="GSNAP":
				cmd = "../../aligners/bin/gmap_build -B ../../aligners/bin -D . -d %s ../../data/%s.fa" % (self.inputfile, self.inputfile)
			else:
				print("Aligner:",aligner," does not exist.")
				assert False

	def print_data(self):
		for item in self.alignerList:
			print("data",item)

				

