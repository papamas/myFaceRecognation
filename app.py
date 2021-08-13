from flask import Flask
import views

app = Flask(__name__)

# url
app.add_url_rule('/base', 'base', views.base)
app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/face', 'face', views.face)
app.add_url_rule('/face/encoding', 'encoding', views.encoding, methods=['GET', 'POST'])

#
if __name__ == "__main__":
    app.run(debug=True)
