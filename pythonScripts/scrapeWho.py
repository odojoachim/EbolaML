# end results: getting all data from http://www.who.int/csr/don/archive/disease/ebola/en/ 

import urllib.request

p404 = 'The page or file you are trying to access cannot be found.' #will need this later for the loop
link = 'http://www.who.int/csr/don/2001_12_12/en/'
filename = '2001Dec12.txt'

with urllib.request.urlopen(link) as response:
    html = str(response.read())
    if p404 not in html:
        with open(filename, 'w') as f:
            f.write(html)

with open(filename, 'r') as f:
    page = f.read()
    startP = page.find('Disease Outbreak Reported')
    
    # Narrow down the search span
    txt = page[startP:page.find('<!-- end: primary -->')]
    sentences = txt.split('.')

    keyTerms = ['deaths', 'suspected cases']
    cases = []
    
    #Get the reported cases from the text
    for s in sentences:
        if any(kt in s for kt in keyTerms):
            cases.append(s)
    cases = [s for s in cases if 'WHO has received reports' in s]