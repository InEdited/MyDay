from flask import Flask , request, render_template
import DBUtil as db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/catalog/<name>")
def catalog(name):    
    return render_template('catalog.html')

@app.route("/sub_catalogs/<name>")
def subcatalog(name):
    print(name)
    stuff = db.get_sub_catalogs(name)
    return render_template('sub_catalogs.html', things = stuff)

@app.route("/sub_catalogs/services/<name>")
def services(name):
    print(name)
    stuff = db.get_services(name)
    return render_template('services.html', things = stuff)


@app.route("/debug")
def debug():
    db.get_services("Shops")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=4000)

