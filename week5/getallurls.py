import urllib2
import re
from pprint import pprint

page = urllib2.urlopen('http://www.westseattle5k.com').read()

# loop to get all http entries

