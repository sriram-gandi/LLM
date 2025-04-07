from bs4 import BeautifulSoup

def parser(response):
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    text = soup.body.get_text(separator="\n", strip=True)
    return text,title