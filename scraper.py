from bs4 import BeautifulSoup as bs
import requests
import os
from splinter import Browser
import pandas as pd

# Initialize Browser
def init_broswer():

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

# Function to scrape Mars data
def scrape_mars_data():
    browser = init_broswer()

    # first data set: get the mars news
    mars_news = 'https://mars.nasa.gov/news/'
    browser.visit(mars_news)
    html_news = browser.html
    soup_news = bs(html_news,'html.parser')

    title = soup_news.find('div', class_='content_title').text
    paragraph = soup_news.find('div', class_='article_teaser_body').text

    # second data set: get the featured mars image
    mars_website = 'https://www.jpl.nasa.gov'
    mars_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(mars_img_url)

    html_images = browser.html
    soup_mars = bs(html_images,'html.parser')
    feat_img = soup_mars.find('div', class_ = 'carousel_items')
    img_link = feat_img.article['style']
    img_link = img_link.split("'")[1]
    full_img_url = mars_website + img_link

    # third data set: get the latest mars weather report
    mars_twitter = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_twitter)
    mars_tweets = browser.html
    soup_twitter = bs(mars_tweets,'html.parser')
    results = soup_twitter.find_all('p', class_ = 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

    for result in results:
        tweet_text = result.text
        last_mars_weather = []

        if "Sol" in tweet_text:
            last_mars_weather.append(tweet_text)
            break

    mars_weather = last_mars_weather[0]

    # fourth data set: Mars Facts
    mars_facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(mars_facts_url)

    df = tables[0]
    df.set_index(0,inplace=True)
    html_table = df.to_html()
    html_table = html_table.replace('\n', '')

    # save the dataframe to an html file
    # df.to_html('table.html')

    # OSX Users can run this to open the file in a browser,
    # or you can manually find the file and open it in the browser
    # !open table.html


    # Fifth data set: Mars hemisphere links and images
    mars_hemis = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemis)

    mars_hemis_html = browser.html
    soup_hemis = bs(mars_hemis_html,'html.parser')

    elements = browser.find_link_by_partial_text('Hemisphere')
    links_found = []
    for each in elements:
        links_found.append(each._element.get_attribute('href'))

    hemispheres = []

    for link in links_found:
        myDict = {}
        browser.visit(link)
        page_html = browser.html
        page_soup = bs(page_html,'html.parser')
        myDict['Title'] = page_soup.find('div', class_='content').find('h2', class_='title').text.split(" Enhanced")[0]
        myDict['URL'] = page_soup.find('div', class_ = 'downloads').find_all('a')[1]['href']
        hemispheres.append(myDict)
        browser.back()

    scraped_data = {'Latest Mars News': [title, paragraph],
                    'Featured Mars Image': full_img_url,
                    'Latest Mars Weather Report': mars_weather,
                    'Mars Facts': html_table,
                    'Mars Hemispheres': hemispheres}

    return scraped_data
