from selenium import webdriver
from selenium.webdriver.common.by import By
from base import ask

driver = webdriver.Chrome()

def click_link(url, name):
    driver.get(url)
    button = driver.find_element(By.LINK_TEXT, name)
    button.click()

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
def enter_input(url, name):
    pass

def save(details, type):
    pass

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
    prompt = f"Can I find {objective} in this {state}. Yes or No?"
    return reply
