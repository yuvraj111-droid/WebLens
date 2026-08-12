const form = document.getElementById("scrape-form");

const button = document.getElementById("scrape-button");


if (form) {

    form.addEventListener("submit", function () {

        button.textContent = "Scraping...";

        button.disabled = true;

    });

}