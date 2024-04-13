from bs4 import BeautifulSoup, Tag
import requests

def text_bodies(items: list[dict]):
    texts: list[str] = []
    doc_index: int = 0

    for item in items:
        text: str = ""
        try:
            html: str = requests.get(item.get("link", "")).text
            text_paragraphs: list[Tag] = BeautifulSoup(html, "html.parser").find(name="div", class_="texto--single").findChildren("p")

            for p in text_paragraphs:
                text += p.text
            texts.append(text)
        except:
            text += "Error fetching URL!"
        
        print("Document " + str(doc_index) + " was processed")
        doc_index += 1
    
    
    return texts