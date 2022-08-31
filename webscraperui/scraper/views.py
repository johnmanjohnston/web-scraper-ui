from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
import dotenv
import os

dotenv.load_dotenv()

# Create your views here.
def index(request):
    # return HttpResponse("<h1>stuff's working</h1>")
    return render(request, "scraper/index.html")


def search_page(request):
    if not request.GET.get("q"):
        return HttpResponseRedirect("/")

    q = request.GET.get("q")

    searchhtml = "";
    if q == "dev:norequest":
        searchhtml = "<h1>Not requesting</h1>"
        return render(request, "scraper/search.html", {
        "searchcontent": searchhtml
    })

    extraclasses = ""

    headers = {
        "apikey": os.getenv("ZENSERP_KEY")
    }

    params = (
        ("q", q),
        ("num", "99")
    )

    response = requests.get("https://app.zenserp.com/api/v2/search", headers=headers, params=params)
    data = json.loads(response.text)

    for result in data["organic"]:
        try:
            url = result["url"]
        except:
            continue

        try:
            pagetitle = result["title"]
        except KeyError:
            pagetitle = url

        if pagetitle == "":
            pagetitle = url

        try:
            desc = result["description"]
        except:
            desc = ""

        if "#" in url:
            extraclasses = "subpage"
        

        searchhtml += f"""
            <div class="res-title {extraclasses}"> {pagetitle} </div>
            <a href="{url}" class="res-link {extraclasses}">{url}</a>
            <div class="res-desc">{desc}</div>
            <br> <br>
        """

    return render(request, "scraper/search.html", {
        "searchcontent": searchhtml
    })