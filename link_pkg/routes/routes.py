import requests,json
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
from flask import render_template,redirect,request
from link_pkg import app

@app.route("/",methods=["GET","POST"])
def home():
   if request.method == "GET":
      return render_template("home.html")
   else:
      try:
         url = request.form.get("url")
         webpage = requests.get(url).content
         soup = BeautifulSoup(webpage,"html.parser")
         links = [link.attrs["href"] for link in soup.find_all("a") if "href" in link.attrs]
         return render_template("links.html",webpage=url,links=links)
      except ConnectionError as e:
         return render_template("links.html",error=e)
