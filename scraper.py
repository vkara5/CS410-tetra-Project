# -*- coding: utf-8 -*-
"""
@author: dth3
"""
import re
import json
import requests
from bs4 import BeautifulSoup

targetSections = ["diet"]
data = {}

#start with static URLs and add complexity for scraping with progress
staticURLs = [  "https://en.wikipedia.org/wiki/Polycystic_ovary_syndrome",
                "https://en.wikipedia.org/wiki/Obesity",
                "https://en.wikipedia.org/wiki/Osteoporosis",
                "https://en.wikipedia.org/wiki/Metabolic_syndrome",
                "https://en.wikipedia.org/wiki/Cardiovascular_disease",
                "https://en.wikipedia.org/wiki/Type_2_diabetes",
                "https://en.wikipedia.org/wiki/Irritable_bowel_syndrome",
                "https://en.wikipedia.org/wiki/Cancer",
                "https://en.wikipedia.org/wiki/Atherosclerosis",
                "https://en.wikipedia.org/wiki/Alzheimer%27s_disease",
                "https://en.wikipedia.org/wiki/Stroke",
                "https://en.wikipedia.org/wiki/Gout",
                "https://en.wikipedia.org/wiki/Dementia",
                "https://en.wikipedia.org/wiki/Parkinson%27s_disease",
                "https://en.wikipedia.org/wiki/Crohn%27s_disease",
                "https://en.wikipedia.org/wiki/Attention_deficit_hyperactivity_disorder",
                "https://en.wikipedia.org/wiki/Gallstone",
                "https://en.wikipedia.org/wiki/Coronary_artery_disease",
                "https://en.wikipedia.org/wiki/Hypertension",
                "https://en.wikipedia.org/wiki/Breast_cancer",
                "https://en.wikipedia.org/wiki/Prostate_cancer", 
                "https://en.wikipedia.org/wiki/Colorectal_cancer",
                "https://en.wikipedia.org/wiki/Dyslipidemia",
                "https://en.wikipedia.org/wiki/Non-alcoholic_fatty_liver_disease",
                "https://en.wikipedia.org/wiki/Insulin_resistance",
                "https://en.wikipedia.org/wiki/Hyperuricemia"  ]

for sURL in staticURLs:
    
    response = requests.get(url=sURL,)
    print(response.status_code)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #iterate through all target sections (Diet, Prevention, etc.)
    #for target in targetSections:
        
    #Search for desired section on page
    header = soup.find(id='firstHeading')
    title = header.text
    
    findText = soup.find_all('p')
    #print(findText)
    filtered = []
    
    for f in findText:
        toFilter = str(f.text)
        #print(toFilter)
        if toFilter.lower().__contains__("diet"):
            
            removeBrackets = re.sub(r'\[[^\]]*]', '', toFilter)
            removeParens = re.sub(r'\([^)]*\)', '', removeBrackets)
            toAppend = removeParens.replace("\n", "")
            
            filtered.append(toAppend)
            
            #print(toFilter + '\n\n')
    
    data[title] = filtered
    
                    
#print(data)

with open("sample.json", "w") as outfile:
    json.dump(data, outfile)