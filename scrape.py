from database import db
import time
from sites import theverge, fox, wired, reddit, abc, techcrunch

# Dictionary mapping source keys to their display names
sources = {
    'abc': 'ABC',
    'fox': 'FOX',
    'reddit': 'Reddit',
    'techcrunch': 'TechCrunch',
    'theverge': 'The Verge',
    'wired': 'Wired'
}

def scrape_all():
    # Scrapes content from all specified sources and handles errors.
    for source_key, source_name in sources.items():
        # Use globals() to dynamically call the scrape function of each source
        if not globals()[source_key].scrape(db):
            print(f"ERROR: {source_name} SCRAPE ERROR")
    print("SCRAPING COMPLETE")

def get_content():
    # Retrieves content from the database for all specified sources.
    content = {}
    conn = db.connect()
    c = conn.cursor()

    for source_key, source_name in sources.items():
        # Execute a SELECT query for each source and store the result in the content dictionary
        result = c.execute(f"SELECT * FROM content_agg WHERE source = '{source_key}' ORDER BY rowid DESC;")
        content[source_name] = result.fetchall()

        if content[source_name] == []:
            conn.close()
            return None

    conn.close()
    return content

def get_content_for_source(s):
    # Retrieves content from the database for a specific source.
    if s in sources:
        source_name = sources[s]
        content = {}
        conn = db.connect()
        c = conn.cursor()

        # Execute a SELECT query for the specified source and store the result in the content dictionary
        result = c.execute(f"SELECT * FROM content_agg WHERE source = '{s}' ORDER BY rowid DESC;")
        content[source_name] = result.fetchall()

        if content[source_name] == []:
            conn.close()
            return None

        conn.close()
        return content
    else:
        return None

def scrape_start(sleep_time=3600):
    # Initiates a continuous scraping process with a specified sleep time between scrapes.
    while True:
        scrape_all()
        time.sleep(sleep_time)

# Running ScrapeJob.py directly executes scrape_all() once
if __name__ == '__main__':
    scrape_all()
