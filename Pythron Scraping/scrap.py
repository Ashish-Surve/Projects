##########################################################################################
# This program was ade to scrap a webpage and create a Machine-Op Table for Assembler.
# @Author Ashish Surve
# @Version 0.1.0
##########################################################################################

# import libraries
from urllib.request import urlopen #for getting the page.
from bs4 import BeautifulSoup      #for scraping

#url for the page
url_page='http://ref.x86asm.net/coder32.html'
#get the html in a variable
page = urlopen(url_page);

#parsing the page in BS format
soup= BeautifulSoup(page,'html.parser')

#get the tag where data exists.
table = soup.find('table',attrs={'class':'ref_table notpublic'})

#here I m storing all tbodies individually.
#Later going to extract from this the op codes and instructions
tbodyids = table.findAll('tbody')
#print(len(tbodyids))

#writing data to a file
f= open("Opcodes.txt","at")
p_opc="p"   #Primary opcode in hexadecimal
mnem="y"	   #Mnemonic for the opcode
for tbi in range(0,len(tbodyids)):
	tds = tbodyids[tbi].findAll('td') #one <tr> has many row divisions called tds
	#some tbody didnt have an id attribute which gives us p_opc aka prim opcode
	if tbodyids[tbi].has_attr('id'):
		p_opc=tbodyids[tbi]['id']
	# some tbody didnt have ids so instead of id atribute we get the opcode from a table field	
	else:
		p_opc=tds[2].text.strip()  #strip() - used to get rid of <tags>
		p_opc="x"+p_opc			 # the column used doesnt have an x notation for hexadecimal
	mnem = tds[10].text.strip()  # extract the mnem from the column or the 11th <td> of <tr>
	if not(p_opc=="x" or mnem=="" or mnem=="undefined"):   #if the opcode or mnem is empty
		print(p_opc+"   "+mnem)						#to see the o/p
		f.write(p_opc+"   "+mnem+"\n")				#saving in the file
	else:
		print("EMPTY EMPTY=========================================>")	


