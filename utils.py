import subprocess as sb
def sam2bam(inputfile,outputfile,numThreads=8):
	'''
	This function converts the sam file into sorted bam file
	input : filename.ext
	'''
	
	sb.call(["samtools", "-@",str(numThreads),"sort", "-o", outputfile,inputfile])
	return 
