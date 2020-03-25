#import bibliotek
import requests
from bs4 import BeautifulSoup
import json
import pprint
#adres URL z przykładowej strony z opiniami
url_prefix="https://www.ceneo.pl"
product_id=input("Podaj kod produktu: ")
url_postfix="#tab=reviews"
url=url_prefix+"/"+product_id+url_postfix
opinions_list=[]
while url:
    #poranie kodu html strony z podanego URL
    page_respons=requests.get(url)
    page_tree=BeautifulSoup(page_respons.text, 'html.parser')

    #wydobycie z  kodu HTML strony fragmentów odpowiadającyh poszczególnym opiniom
    opinions=page_tree.find_all("li", "review-box")

    #wydobycie składowych dla  pojedynczej opinii 
    for opinion in opinions:
    #identyfikator: li.review-box["data-entry-id"]
    # autor: div.reviewer-name-line
    #rekomendacja: div.product-review-summary > em
    #gwiazdki: span.review-score-count
    #potwierdzona zakupem: div.product-review-pz
        opinion_id=opinion['data-entry-id']
        author=opinion.find("div","reviewer-name-line").string
        recommendation=opinion.find("div","product-review-summary").find("em").string
        stars=opinion.find("span","review-score-count").string
        try:
            purchased=opinion.find("div","product-review-pz").find("em").string
        except AttributeError:
            purchased=None
        #data wystawienia: span.review-time > time["datetime"]- pierwszy element listy
        dates=opinion.find("span","review-time").find_all("time")
        review_date=dates.pop(0)["datetime"]
        try:
            purchase_date=dates.pop(0)["datetime"]
        except IndexError:
            purchase_date=None
        #data zakupu: span.review-time > time["datetime"]- drugi element listy jeżeli istnieje
        useful=opinion.find("button","vote-yes").find("span").string
        useless=opinion.find("button","vote-no").find("span").string
        content=opinion.find("p","product-review-body").get_text()

        ##przydatna: span[id=^vote-yes]
                #button.vote-yes["data-total-vote"]
                #button.vote-yes > span
        #nieprzydatna: span[id=^vote-no]
                #button.vote-no["data-total-vote"]
                # button.vote-no > span
        #treść: p.product-review-body
        #wady: div.cons-cell > ul
        try:
            pros=opinion.find("div","pros-cell").find("ul").get_text()
        except AttributeError:
            pros=None
        #zalety: div.pros-cell > ulpytho    
        try:
            cons=opinion.find("div","cons-cell").find("ul").get_text()
        except AttributeError:
            cons=None    

        opinion_dict={
            "opinion_id":opinion_id,
            "recommendation":recommendation,
            "starts":stars,
            "content":content,
            "author":author,
            "pros":pros,
            "cons":cons,
            "useful":useful,
            "useless":useless,
            "purchased":purchased,
            "purchase_date":purchase_date,
            "review_date":review_date
        }    
        opinions_list.append(opinion_dict)
    try:
        url=url_prefix+page_tree.find("a","pagination_next")["href"]
    except TypeError:
        url=None
    print(url)    

    
with open(product_id+".json","w",encoding="utf-8") as fp:
    json.dump(opinions_list,fp,ensure_ascii=False,indent=4,separators=(",",":"))

    
