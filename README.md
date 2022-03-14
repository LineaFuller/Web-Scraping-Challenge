# Web-Scraping-Challenge

In this assignment, I will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what I did.

# Step 1: Scraping
I used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter to make my initial scrape.

I created a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

Scrape the Mars News Site and collect the latest News Title and Paragraph Text, JPL Mars Space Image, Mars Facts, and Mars Hemispheres. Assign each element to a variable to reference later. 

# Step 2: MongoDB and Flask Application

I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

I started by converting my Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that executed all of my scraping code from above and returned one Python dictionary containing all of the scraped data.

Next, I created a route called /scrape and imported my scrape_mars.py script

I then created a root route / that will queried my Mongo database that passes the mars data into an HTML template to display the data. 

Finally, I used the given HTML template file called index.html that took all of the mars data dictionary and displayed all of the data in the appropriate HTML elements. 
