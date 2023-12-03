import requests
from bs4 import BeautifulSoup
import sqlite3

# Target URL for scraping Fox News
url = "https://www.foxnews.com/"

# Headers to mimic a user agent
headers = {'User-Agent': 'Mozilla/5.0'}

def scrape(db):
    # Make a request to the target URL and get the HTML content
    html = requests.get(url, headers=headers).content
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    
    # Establish a connection to the SQLite database
    conn = db.connect()
    
    if conn is not None:
        # Loop through each article element in reverse order
        for article in reversed(soup.find_all('article')): 
            try:
                # Find the 'a' element within the article
                link = article.find('a')
                
                # Extract the title and URL from the 'a' element
                title = link.text.strip()
                href = link['href']
                
                # Check if the URL is relative and prepend the base URL if needed
                if not href.startswith('http'):
                    href = 'https://www.foxnews.com' + href
                    
                # Create a cursor to execute SQLite queries
                c = conn.cursor()
                
                # Insert data into the content_agg table
                c.execute("INSERT INTO content_agg(source, title, url) VALUES('foxnews', ?, ?)", (title, href))
                
            except sqlite3.IntegrityError as e:
                # Ignore duplicate entries based on the unique constraint
                pass
            except Exception as e:
                # Print an error message for other exceptions
                print("Error: ", e)
                return False
                
        # Commit the changes and close the database connection
        conn.commit()
        conn.close()
        return True
    else:
        # Return False if the database connection could not be established
        return False
