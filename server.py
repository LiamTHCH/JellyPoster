from flask import Flask, render_template
import time
from Jellyfin import JellyFin

Chehtelekoum = JellyFin("https://jellyfin.chehtelekoum.de","bacbff08a18a44c6b29f1da016f02fa0")

print(Chehtelekoum.get_PLAYING_device("89.247.8.169"))



app = Flask(__name__)

# Fonction qui retourne l'URL de l'image
def get_image_url():
    image = ""
    if (Chehtelekoum.get_PLAYING_device("89.247.8.169")) is not None:
        image = Chehtelekoum.get_PLAYING_device("89.247.8.169")[-1]
    else:
        image = "https://static-00.iconduck.com/assets.00/jellyfin-icon-1024x1024-udvadsvh.png"
    return image


@app.route('/')
def index():
    return render_template("index.html", url=get_image_url())



if __name__ == '__main__':
    app.run(debug=True)
