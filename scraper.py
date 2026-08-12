import requests

from bs4 import BeautifulSoup

from urllib.parse import urljoin


def scrape_website(url):

    # ==========================================
    # REQUEST
    # ==========================================

    headers = {

        "User-Agent":
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/151.0 Safari/537.36"

    }


    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )


    response.raise_for_status()


    # ==========================================
    # PARSE HTML
    # ==========================================

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )


    # ==========================================
    # TITLE
    # ==========================================

    if soup.title:

        title = soup.title.get_text(
            strip=True
        )

    else:

        title = "No title found"


    # ==========================================
    # HEADINGS
    # ==========================================

    headings = []


    for tag in soup.find_all(
        ["h1", "h2", "h3", "h4", "h5", "h6"]
    ):

        text = tag.get_text(
            " ",
            strip=True
        )

        if text:

            headings.append(text)


    # ==========================================
    # PARAGRAPHS
    # ==========================================

    paragraphs = []


    for tag in soup.find_all("p"):

        text = tag.get_text(
            " ",
            strip=True
        )

        if text:

            paragraphs.append(text)


    # ==========================================
    # LINKS
    # ==========================================

    links = []


    for tag in soup.find_all("a"):

        href = tag.get("href")

        if href:

            full_url = urljoin(
                url,
                href
            )

            links.append(full_url)


    # Remove duplicate links

    links = list(
        dict.fromkeys(links)
    )


    # ==========================================
    # IMAGES
    # ==========================================

    images = []


    for tag in soup.find_all("img"):

        src = tag.get("src")

        if src:

            full_url = urljoin(
                url,
                src
            )

            images.append(full_url)


    # Remove duplicate images

    images = list(
        dict.fromkeys(images)
    )


    # ==========================================
    # WORD COUNT
    # ==========================================

    word_count = 0


    for paragraph in paragraphs:

        word_count += len(
            paragraph.split()
        )


    # ==========================================
    # STATISTICS
    # ==========================================

    statistics = {

        "headings": len(headings),

        "paragraphs": len(paragraphs),

        "links": len(links),

        "images": len(images),

        "words": word_count

    }


    # ==========================================
    # RETURN
    # ==========================================

    return {

        "title": title,

        "url": url,

        "headings": headings,

        "paragraphs": paragraphs,

        "links": links,

        "images": images,

        "statistics": statistics

    }