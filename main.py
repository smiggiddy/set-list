from setlist import SetList
from users import Users
from forms import CreateSetList
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from requests.api import post, request
from flask_ckeditor import CKEditor, CKEditorField


# ------ Flask ------ #
app = Flask(__name__)
Bootstrap(app)

mikeset = SetList('Sankofa')
user1 = Users(mikeset)

mikeset.add_songs(
    set_order=1,
    song_title='Rock With You',
    song_artist='Michael Jackson',
    song_url='http://www.youtube.com/michaeljackson',
    song_bpm=94)

print(user1.setlist.set_list[0])





@app.route('/')
def home():
    """
    Serve up the home page
    """

    return '<h1> Setlist Home </h1>'



if __name__ == "__main__":
    app.run(debug=True)