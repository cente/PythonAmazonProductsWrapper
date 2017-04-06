# Intro

PAPW : Python Amazon Products Wrapper

Another Amazon Wrapper, this time in Python! Made because everything out there that was written in Python is no longer updated, and because I'm using it as an engine for other projects. You're encouraged to do the same!


# Requirements

* Python 3.6
* requests
* argparser


# Arguments

python3.6 amazon.py operation

## Operation

### Amazon Operations
Currently Implemented:
ItemSearch

Yet to be Implemented:
BrowseNodeLookup
ItemLookup
SimilarityLookup
CartAdd
CartClear
CartCreate
CartGet
CartModify

### Script/Maintenance Operations
GenerateConfig

### Arguments

--product-id : ID(s) of products.
--id-type :

--response : Response group; can specify more than one, separated by a space. See http://docs.aws.amazon.com/AWSECommerceService/latest/DG/CHAP_ResponseGroupsList.html
Valid Values: Accessories | BrowseNodes | EditorialReview | Images | ItemAttributes | ItemIds | Large | Medium | OfferFull | Offers | PromotionSummary | OfferSummary| RelatedItems$
Defaults to ItemAttributes

# Contribute

You are absolutely welcome to submit bug reports or code. This is my first GitHub project so it may take a bit for me to get to processing them, give me some time!
