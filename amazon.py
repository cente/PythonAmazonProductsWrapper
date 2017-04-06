# This script is created for python 3.6.

try:
    import configparser # pip3.6 install configparser
except ModuleNotFoundError as err:
    print("OS error: {0}".format(err))
    print("Configparser not installed but it's required. pip3.6 install configparser")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

class InputError(Exception):
    pass

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

import argparse # Built in
parser = argparse.ArgumentParser(description='This is an Amazon Products API script written in Python by Brendon Conley.',
    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('operation', metavar='operation',choices=['ItemLookup', 'GenerateConfig'] ,
    help="Required. What are we doing? \n ItemLookup : Looks up a single item. \n GenerateConfig : Creates a new config.ini in the same directory the script runs in")
parser.add_argument('--keywords', "-k", metavar='keyword1, keyword2, keyword3',
    help='Used for ItemLookup',
    dest='keywords',
    nargs='*')

args = parser.parse_args()
if args.operation and args.keywords is None:
    parser.error("Operation requires keyword(s)")

from datetime import datetime


def get_timestamp():
    from time import gmtime, strftime
    return strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())



if args.operation=='ItemLookup':
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
    import hmac
    import hashlib
    import base64
    signature=base64.b64encode(hmac.new(awsprivkey, msg=prerequest.encode('utf-8'), digestmod=hashlib.sha256).digest()) #actual encoding cause amazon likes urls that can work in emails
    params.update({'Signature':signature}) # adding the signature hash to the end of the url
    goodun=Request('GET', apiurl, params=params).prepare()
    print ('Good Url : ', goodun.url)
    s = Session()
    resp=s.send(goodun)
    print (resp.text)
# Responsegroup Values
# Valid Values: Accessories | BrowseNodes | EditorialReview | Images | ItemAttributes | ItemIds | Large | Medium | OfferFull | Offers | PromotionSummary | OfferSummary| RelatedItems$
