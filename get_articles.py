from bs4 import BeautifulSoup
import urllib.request as main
import time
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.pdfbase.ttfonts import TTFont
import json


def save_file(filename, text, format='txt', original = ''):  #Function that through a selection it saves the AI presented data in the wanted type file.

    file_path = filename + "." + format

    if format == 'pdf':  #pdf
        pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
        doc = SimpleDocTemplate(file_path, pagesize=letter)

        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.fontName = "Arial"
        style.language = "el"

        greek_paragraph = Paragraph(text, style)
        doc.build([greek_paragraph])

    elif format == 'txt':  #txt
        with open(file_path, 'w', encoding='utf-8') as f:
            lines = text.replace('\n', '').split('.')
            for line in lines[:-1]:
                f.write(line + '.' + '\n')

    elif format == 'json':  #json
        data = {
            "query": original,
            "answer": text
        }
        json_string = json.dumps(data)
        with open(file_path, 'w') as json_file:
            json_file.write(json_string)

    

def get_links(url): #Function that takes the links of the articles on the current_source(page)
    html_content = None
    with main.urlopen(url) as res:
        html_content = res.read()

    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = soup.find_all('div', class_='article-data border-box right')
        links = []
        for article in articles:
            link = article.find('a')
            if link:
                links.append(link['href'])
    return links


def get_text(urls, wanted_year): #Function that retrieves the text of all the articles found in the current_source(page)
    text = ""
    k = 0
    for url in urls:
        
        html_content = None
    
        with main.urlopen(url) as res:
            html_content = res.read()
            time.sleep(0.05)
        
        if html_content:
            
            soup = BeautifulSoup(html_content, 'html.parser')
            articles = soup.find('div', class_='post-content mb-30 border-box')
            if articles:
                time_element = soup.find('time')
                datetime_value = time_element['datetime']
                dt = datetime_value[:4]
                if wanted_year > dt :
                    return str(dt)


                paragraphs = articles.find_all('p')
                k+=1
                text += "Article {}\n".format(k)
                for paragraph in paragraphs:
                    
                    text += paragraph.get_text() + "\n"
          
    return text           

if __name__ == "__main__":


    wanted_year = str(input("Give me a year: "))  #wanted year to stop searching(<= wanted year) 
    category = str(input("Give me a category: "))   #category


    DEFAULT_SOURCE =  str("https://www.skai.gr")  
    current_source = "https://www.skai.gr/news/{}".format(category)  #link of "next" pages

    page_var = 1
    tail = "?page={}".format(page_var)   # ?page={number} example: https://www.skai.gr/news/technology?page=1

    stop = 1  #delete after


    while True:

        links = get_links(current_source)  
        print(links)
        for i in range(len(links)):   #adds "https://www.skai.gr" in links to become valid
                links[i] = DEFAULT_SOURCE + links[i]

        current_year = get_text(links, wanted_year, stop)[1]  #delete ,stop after
        

        if "?page=" in current_source :     #checks if the form of the url is https://www.skai.gr/news/technology or  https://www.skai.gr/news/technology?page=1
            current_source = current_source[:-1] + str(page_var) 
        else:
            current_source += tail

        page_var += 1

        stop = 2  #delete after
        if current_year < wanted_year:
            break
       

