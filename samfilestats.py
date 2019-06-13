import sys
from tqdm import tqdm
from collections import Counter, OrderedDict


def stats(samfile):
	output_stats = OrderedDict()
	reads = Counter()
	__reads = {}
	__reads_status = {}

	#amppability
	output_stats ['total'] = 0
	output_stats ['mapped'] = 0
	output_stats ['unmapped'] = 0
	output_stats ['unique'] = 0
	output_stats ['multi'] = 0
	output_stats ['broken'] = 0

	#samfile = './head.sam'
	print('parsing the same file . .. ')

	with open(samfile) as f:
		for line in tqdm(f):
			split = line.split('\t')
			if (not line.startswith('@PG') and not line.startswith('@HD') and not line.startswith('@SQ')and len(split) >= 10 ):
				read_name = split[0]
				flag_code = int(split[1])
				name_and_flag = read_name
				
				if (flag_code & 0x0001 != 0): #is it paired end if yes
					
					if(flag_code & 0x0004 != 0 or flag_code & 0x0008 != 0):
						if(flag_code & 0x0004 != 0):
							try:
							
								if __reads_status[read_name] == 'unmapped':
									output_stats['unmapped'] += 1
									output_stats['total'] += 1
								
								if __reads_status[read_name] == 'broken':
									print(str(read_name)+' broken')
									output_stats['broken'] += 1
									output_stats['total'] += 1
							  
							except Exception as e:
								__reads_status[read_name] = 'unmapped'
								output_stats['total'] += 1
											
						if(flag_code & 0x0008 != 0):
							try:
							
								if __reads_status[read_name]:
									
									output_stats['broken'] += 1
									output_stats['total'] += 1
							
							except Exception as e:
								__reads_status[read_name] = 'broken'
								output_stats['total'] += 1
					else:
						if(flag_code & 0x0040):
							name_and_flag += ':first'
						if(flag_code & 0x0080 != 0):
							name_and_flag += ':second'
					
						if (name_and_flag not in reads):
							reads[name_and_flag] +=1
							output_stats['unique'] +=1 
							output_stats['total'] += 1
							output_stats['mapped'] +=1
						#read is multi-mapped
						else: 
							#print(line)
							if (reads[name_and_flag]==1):
								output_stats['unique'] -= 1
								output_stats['multi'] +=1
							reads[name_and_flag] +=1
						
						
				else:   #single
					if(flag_code & 0x0004 != 0): #if unmapped
						output_stats['unmapped'] += 1
						output_stats['total'] += 1
					
					if (name_and_flag not in reads):
						reads[name_and_flag] +=1
						output_stats['unique'] +=1 
						output_stats['total'] += 1
						output_stats['mapped'] +=1
	return output_stats
