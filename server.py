from flask import Flask, render_template, redirect
from database import db
import scrape as sj
import threading

app = Flask(__name__)

# Configure your app, move configuration to a separate file if necessary

@app.route('/', methods=["GET"])
def home():
    try:
        content = sj.get_content()
        if content is None:
            return "FETCHING DATA, PLEASE TRY AGAIN LATER!"
        return render_template('index.html', content=content)
    except Exception as e:
        # Log the exception or handle it appropriately
        return f"An error occurred: {str(e)}"

@app.route('/readmore/<source>', methods=["GET"])
def readmore(source):
    try:
        content = sj.get_content_for_source(source)
        if content is None:
            return redirect('/404')
        return render_template('readmore.html', content=content)
    except Exception as e:
        # Log the exception or handle it appropriately
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    # Start ScrapeJob as a background job in a new thread
    t1 = threading.Thread(target=sj.scrape_start)
    t1.daemon = True
    t1.start()

    # Start Flask Server
    app.run()
