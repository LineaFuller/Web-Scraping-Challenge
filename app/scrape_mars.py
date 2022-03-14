# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def initial_browser():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

 def scrape_info():
    browser = initial_browser()
    mars_data = {}

                # Mars News
    # News URL 
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    # Parse the resulting html with soup
    news_html=browser.html
    news_soup = soup(html, 'html.parser')
    # Retrieve the latest news title and paragraph information
    news_title = soup.find_all('div', class_='content_title').get_text()
    news_paragraph = soup.find_all('div', class_='rollover_description_inner').get_text()

                # Updated JPL Mars Space Image

# Image URL
    jpl_url="https://www.jpl.nasa.gov"
    image_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    # Parse the resulting html with soup
    img_html=browser.html
    img_soup = soup(html, 'html.parser')
    # find the relative image url
    relative_url = image_soup.find_all('img')[3]["src"]
    # Use the base url to create an absolute url
    final_image_url = jpl_url + relative_url
    

                # Mars Fact

    # Mars fun facts URL
    facts_url='https://space-facts.com/mars/'
    # use 'read_html' to scrape the facts table into a dataframe
    facts_df=pd.read_html(facts_url[0])
    # assign columns and set index of dataframe
    facts_df.columns = ['Description', 'Mars', 'Earth']
    facts_df.set_index('Description', inplace=True)
    # Convert dataframe into HTML format
    facts_html_df = facts_df.to_html()
    fact_html_df.replace('\n','')



    
            # Mars Hemispheres 

    # Mars hemisphere title and image
    usgs_url = 'https://astrogeology.usgs.gov'
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    # Parse the resulting html with soup
    hemi_html = browser.html
    hemi_soup = soup(html_text, "html.parser")
    # Extract hemisphere item elements
    mars_hemisphere = hemi_soup.find('div', class_='collapsible results')
    mars_item = mars_hemisphere.find_all('div', class_='item')
    hemi_img_url = []

    # Find the elements on each loop 
    # for i in mars_item:
          
  

    # Mars Dictionary
   mars_data={
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image":  final_image_url,
        "facts": str(fact_html_df),
        # "hemispheres": hemispheres,
        "last_modified": dt.datetime.now()
    }
    # Close the browser after scraping
    browser.quit()
    return mars_data




