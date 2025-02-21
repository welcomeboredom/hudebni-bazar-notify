import os
import yaml
import requests
from bs4 import BeautifulSoup
from pushnotifier import PushNotifier

# Configuration
# BASE_URL = "https://hudebnibazar.cz"
# URL = "http://hudebnibazar.cz/kytary/110000/"
# KEYWORDS = [
#     "chase"
# ]

# Functions
def get_links(scrape_url: str, keywords: list) -> list:

    #response = requests.get(scrape_url)

    file_path = 'hudebni_bazar_result.html'

    with open(file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    
    links = []

    print("Troubleshoot found links")
    for link in soup.find_all('a'):
        for keyword in keywords:
            if keyword in link.get('href'):
                links.append(link.get('href'))
                print(link.get('href'))

    return(links)

def check_file_and_notify(links) -> list:
    with open("links_seen.txt", "r+") as file:
        file_content = file.read()  # cursor at the end
        new_links = []
        for link in links:
            if link not in file_content:
                split_link = link.split('/')
                send_push_notification(split_link[1] ,CONFIG["hudebnibazar"]["base_url"] + link)
                file.write(link + "\n")
                new_links.append(link)
    return(new_links)
                

def send_push_notification(text: str, url: str) -> None:
    pn = PushNotifier.PushNotifier(
        CONFIG["pushnotifier"]["username"],
        CONFIG["pushnotifier"]["password"],
        CONFIG["pushnotifier"]["package"],
        CONFIG["pushnotifier"]["api_token"]
    )
    pn.send_notification(text, url)

# Main body
if __name__ == "__main__":
    # config
    with open("config.yml", "r") as config_file:
        CONFIG = yaml.load(config_file, Loader=yaml.FullLoader)

    #send_push_notification("https://www.seznam.cz")

    links = get_links(CONFIG["hudebnibazar"]["scrape_url"], CONFIG["hudebnibazar"]["keywords"])
    check_file_and_notify(links)
