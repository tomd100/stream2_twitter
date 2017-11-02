from flask import Flask
from flask import render_template, request
import os

app = Flask(__name__)
previous_searches = set()

fake_news = ["Trump Resigns", "Fruit Declares War", "Meat running Scared"]


@app.route("/")
def show_search_page():
    return render_template("search.html")


@app.route("/search")
def do_search():
    
    q = request.args.get('query')
    previous_searches.add(q)
    
    return render_template("results.html", items=fake_news)

@app.route("/previous")
def show_previous():
    return render_template("previous.html", search_terms=previous_searches)
    

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
