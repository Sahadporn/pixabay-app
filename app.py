from quart import Quart, render_template, request
import requests

app = Quart(__name__, template_folder='template')

URL = "https://pixabay.com/api/?key="

@app.route("/", methods=["GET", "POST"])
async def home():
    if request.method == "POST":
        form = await request.form
        api_url = URL+process.env.API_KEY+"&q="+form['query']+"&image_type=photo&pretty=true"
        res = requests.get(api_url)
        imgs = res.json()["hits"]
        return await render_template("home.html", imgs=imgs)
        
    return await render_template("home.html")

if __name__ == "__main__":
    app.run(debug=False, port=8000)
