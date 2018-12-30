#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time

import json

def scrape():
    scraped_data = {}
    #pointing to the directory where chromedriver exists
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    #visiting the page
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    # Wait for article_teaser_body and content_title to load
    browser.is_element_not_present_by_id("content_title", wait_time=30)
    browser.is_element_not_present_by_id("article_teaser_body", wait_time=30)
    #using bs to write it into html
    html = browser.html
    soup = bs(html,"html.parser")
    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    scraped_data['featured_news'] = {
        "Title": news_title,
        "Paragraph": news_paragraph
    }
    #Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

    #Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a 
    #variable called `featured_image_url`.

    #Make sure to find the image url to the full size `.jpg` image.

    #Make sure to save a complete url string for this image.
    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_image)
    #Getting the base url
    from urllib.parse import urlsplit
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
    #Design an xpath selector to grab the image
    xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"
    #Use splinter to click on the mars featured image
    #to bring the full resolution image
    # browser.is_element_not_present_by_xpath(xpath, wait_time=30)
    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()
    browser.is_element_not_present_by_name("fancybox-image", wait_time=30)
    #get image url using BeautifulSoup
    html_image = browser.html
    soup = bs(html_image, "html.parser")
    img_url = soup.find("img", class_="fancybox-image")["src"]
    full_img_url = base_url + img_url
    scraped_data['image_of_the_day'] = {
        "URL": full_img_url
    }
    #Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather 
    #tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.

    url_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_weather)
    html_weather = browser.html
    soup = bs(html_weather, "html.parser")
    #temp = soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    scraped_data["mars_weather"] = {
        "data": mars_weather
    }
    #Visit the Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about 
    #the planet including Diameter, Mass, etc.

    #Use Pandas to convert the data to a HTML table string.
    url_facts = "https://space-facts.com/mars/"
    browser.visit(url_facts)
    table = pd.read_html(url_facts)
    table[0]
    df_mars_facts = table[0]
    df_mars_facts.columns = ["Parameter", "Values"]
    df_mars_facts.set_index(["Parameter"])
    mars_html_table = df_mars_facts.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    scraped_data['mars_facts_data'] = {
        "table": mars_html_table
    }
    return scraped_data

#Ignoring USGS cause the website is down presumably due to government shut down.

data = scrape()
print(json.dumps(data))