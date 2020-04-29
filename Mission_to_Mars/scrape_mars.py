from splinter import Browser
from bs4 import BeautifulSoup
import time

def init_browser():
    # Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html

    #getting the soup object
    soup = BeautifulSoup(html, 'html.parser')

    #scrapping for the news title
    article = soup.find_all('div', class_='content_title')[1]
    title = article.text

    #scrapping for the paragraph text

    # paragraph  = soup.find('div', class_='article_teaser_body').text

    print(title)

    print('')

    # print(paragraph)

    # Mars Facts

    import pandas as pd

    time.sleep(2)

    url = 'https://space-facts.com/mars/'

    # to get all tables 
    tables_df = pd.read_html(url)
    tables_df


    # get the required table and its DF


    mars_facts=tables_df[0]

    #rename columns of the table

    mars_facts.columns = ["Description","Fact Value"]
    mars_facts


    #pandas to html

    html_table = mars_facts.to_html()
    html_table

    html_table.replace('\n', '')

    # saving to a table html

    mars_facts.to_html('table.html')

    # Mars Hemispheres

    #Url to scrape
    url_mars_hems='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # visiting the browser

    browser.visit(url_mars_hems)
    time.sleep(2)
    html_3= browser.html

    #getting the soup object
    soup_3 = BeautifulSoup(html_3, 'html.parser')


    # getting the titles of the hemispheres
    cerberus_hem = browser.find_by_tag('h3')[0].text
    schiaparelli_hem= browser.find_by_tag('h3')[1].text
    syrtis_hem = browser.find_by_tag('h3')[2].text
    valles_hem = browser.find_by_tag('h3')[3].text

    schiaparelli_hem

    #getting the images

    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')


    html_4=browser.html
    soup_4=BeautifulSoup(html_4, 'html.parser')


    cerbus=soup_4.find_all('a')[5]['href']

    browser.back()

    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    html_4=browser.html
    soup_4=BeautifulSoup(html_4, 'html.parser')


    schia=soup_4.find_all('a')[5]['href']

    hemisphere_image_urls = [
        {"title": cerberus_hem, "img_url": cerbus},
        {"title": schiaparelli_hem, "img_url": schia}
    ]

    print(hemisphere_image_urls)

    mars_dict={}
    mars_dict['title'] = title
    # mars_dict['paragraph'] = paragraph
    mars_dict['table']=html_table
    mars_dict['hem Images']=hemisphere_image_urls

    return mars_dict

if __name__ == "__main__":
    print("\nTesting Data Retrieval:....\n")
    print(scrape())    
