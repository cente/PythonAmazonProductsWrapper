

# This script is created for python 3.6.

# Imports here

import sys
import argparse # Built in
import hmac
import hashlib
import base64
from datetime import datetime

try:
    import configparser # pip3.6 install configparser
except ModuleNotFoundError as err:
    print("OS error: {0}".format(err))
    print("Configparser not installed but it's required. pip3.6 install configparser")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise



# Reusable Functions here

def get_timestamp():
    from time import gmtime, strftime
    return strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())

# Classes
class InputError(Exception):
    pass



# Read the config into variables
config = configparser.RawConfigParser()
config.read("config.ini")

try:
    awstag=config['Amazon Account Settings']['AssociateTag']
except:
    raise InputError('Associate Tag Not Set or Invalid, pass me the -c argument to generate a new config')

try:
    awspubkey=config['Amazon Account Settings']['AWSAccessKey']
except:
    raise InputError('AWS Access Key Not Set or Invalid pass me the -c argument to generate a new config')

try:
    awsprivkey=config['Amazon Account Settings']['AWSSecretKey'].encode()
except:
    raise InputError('AWS Secret Key Not Set or Invalid, pass me the -c argument to generate a new config')

try:
    apiurl=config['Advanced Settings']['API']
except:
    raise InputError('API URL Not Set or Invalid, pass me the -c argument to generate a new config')


# Define and interpret the command line arguments

parser = argparse.ArgumentParser(description='This is an Amazon Products API script written in Python by Brendon Conley.',
    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('operation', metavar='operation',choices=['ItemLookup', 'GenerateConfig', 'ExtendedHelp', 'ItemSearch'] ,
    help="Required. What are we doing? \n ItemLookup : Looks up a single item. \n GenerateConfig : Creates a new config.ini in the same directory the script runs in")
parser.add_argument('--id', "-i", metavar='itemid',
    help='The Amazon ID number. You can specify up to 10 at a time.',
    dest='aid',
    nargs='*')
parser.add_argument('--idtype', "-t", metavar='responses',
    help='Used with -id to change from Amazon ID to SKU/UPC/EAN/ISBN ',
    dest='idtype',
    nargs='*')
parser.add_argument('--keyword', "-k", metavar='keyword',
    help='Keyword for searches. If it contains a space, enclose it with double quotes ("search terms")',
    dest='keyword')

args = parser.parse_args()


if args.operation=='ItemSearch':
    # The ItemSearch operation searches for items on Amazon. The Product Advertising API returns up to ten items per search results page.
    # An ItemSearch request requires a search index and the value for at least one parameter. For example, you might use the BrowseNode parameter for Harry Potter books and specify the Books search index.
    if args.keyword is None:
        parser.error("Operation Requires Keyword")
    print(args.keyword)








if args.operation=='ItemLookup':
    print("Not Yet Implemented")
    sys.exit( 0 )


    import collections
    preparams={
    'AWSAccessKeyId':awspubkey,
    'AssociateTag':awstag,
    'ItemId':args.keywords,
    'Timestamp':get_timestamp(),
    'ResponseGroup':'Images,ItemAttributes,Offers',
    'Operation':'ItemLookup',
    'IdType':'ASIN',
    'Service':'AWSECommerceService'}

    params= collections.OrderedDict(sorted(preparams.items()))
    from requests import Session, Request
    p = Request('GET', apiurl, params=params).prepare() # I'm just url-fying the params here, which alphebetizes, converts bad characters, and sorts them
    import re
    matchObj = re.match('.*\?(.*)', p.url) # I really just want the stuff that comes after the ? in the url
    prerequest='GET' + '\n'+ \
        'webservices.amazon.com' + '\n'+ \
        '/onca/xml' + '\n'+ \
        matchObj.group(1) # Getting it ready for the encoding process
    print(prerequest)

    signature=base64.b64encode(hmac.new(awsprivkey, msg=prerequest.encode('utf-8'), digestmod=hashlib.sha256).digest()) #actual encoding cause amazon likes urls that can work in emails
    params.update({'Signature':signature}) # adding the signature hash to the end of the url
    goodun=Request('GET', apiurl, params=params).prepare()
    print ('Good Url : ', goodun.url)
    s = Session()
    resp=s.send(goodun)
    print (resp.text)
# Responsegroup Values
# Valid Values: Accessories | BrowseNodes | EditorialReview | Images | ItemAttributes | ItemIds | Large | Medium | OfferFull | Offers | PromotionSummary | OfferSummary| RelatedItems$
