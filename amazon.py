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
    awsprivkey=config['Amazon Account Settings']['AWSSecretKey']
except:
    raise InputError('AWS Secret Key Not Set or Invalid, pass me the -c argument to generate a new config')

try:
    apiurl=config['Advanced Settings']['API']
except:
    raise InputError('API URL Not Set or Invalid, pass me the -c argument to generate a new config')

mport argparse # Built in
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



def createSignedRequest (secret,s):
    import hmac
    import hashlib
    import base64
    dig = hmac.new(b'1234567890', msg=s.encode('utf-8'), digestmod=hashlib.sha256).digest()
    base64.b64encode(dig).decode()


if args.operation=='ItemLookup':
    print ('operation matches')
    if len(args.keywords)==1:
        print (args.keywords[0])
        import requests
        payload={
        'AWSAccessKeyId':awspubkey,
        'AssociateTag':awstag,
        'ItemId':args.keywords,
        'Operation':'ItemLookup',
        'ResponseGroup':'Images%2CItemAttributes%2COffers%2CReviews',
        'Service':'AWSECommerceService',
        'timestamp':datetime.utcnow().isoformat() + 'Z',
        'version':'2013-08-01'}
        print (payload)




print (args.keywords[0])
# Responsegroup Values
# Valid Values: Accessories | BrowseNodes | EditorialReview | Images | ItemAttributes | ItemIds | Large | Medium | OfferFull | Offers | PromotionSummary | OfferSummary| RelatedItems$






# Responsegroup Values
# Valid Values: Accessories | BrowseNodes | EditorialReview | Images | ItemAttributes | ItemIds | Large | Medium | OfferFull | Offers | PromotionSummary | OfferSummary| RelatedItems | Reviews | SalesRank | Similarities | Small | Tracks | VariationImages | Variations (US only) | VariationSummary
