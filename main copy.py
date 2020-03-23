from flask import Flask , request, render_template

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

@app.rout("/sub_catalogs/<name>")
def subcatalog(name):
    return render_template('sub_catalogs.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=4000)
