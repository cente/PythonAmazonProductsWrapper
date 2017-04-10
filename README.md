# Introducing PAPW : Python Amazon Products Wrapper

Another Amazon Wrapper, this time in Python! Made because everything out there that was written in Python is no longer updated, and because I'm using it as an engine for other projects.

# Requirements

* Python 3.6
* requests
* argparser


# Arguments

syntax:

python3.6 amazon.py operation --otherarguments

## Operations

### Amazon Operations
#### Currently Implemented:

##### ItemSearch

The ItemSearch operation searches for items on Amazon. The Product Advertising API returns up to ten items per search results page.

An ItemSearch request requires a search index and the value for at least one parameter. For example, you might use the BrowseNode parameter for Harry Potter books and specify the Books search index.

Currently supported filters:

* Keywords  

#### Operations Yet to be Implemented:

* BrowseNodeLookup
* ItemLookup
* SimilarityLookup
* CartAdd
* CartClear
* CartCreate
* CartGet
* CartModify

### Script/Maintenance Operations

* generateconfig - Creates a brand new config.ini
* version - Output current version

## Additional Arguments

--product-id : ID(s) of products.

--id-type : ASIN, ISBN, UPC, EAN. Defaults to ASIN.

--response : Response group; can specify more than one, separated by a space. Defaults to ItemAttributes. See http://docs.aws.amazon.com/AWSECommerceService/latest/DG/CHAP_ResponseGroupsList.html

Valid Values: Accessories | BrowseNodes | EditorialReview | Images | ItemAttributes | ItemIds | Large | Medium | OfferFull | Offers | PromotionSummary | OfferSummary| RelatedItems$

# Contribute

You are absolutely welcome to submit bug reports or code. This is my first GitHub project so it may take a bit for me to get to processing them, give me some time!
