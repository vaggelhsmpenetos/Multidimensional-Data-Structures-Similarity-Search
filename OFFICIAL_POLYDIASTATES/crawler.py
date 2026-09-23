import json
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import csv

links = []
awards = []
surnames1 = []
education = []
publications = []

def get_computer_scientist_surnames(url, limit=682):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ul_elements = soup.select('div.mw-parser-output ul')
        wiki = 'https://en.wikipedia.org/'
        surnames = []
        for ul in ul_elements:
            li_elements = ul.find_all('li')
            for li in li_elements:
                a_elements = li.find('a')
                #print("Link:", a_elements.get("href"), "Text:", a_elements.string)
                link1 = a_elements.get("href")
                link = wiki+link1
                links.append(link)
                surname = a_elements.text.split()[-1]
                surnames.append(surname)
                if len(surnames) == limit:
                    return surnames

        return surnames    
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
def crawl(url,awards):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        awards_elements = soup.select('div.plainlist ul')
        awards_section = soup.find('th', {'scope': 'row', 'class': 'infobox-label'}, string ='Awards')

        counter = 0
        if awards_section:
        # Navigate to the corresponding ul containing the awards
            ul = awards_section.find_next('ul')

            for li in ul.find_all('li'):
                 a_element = li.find('a')
                 if a_element:
                    #print(a_element.get('href'))
                    counter += 1
            
            #print(counter)
    
    
        awards.append(counter)



    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    

def crawl_education(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        education_section = soup.find('span', {'class': 'mw-headline'}, string =re.compile("Education",re.IGNORECASE))

        if education_section is not None:
            # Navigate to the corresponding p containing the education details
            p = education_section.find_next('p')
            if p is not None:
                education.append(p.getText())
            else:
                education.append("")
        else:
            education.append("")




    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def crawl_publications(url):
    response = requests.get(url)
    
    

    
    if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            publication_keywords = [
            'Selected publications',
            'Books',
            'Bibliography',
            'Papers',
            'Works',
            'Selected notable papers',
            'Publications'
        ]

            for publication_keywords in publication_keywords:
                publication_section = soup.find('span', {'class': 'mw-headline'}, string =re.compile("Publication",re.IGNORECASE))
                
                counter = 0
                if publication_section:
                # Navigate to the corresponding ul containing the awards
                
                    ul = publication_section.find_next('ul')

                    for li in ul.find_all('li'):
                        counter += 1
                    
                    #print(counter)
            
        
            publications.append(counter)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None


"""        
def save_to_json(data, filename='scientists_surnames.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
"""
url_to_crawl = 'https://en.wikipedia.org/wiki/List_of_computer_scientists'
surnames = get_computer_scientist_surnames(url_to_crawl, limit=683)

if surnames:
    surnames1 = surnames.copy()
    print(surnames1)
    print(len(surnames1))
else:
    print("No surnames were extracted.")


for i in range(0,682):
    crawl(links[i],awards)

for i in range(0,682):
    crawl_education(links[i])

for i in range(0,682):
    crawl_publications(links[i])
   
csv_file = 'output.csv'

# Combine lists into a list of tuples
data = list(zip(surnames1 , awards, publications ,education))

# Open the CSV file in write mode
with open(csv_file, 'w', encoding='utf-8' ,newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the header if needed
    # writer.writerow(['Column1', 'Column2'])

    # Write the data to the CSV file
    writer.writerows(data)

print(f'Data has been written to {csv_file}')


