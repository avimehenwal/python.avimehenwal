import re
import pdb
import json
from pprint import pprint
from urllib.request import urlopen


url = 'http://product.reflektion.com/rfk/js/11114-78945296/init.js?encode=0'
res = urlopen(url)
r = res.read().decode('utf-8')

# fetch reflektion.js
refjs = re.search(r'\("(//[\w|.|/]+reflektion.js[\?|\w|=|\d]+)', r)
if refjs:
    print(refjs.groups())
else:
    print("you failed")    

#pdb.set_trace()
