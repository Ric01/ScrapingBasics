"""
Registered: CONNECTIS CHILE
This script gets a list of urls and it gets the links count
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import datetime,json


def scrape_link_count(url_list,filepath):

    #url_list = ['http://www.kayser.cl/12-femenino','http://www.monarch.cl','http://www.intime.cl','http://www.besame.com']

    #Check if theres internet connection
    python_url = 'http://www.python.org'
    driver = webdriver.Chrome()
    driver.get(python_url)
    internet_conn = "Python" in driver.title
    driver.close()


    if not internet_conn:
        print("I dont have internet connection")
    else:

        print("i have internet connection")

        #Create file for json dump
        file_tstamp = datetime.datetime.now()
        filename = "scrape"+ str(file_tstamp) + ".json"
        print("Using ", filename, " for scraping data")
        scrape_file = open(filename,'w')

        driver2 = webdriver.Chrome()

        for scrape_site in url_list:
        #Selenium lib to use chrome for scraping
            url = scrape_site
            driver2.get(url)
            #print(driver2.title)

            #Passing html data to beautiful soup
            html = driver2.page_source
            soup = BeautifulSoup(html,'html.parser')
            scrape_data = {}
            scrape_data.update({'url':url})
            for tag in soup.find_all('title'):
                #print(type(tag.text))
                #print(tag.text)
                #scrape_file.write(tag.text)

                if  len(tag.text) == "":
                    print("Couldnt open website: ",url)
                else:
                    print("Mining website:",tag.text)


            # Ejemplo de imprimir todos los links de la pagina.

            link_count = len(soup.find_all('a'))
            print("El sitio tiene ", link_count, "links")
            for scrape_suspect in soup.find_all('lenceria'):
                print(scrape_suspect)

            scrape_data.update({'links': str(link_count)})

            scrape_file.write(json.dumps(scrape_data))
            # print(corp_rank[0]['Bank'],corp_rank[0]['complaint_level'])

        driver2.close()
        scrape_file.close()