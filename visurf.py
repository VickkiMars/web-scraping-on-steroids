from bs4 import BeautifulSoup
import requests
from utils import determine_type, final_answer, action, what_next, enter_input, click
from base import ask
from typing import Any, Union

action_space = []

def get_html(url: str) -> Union[dict, str]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        html_content = soup.prettify()
    else:
        print(f"Failed to fetch webpage {url}. Status code: {response.status_code}")
    return html_content

def extract(url:str) -> Union[dict, str]:
    features = ask(web=get_html(url=url))
    # links = features["links"]
    # buttons = features["buttons"]
    # text = features["text"]
    # input_fields = features["input_fields"]
    # tables = features["tables"]
    return features

def recurr(query: str, searchable:str, url:str) -> Any:
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
            response = click(type_, url, reply)
        elif type_ == "input":
            response = enter_input(url, reply, "text")
        else:
            response = click(url, reply)

        html = get_html(response)
        response = what_next(query, html)
        if response == "Yes":
            features = extract(url)
        else:
            recurr(query, url)
            
    


