# http://www.who.int/csr/don/archive/disease/ebola/en/ 

seed = 'http://www.who.int/csr/don/archive/disease/ebola/en/'

# Process each pair of links and locations
def getInfo(pair):
    # Getting the http link
    link = pair
    link = link[:link.find('"')]
    link = link.replace('/entity', 'http://www.who.int') # Good!
    
    # Getting the date to use later on
    sDate = link.find('don/')+4
    eDate = link.find('ebola')-1
    date = link[sDate:eDate]
    date = date.replace('/en/index.ht', '')
    
    place = pairs[1]
    sPlace = place.find('_info">')+7
    ePlace = place.find('</span>', sPlace)
    place = place[sPlace:ePlace].strip()
    
    i = {'link':link, 'date':date, 'place':place}
    info.append(i)

#list of dictionaries
info = []

# Got all links from the source code to get going
with open('cleanlinks.txt', 'r') as f:
    page = f.read()
    page = page.replace('<li >', '')
    page = page.replace('</li>', '')
    page = page.strip()
    pairs = page.split('<a  href="')
    for p in pairs:
        getInfo(p)
    f.close()

# ---------------------------------------------------
from urllib import request

p404 = 'The page or file you are trying to access cannot be found.'
link = info[1]['link']
filename = 'temp.txt'

with request.urlopen(link) as response:
    html = str(response.read())
    if p404 not in html:
        with open(filename, 'w') as f:
            f.write(html)
            f.close()

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
    for i in range(len(cases)):
        c = cases[i][::-1]
        c = c[:c.find('>')]
        cases[i] = c[::-1]
