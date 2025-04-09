from flask import Flask, render_template

app = Flask(__name__)


#1 App route hello world
@app.route("/")
def hello_world():
    return "<p>Hello, World! Halo cantik<p>"

#2 App Route Halaman Pertama
@app.route('/about/')
def about():
    return "<p>saya orang soppeng<p>"

#3 App Route Halaman HTML Flaskland
@app.route("/page/keren/")
def keren():
    return render_template("keren.html")

#4 App Route Halaman HTML Full
@app.route("/full/")
def full():
    return render_template("full.html")

#5 App Route Dinamis
@app.route('/nama/<string:nama>')
def getnama(nama):
    return "nama anda adalah {}".format(nama)


#6 App route variabel global
app_name = "My Flask App"  # Variabel global

@app.route('/')
def home():
    return f"Welcome to {app_name}!"

#7 App route variabel Lokal
@app.route("/lokal/")
def data():
    user = {"name": "Ali", "age": 25, "city": "Jakarta"}
    return render_template('lokal.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)