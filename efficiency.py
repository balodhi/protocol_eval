import os
import argparse
from tqdm import tqdm
from samfilestats import stats

def write_data(outputfile,pairEnd, countFromfastqc, paironecount, pairtwocount, pairextracount, sumall):
    with open(outputfile,'a') as f:
        f.write('#'*50)
        f.write('\n Total read '+str(countFromfastqc))
        if pairEnd:
            f.write("\n Overall PairEnd")
            f.write('\n \t Uniquely mapped reads: '+str(pairtwocount)+ ' '+ str(round(float(pairtwocount/countFromfastqc)*100.0,3)))
            f.write('\n \t broken reads: '+str(paironecount)+' ' +str(round(float(paironecount/countFromfastqc)*100.0,3)))
            unmapped = countFromfastqc - (pairtwocount+paironecount)
            f.write('\n overall unmapped reads: '+str(unmapped)+' '+str(round(float(unmapped/countFromfastqc)*100.0,3)))
            f.write("\n \n SamFile PairEnd")
            f.write('\n \t Uniquely mapped reads: '+str(pairtwocount)+ ' '+ str(round(float(pairtwocount/sumall)*100.0,3)))
            f.write('\n \t broken reads: '+str(paironecount)+' ' +str(round(float(paironecount/sumall)*100.0,3)))
        else:
            f.write("\n overall SingleEnd")
            f.write('\n \t Uniquely mapped reads: '+str(paironecount)+' '+str(round(float(paironecount/countFromfastqc)*100.0,3)))
            
            f.write("\n \n Samfile SingleEnd")
            f.write('\n \t Uniquely mapped reads: '+str(paironecount)+' '+str(round(float(paironecount/sumall)*100.0,3)))
            
        f.write('\n Overall Multiple mapped reads: '+str(pairextracount)+' ' + str(round(float(pairextracount/countFromfastqc)*100.0,3)))
        f.write('\n \n Samfile Multiple mapped reads: '+str(pairextracount)+' ' + str(round(float(pairextracount/countFromfastqc)*100.0,3))+'\n')
                
        f.write('#'*100)

def fastqcCount(file):
    with open(file,'r') as f:
        content = f.readlines()
    data = None
    for c in content[0:10]:
        if('Total' in c):
            data = c.split()
    count = float(data[-1])
    print(count)
    return count

def efficiency(filesList, pairEnd, aligner):
    fastqcroot = '.'
    samroot = '.'
    for files in filesList:
        
        pathToSam = os.path.join(samroot,(files +'_'+aligner+ '.sam'))
        pathToFastqc = os.path.join(fastqcroot,(files +'_1.txt'))
        
        #paironecount, pairtwocount, pairextracount, sumall = samCount(pathToSam, pairEnd)
        samfileoutput = stats(pathToSam)
        countFromfastqc = fastqcCount(pathToFastqc)
        print('data from samcount' + str(sumall) +' data from textfile '+ str(samfileoutput))
        #write_data ((files+'_'+aligner+'.txt'), pairEnd, countFromfastqc, paironecount, pairtwocount, pairextracount, sumall)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='input.txt', help='give the input file')
    parser.add_argument('--pairend',action='store_true', help='pairEnd')
    parser.add_argument('--aligner',type=str, choices = ['crac'])
    args = parser.parse_args()
    
    filename = args.input
    
    with open(filename,'r') as f:
        filesList = f.read().splitlines()
    
    efficiency(filesList, args.input, args.aligner)