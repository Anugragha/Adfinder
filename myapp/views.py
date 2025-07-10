from django.shortcuts import render
import requests
from .models import Tag, Advert
from bs4 import BeautifulSoup
from rake_nltk import Rake
import nltk
import collections
import difflib

#nltk.download('stopwords')
# Create your views here.
def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        #print(url)
        response = requests.get(url=url)
        #print(response)

        #Reading the html document from the response
        soup = BeautifulSoup(response.content,'html.parser')
        #print(soup)
        all_text =''

        #Extracting only the text from the html which is done by filtering the <p> tag
        for para in soup.find_all('p'):
            all_text+=str(para.get_text())
        #print(all_text)

        #Extracting the keywords from the paragraph which saved in all_text
        rake_var = Rake()
        rake_var.extract_keywords_from_text(all_text)
        keywords_extracted = rake_var.get_ranked_phrases()
        #print(keywords_extracted)

        #Matching the extracted keywords to the tags - to find the relevant ads
        adtags = []
        tags = Tag.objects.all()
        for tag in tags:
            adtags.append(tag.tagname)
        seta = set(keywords_extracted)
        setb = set(adtags)
        commonwords = []
        if (seta & setb):
            commonwords = list(seta & setb)
        #print(commonwords)
        #Now matching the commonwords to the ads and saving the ads as list

        relevantads = []
        for advert in Advert.objects.all():
            for tag in advert.tags.all():
                if tag.tagname in commonwords:
                    relevantads.append(advert)
                    relevantads = set(relevantads)
                    relevantads = list(relevantads)
        print(relevantads)
        
        #Rendering the relevant ads on the homepage
        context = {
            'relevantads':relevantads,
            'commonwords':commonwords
        }
        return render(request,'myapp/index.html',context)


    return render(request, 'myapp/index.html')