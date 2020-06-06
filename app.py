from flask import Flask, render_template
import os

app = Flask(__name__)

# Data

data = {
    "NW Corner": [
        "https://businessjargons.com/north-west-corner-rule.html",
        "https://drive.google.com/file/d/17W_foCU1WNwrAs1cUVr_XIXV9ULOwmo8/view?usp=drivesdk",
        "https://drive.google.com/file/d/17Wcrq4G779EXvEbAyTtiLumSUHvCYU5v/view?usp=drivesdk",
    ],
    "Least Cost Method": [
        "https://drive.google.com/file/d/186F3tVex_3JK7-JsUfPQ7w6Y6NWuMwD4/view?usp=drivesdk",
        "https://drive.google.com/file/d/186nbyN84AEd_DxMwjZewSKManCVqPHNe/view?usp=drivesdk",
        "https://drive.google.com/file/d/18AdaQo-45HYU1Ef098lcVkKr5rvWo8Bj/view?usp=drivesdk",
    ],
    "Row Minima": [
        "https://drive.google.com/file/d/19ilg1NzVjwSJyE5yvY87rrgjz05SqIuY/view?usp=drivesdk"
    ],
    "VAM": ["https://drive.google.com/open?id=1eBpko100vkNUImBkBRg1ySuDrYuZ_lug"],
    "MODI Method": [
        "https://drive.google.com/open?id=11FRrUdbLpi21Et2bZmOQZ-rgEy-7L9AW",
        "https://drive.google.com/open?id=11a9S_yN-p4mRHoAb8UI-yizEGlszp5Qm",
        "https://drive.google.com/open?id=14suVA6V5WSPV2FekejKodcUYRLshnjH-",
        "https://drive.google.com/open?id=14trYi8U-Gz26f5YO0D6K66476wQCAU1a",
    ],
    "Degenaracy Procedure": [
        "https://drive.google.com/open?id=17lbg5s-gQvfUg4iw6hEKMPvqbRD7P7ht",
        "https://drive.google.com/open?id=18BQmqPD9x-tprc-zh6kRR7KfXi5_6OUv",
    ],
    "Unbalanced Transportation Problem": [
        "https://drive.google.com/open?id=19O6jB-5qZSw-AVbs_b8Mo73oHBXI9T6l"
    ],
    "Assignment Problem": [
        "https://drive.google.com/open?id=19_2WDM8zNxN_h94IDr89dU48ZdBYHCQC"
    ],
    "Hungarian Method": [
        "https://drive.google.com/drive/folders/1BeFZStlZyb1KrWUD07FIi40I4p20hQbE?usp=sharing"
    ],
    "Prohibited Assignment Problem": [
        "https://drive.google.com/open?id=1ENB8Gi_2cTtmwa-NRG9fdYIVFsgyTDvW"
    ],
    "Travelling Salesman Problem": [
        "https://drive.google.com/open?id=1EYeMDCjYTwIvwp1JwAb34TzNNmGht2Lv"
    ],
    "Duality Theory": [
        "https://drive.google.com/open?id=1FYRC37BZgwvhHYiWt3ToVf9GHm55gI8x",
        "https://drive.google.com/open?id=1G2YaVm-p9pY6JSRIPLCQu3dboOo7e9tj",
    ],
    "Dual Problem using BIG-M": [
        "https://drive.google.com/open?id=1I5VsvceS0OKyAuu8cM65Okjz0ndbrDZs"
    ],
}


@app.route("/")
def index():
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
