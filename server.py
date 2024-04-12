from flask import Flask, render_template
import time
from Jellyfin import JellyFin
import os


Jelly = JellyFin(os.environ.get("JELLYFIN_URL"), os.environ.get("JELLYFIN_API_KEY"))
clientip = os.environ.get("CLIENT_IP")


app = Flask(__name__)


def get_image_url():
    image = ""
    if (Jelly.get_PLAYING_device(clientip)) is not None:
        image = Jelly.get_PLAYING_device(clientip)[-1]
    else:
        image = "https://static-00.iconduck.com/assets.00/jellyfin-icon-1024x1024-udvadsvh.png"
    return image


@app.route('/')
def index():
    return render_template("index.html", url=get_image_url())



if __name__ == '__main__':
    app.run(debug=True)
