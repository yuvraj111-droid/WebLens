from flask import Flask, render_template, request, Response, redirect
import json
import csv
import io

from scraper import scrape_website


app = Flask(__name__)

HISTORY_FILE = "history.json"


# ==========================================
# HISTORY
# ==========================================

def load_history():

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_history(history):

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    history = load_history()

    return render_template(
        "index.html",
        history=history
    )


# ==========================================
# SCRAPE
# ==========================================

@app.route("/scrape", methods=["POST"])
def scrape():

    url = request.form.get("url", "").strip()

    if not url:

        return render_template(
            "index.html",
            history=load_history(),
            error="Please enter a website URL."
        )

    try:

        data = scrape_website(url)

        # Save history

        history = load_history()

        history.insert(
            0,
            {
                "url": url,
                "title": data["title"]
            }
        )

        # Keep latest 10 searches

        history = history[:10]

        save_history(history)

        return render_template(
            "results.html",
            data=data
        )

    except Exception as e:

        return render_template(
            "index.html",
            history=load_history(),
            error=f"Unable to scrape this website: {e}"
        )


# ==========================================
# CLEAR HISTORY
# ==========================================

@app.route("/clear-history", methods=["POST"])
def clear_history():

    save_history([])

    return redirect("/")


# ==========================================
# DOWNLOAD CSV
# ==========================================

@app.route("/download", methods=["POST"])
def download():

    title = request.form.get("title", "")

    headings = request.form.getlist("headings")

    paragraphs = request.form.getlist("paragraphs")

    links = request.form.getlist("links")

    images = request.form.getlist("images")


    output = io.StringIO()

    writer = csv.writer(output)


    writer.writerow([
        "Type",
        "Content"
    ])


    writer.writerow([
        "Title",
        title
    ])


    for heading in headings:

        writer.writerow([
            "Heading",
            heading
        ])


    for paragraph in paragraphs:

        writer.writerow([
            "Paragraph",
            paragraph
        ])


    for link in links:

        writer.writerow([
            "Link",
            link
        ])


    for image in images:

        writer.writerow([
            "Image",
            image
        ])


    response = Response(
        output.getvalue(),
        mimetype="text/csv"
    )


    response.headers["Content-Disposition"] = (
        "attachment; filename=weblens_scraped_data.csv"
    )


    return response


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)