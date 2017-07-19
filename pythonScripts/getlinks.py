# http://www.who.int/csr/don/archive/disease/ebola/en/ 

from urllib import request

p404 = 'The page or file you are trying to access cannot be found.' #will need this later for the loop
seed = 'http://www.who.int/csr/don/archive/disease/ebola/en/'
filename = 'links.txt'

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