import requests
from bs4 import BeautifulSoup
import sqlite3

# Target URL and headers for the request
url = "https://abcnews.go.com/"
headers = {'User-Agent': 'Mozilla/5.0'}

def scrape(db):
    # Make a request to the target URL and parse the HTML content
    html = requests.get(url, headers=headers).content
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    
    # Establish a connection to the SQLite database
    conn = db.connect()

    if conn is not None:
        # Loop through each article on the page
        for article in reversed(soup.find_all('article')):
            try:
                # Extract title and URL from each article
                title = article.find('h1').text.strip()
                article_url = article.find('a')['href']

                # Create a cursor to execute SQLite queries
                c = conn.cursor()

                # Insert data into the content_agg table
                c.execute("INSERT INTO content_agg(source, title, url) VALUES('abcnews', ?, ?)", (title, article_url))

            except sqlite3.IntegrityError:
                # Ignore duplicate entries (based on unique constraint)
                pass
            except Exception as e:
                # Print an error message for other exceptions
                print("Error:", e)
                return False

        # Commit the changes and close the database connection
        conn.commit()
        conn.close()
        return True
    else:
        # Return False if the database connection could not be established
        return False
