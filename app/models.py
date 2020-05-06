class Product:
    def __init__(self,product_id,name,opinions=[]):
        self.product_id=product_id
        self.name=name
        self.opinions=opinions
    def __str__(self):
        return f"Product id:{self.product_id}\nName: {self.name}\nOpinions:\n".join(str(opinion) for opinion in self.opinions)
        #return f"Product id:{self.product_id}\nName: {self.name}\nOpinions:\n{[str(opinion) for opinion in self.opinions]}"

class Opinion:
    #słownik z składowymi opinii i ich selektorami
    tags = {
    "recommendation":["div","product-review-summary", "em"],
    "stars":["span", "review-score-count"],
    "content":["p","product-review-body"],
    "author":["div", "reviewer-name-line"],
    "pros":["div", "pros-cell", "ul"],
    "cons":["div", "cons-cell", "ul"], 
    "useful":["button","vote-yes", "span"],
    "useless":["button","vote-no", "span"],
    "purchased":["div", "product-review-pz", "em"]
     }
    #definicja konstruktora(inicjalizatora) klasy Opinion
    def __init__(self, opinion_id=None, author=None, recommendation=None, stars=None, content=None, pros=None,consl=None,useful=None,useless=None, purchased=None,purchase_date=None,review_date=None):
    
        self.opinion=opinion_id
        self.author=author
        self.recommendation=recommendation
        self.stars=stars
        self.content=content
        self.pros=pros
        self.cons=cons
        self.useful=useful
        self.useless=useless
        self.purchased=purchased
        self.purchase_date=purchase_date
        self.review_date=review_date
    def _str_(self):
        return f"Opinion id: {self.opinion}\nAuthor: {self.author}\nStars: {self.stars}"
    def extract_opinion(self):
        pass    
opinion=Opinion()
print(opinion)
product=Product(None,None, opinions=[opinion1,opinion2])
print(product)