import sys
import re

#with open(sys.argv[1],'rt')as file1, open(sys.argv[2],'rt')as file2:

class Compare:

	def __init__(self):
		count1=0
		count2=0
		count3=0
		count4=0
		count5=0
		count6=0
		count7=0
		list1=[]
		list2=[]
		dict1= {}
		dict2= {}
		with open(sys.argv[1],'rt')as file1, open(sys.argv[2],'rt')as file2:

			for line in file1:
			#matchobj1 = re.match('tempest',line)
			#if matchobj1:
				if line.startswith('tempest'):
					words= line.split()
			
					if words[1] == '...': 
						count1 += 1
						dkey1 = words[0]
						dval1 = words[2]
						dict1[dkey1] = dval1
						a = str(dkey1) + str(dval1)
						list1.append(a)
				
			print "Total number of lines starting with 'tempest' in first file" 
			print count1
		#for i in dict1['ok']:	
		#	print i

			for line in file2:
			#matchobj2 = re.match(r'^tempest',line, re.M)
			#if matchobj2:
				if line.startswith('tempest'):
					words1= line.split()
				#count2 +=1
					if words1[-2] == '...': 
						count2 += 1
						dkey2 = words1[0]
						dval2 = words1[2]
						dict2[dkey2] = dval2				
						b = str(dkey2) + str(dval2)
						list2.append(b)
			
			print "Total number of lines starting with 'tempest' in second  file"
			print count2
		#print count3
		#for j in dict4['FAIL']:	
		#	print j
	
			f1= open("match1same",'w+')
			for i in list1:
				for j in list2:
		#s = set(list1) & set(list2)
					if i==j:
						f1.writelines(i+ '\n')
						count3 +=1		
			f1.close()	
			print "Total number of lines 'tempest' to '...' matching status same  ( both are 'ok' or both are 'FAIL' )"	
			print count3

			f2= open("match2diff",'w+')
			for i in dict1:
			#print dict1[i]		
				for j in dict2:
					if i==j:	
						if dict1[i] != dict2[j]:
							f2.writelines(i+ '\n')					
							count4 +=1
			f2.close()
			print "Total number of lines 'tempest' to '...' matching status differs  ( one file have 'ok' and another has 'FAIL' )"	
			print count4

			f3= open("match3any", 'w+')	
			for i in dict1:
				for j in dict2:
		#s = set(list1) & set(list2)
					if i==j:
						f3.writelines(i+ '\n')
						count5 +=1
			f3.close()
			print "Total number of lines 'tempest' to '...' matching status may be anything ( the status is neither 'ok' not 'FAIL')"		
			print count5

			f4= open("match4sec", 'w+')
			for i in dict1:
				if i in dict2:
					continue
				else:
					count6 +=1
					f4.writelines(i+ '\n')
			f4.close()
			print "Total number of lines 'tempest' to '...' available in first not in second"	
			print count6

			f5= open("match5fir", 'w+')
			for i in dict2:
				if i in dict1:
					continue
				else:
					count7 +=1
					f5.writelines(i+ '\n')
			f5.close()
			print "Total number of lines 'tempest' to '...' available in second not in first"	
			print count7

a=Compare()

		
	
