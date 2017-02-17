#script goal is to categorize set of words in 3 categories - professional, organizational and social
#whole set consists of 30 subsets(responses), 5 to 20 words each, separated by STOP string
#whole set is contained in slova.txt and is compared with each of 3 lists, which derive from slova_org.txt, slova_pro.txt and slova_soc.txt
#expected result is list, which contains 30 lists with 3 integers in each. integer is number of words from each category in each response

#initiating resulting counter 
counter=[]
for x in range(30):
	counter.append([0, 0, 0])

#creating lists, to which we will compare our words
import codecs
with codecs.open("slova_org.txt", "rb", encoding="utf-8") as fp:
    org_list = []
    for line in fp:
        org_list.append(line[:-2]) if line[-1] == "\n" else org_list.append(line)
with codecs.open("slova_pro.txt", "rb", encoding="utf-8") as fp:
    pro_list = []
    for line in fp:
        pro_list.append(line[:-2]) if line[-1] == "\n" else pro_list.append(line)
with codecs.open("slova_soc.txt", "rb", encoding="utf-8") as fp:
    soc_list = []
    for line in fp:
        soc_list.append(line[:-2]) if line[-1] == "\n" else soc_list.append(line)

#all words are lowered to reach unification
org_list = [item.lower() for item in org_list]
pro_list = [item.lower() for item in pro_list]
soc_list = [item.lower() for item in soc_list]



response=0
import codecs
fini=codecs.open('slova.txt', encoding='utf-8')
fin=fini.readlines()
for res in fin:
	res=res.strip()
	res=res.lower()
	if res in org_list:
		counter[response][0]+=1
	if res in pro_list:
		counter[response][1]+=1
	if res in soc_list:
		counter[response][2]+=1
	if res == "stop":#STOP means completion of given response and accessing new one
		response+=1

for LIST in counter:
        print (LIST)





#DUMP ALL THE WAY DOWN THERE, PAY NO ATTENTION

        
#def print_list(the_list):
#	for LIST in the_list:
#		print(LIST)
#		
#def longread(length_count, quantity_count):
#	fin = open('words.txt')
#	counter = 0
#	for line in fin:
#		while counter<quantity_count:
#			word=fin.readline().strip()
#			if len(word)==length_count:
#				print (word)
#				counter = counter+1
#				
#				
#reading from formatted list to lists
#import codecs
#fin=codecs.open('slova.txt', encoding='utf-8')
#org_list=[]
#pro_list=[]
#soc_list=[]
#for line in fin:
#	word=fin.readline().strip()
#	if word != "STOP":
#		org_list.append(word)
#
#

