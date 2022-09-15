from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
import json
import dotenv
import os

dotenv.load_dotenv()

# Create your views here.
def index(request):
    return render(request, "scraper/index.html")


def search_page(request):
    if not request.GET.get("q"):
        return HttpResponseRedirect("/")

    if not request.GET.get("pg"):
        pagecount = 0
    else:
        pagecount = int(request.GET.get("pg"))
    
    q = request.GET.get("q")
    print(pagecount)

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
        ("num", "100"),
        ("start", str(int(pagecount) * 100)) 
    )

    response = requests.get("https://app.zenserp.com/api/v2/search", headers=headers, params=params)
    data = json.loads(response.text)

    emptyresulthtml = f"<h1 style='font-weight: 300'>Couldn't find anything about \"{q}\"</h1>"

    if "organic" in data:
        validsearch = True
    else:
        validsearch = False

    if validsearch == False:
        searchhtml = emptyresulthtml

        return render(request, "scraper/search.html", {
        "searchcontent": searchhtml
    })

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

    if searchhtml.strip() == "":
        return render(request, "scraper/search.html", {
            "searchcontent": f"<h1>Couldn't find more information on \"{q}\"</h1>"
        })

    return render(request, "scraper/search.html", {
        "searchcontent": searchhtml
    })