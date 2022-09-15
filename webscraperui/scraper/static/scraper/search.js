const url = new URL(location.href);
const urlsearchparams = new URLSearchParams(url.search);
const searchBar = document.getElementById("search-bar");
searchBar.setAttribute("value", urlsearchparams.get("q"));

const prevPage = document.getElementById("prev-page");
const nextPage = document.getElementById("next-page");
var targetPage;

if (!urlsearchparams.get("pg") || parseInt(urlsearchparams.get("pg")) == 0) {
    prevPage.style.display = "none";
    targetPage = 0;
}

if (urlsearchparams.get("pg")) {
    targetPage = parseInt(urlsearchparams.get("pg"));
}

function updatePage() {
    // console.log("updatePage() called");
    
    if (!urlsearchparams.get("pg")) {
        urlsearchparams.append("pg", targetPage);
    } else {
        urlsearchparams.set("pg", targetPage);
    }

    window.location.search = urlsearchparams;
}

prevPage.onclick = () => {
    targetPage--;
    updatePage();
}

nextPage.onclick = () => {
    targetPage++;
    updatePage();
}

// i know. code's messy af but get's the job done and that's what matters.