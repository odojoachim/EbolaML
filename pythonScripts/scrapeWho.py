# end results: getting all data from http://www.who.int/csr/don/archive/disease/ebola/en/ 

from urllib import request

p404 = 'The page or file you are trying to access cannot be found.' #will need this later for the loop
link = 'http://www.who.int/csr/don/2011_05_10/en/'
filename = '2001Dec12.txt'

with request.urlopen(link) as response:
    html = str(response.read())
    if p404 not in html:
        with open(filename, 'w') as f:
            f.write(html)

with open(filename, 'r') as f:
    page = f.read()
    startP = page.find('<!-- begin: primary -->')
    endP = page.find('<!-- end: primary -->')
    
    #Narrow down for better search
    txt = page[startP:endP]
    sentences = txt.split('.')

    keyTerms = ['deaths', 'suspected cases', 'a case']
    cases = []
    
    #Get the reported cases from the text
    for s in sentences:
        if any(kt in s for kt in keyTerms):
            cases.append(s)
    
    #Return only the relevant sentences (should be at least 1)
    cases = [s for s in cases if 'WHO' in s]