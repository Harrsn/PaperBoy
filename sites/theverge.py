import requests
from bs4 import BeautifulSoup
import sqlite3

# Target URL for scraping The Verge
url = "https://www.theverge.com/"

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
        # Loop through each compact entry title element in reverse order
        for i in reversed(soup.find_all('h2', class_='c-entry-box--compact__title')): 
            try:
                # Find the 'a' element within the title element
                j = i.find('a')
                
                # Extract the title and URL from the 'a' element
                title = j.text.strip()
                article_url = j['href']
                
                # Create a cursor to execute SQLite queries
                c = conn.cursor()
                
                # Insert data into the content_agg table
                c.execute("INSERT INTO content_agg(source, title, url) VALUES('theverge', ?, ?)", (title, article_url))
                
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
