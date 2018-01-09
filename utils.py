import subprocess as sb
import timeit
def sam2bam(inputfile,outputfile,numThreads=8):
	'''
	This function converts the sam file into sorted bam file
	input : filename.ext
	'''
	sb.call(["samtools", "-@",str(numThreads),"sort", "-o", outputfile,inputfile])
	return 
def runCommand(command):
	'''
	execuate any given command line tool
	'''
	print(command)
	s = timeit.timeit()
	sb.call(command)
	e = timeit.timeit()
	execution_time = e-s

	print("execution time:"+str(execution_time))



def deleteFile(filename):
	'''
	delete any given file
	'''
	print("delete",filename)
	#os.remove(filename)
