const url = new URL(location.href);
const urlsearchparams = new URLSearchParams(url.search);
const searchbar = document.getElementById("search-bar");
searchbar.setAttribute("value", urlsearchparams.get("q"));