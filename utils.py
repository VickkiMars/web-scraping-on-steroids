from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from base import ask
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


driver = webdriver.Chrome()

def click(type: str, url: str, name: str):
    """
    Function to click on a button
    
    :param type: The ID or other locator of the button or link. (unexact)
    :param url: The URL of the website.
    :param name: The ID or other locator of the button or link (exact)
    """
    try:
        driver.get(url)
        button = driver.find_element(By.LINK_TEXT, name)
        button.click()
        page_source = driver.page_source
        return page_source
    except Exception as e:
        print(f"An error occured while clicking the {name} link in {url}:\n{e}")

def enter_input(url: str, input_text: str, input_id: str, button_id: str=None):
    """
    Function to enter input into an input field in a website
    
    :param url: The URL of the website.
    :param input_text: The text to search for
    :param input_id: The ID or other locator of the input field
    :param button_id: The ID or other locator of the button to be pressed
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver.get(url)

    input_field = driver.find_element(By.ID, input_id)
    input_field.send_keys(input_text)

    if button_id:
        input_button = driver.find_element(By.ID, button_id)
        input_button.click()
    else:
        input_field.send_keys(Keys.RETURN)

    driver.implicitly_wait(10)
    print("Waiting for results...")
    return driver.page_source


message = [
            {
                "role": "system",
                "content": "{0}"
            },
            {
                "role": "user",
                "content": "{1}"
            }
        ]

def get_url(query:str) -> str:
    content = "You are an expert at solving problems by giving direct answers."
    prompt = "Extract the url from this statement: {query}"
    message = message.format(content, prompt)
    response = ask(message=message, mnt=20)

def action(type, action, samples):
    content = "You are an expert at solving problems with direct answers"

    if "button" in type:
        query = f"The available buttons on a website have the following text {samples}, i need to {action}. Which button best suits my action? Reply only with the button name."
        
        prompt = message.format(content, query)
        reply = ask(message=prompt, mnt=10)

    elif "link" in type:
        query = f"The available links on a website have the following text {samples}, i need to {action}. Which link best suits my action? Reply only with the link."

        prompt = message.format(content, query)
        reply = ask(message=prompt, mnt=10) 

    elif "input" in type:
        query = f"The available input fields on a website have the following placeholders {samples}, i need to {action}. Which input field best suits my action? Reply only with the input field."
        
        prompt = message.format(content, query)
        reply = ask(message=prompt, mnt=10)
    return reply

def save_table(table):
    headers = table["headers"]
    rows = table["rows"]
    filename = "table.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Data has been saved to {filename}")

    pass

def determine_type(features, query):
    content = "You are an expert at solving problems with direct answers"
    query = f"Given the following features {features}, which of them will best solve this problem: {query}. Answer with either 'links', 'buttons', or 'input_field'. "

    prompt = message.format(content, query)
    reply = ask(message=prompt, mnt=10)
    return reply

def final_answer(json, query):
    content = "You are an expert at solving problems with direct answers"
    prompt = f"from the following json structure {json}, answer this query: {query}"

    prompt = message.format(content, query)
    reply = ask(message=prompt, mnt=10)
    return reply

def what_next(objective, state):
    content = "You are an expert at solving problems with direct answers"
    prompt = f"Can I find {objective} in this {state}. Yes or No?"

    prompt = message.format(content, prompt)
    reply = ask(message=prompt, mnt=3)
    return reply
