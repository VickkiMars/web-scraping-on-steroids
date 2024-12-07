from bs4 import BeautifulSoup
import requests
from utils import determine_type, final_answer, action, click_link, what_next
from base import ask

action_space = []

def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        html_content = soup.prettify()
    else:
        print(f"Failed to fetch webpage {url}. Status code: {response.status_code}")
    return html_content

def extract(url):
    features = ask(web=get_html(url=url))
    # links = features["links"]
    # buttons = features["buttons"]
    # text = features["text"]
    # input_fields = features["input_fields"]
    # tables = features["tables"]
    return features

def recurr(query, links, url):
    features = extract(url)
    response = what_next(query, features)
    if response == "Yes":
        final_answer(features, query)
    else:
        features  = [features["links"], features["input_fields"],features["buttons"]]
        type_ = determine_type(features)
        if "link" in type_:
            type_ == "links"
        elif "input" in type_:
            type_ = "input_fields"
        else: type_ = "buttons"
        reply = action(type_, query, features[response])

        if type_ == "links":
            response = click_link(url, reply)
        elif type_ == "input":
            response = input_text(url, reply, "text")
        else:
            response = click_button(url, reply)

        html = get_html(response)
        response = what_next(query, html)
        if response == "Yes":
            features = extract(url)
        else:
            recurr(links, url)
    


