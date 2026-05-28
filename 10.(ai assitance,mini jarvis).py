import os
import webbrowser
import random
import datetime
import requests
from bs4 import BeautifulSoup
def scrape_jokes():
    global all_jokes
    all_jokes = []
    # for page in range(1):
    url = f"https://www.thepioneerwoman.com/home-lifestyle/a35617884/best-dad-jokes/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    jokes = soup.find_all("li")
    for joke in jokes:
        item = joke.get("data-node-id")
        if item and item.startswith("9."):
            all_jokes.append(joke.get_text(strip=True))
    # print(all_jokes)
    return all_jokes
while True:
    cmd = input("Enter your command: ").lower()
    if(cmd == "time"):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(now)
    elif(cmd == "date"):
        print(datetime.datetime.now().date())
    elif (cmd.startswith("open ")):
        opened = cmd.replace("open ","")
        webbrowser.open(f"https://www.{opened}.com/")
    elif(cmd.startswith("search ")):
        search = cmd.replace("search ","")
        webbrowser.open(f"https://www.google.com/search?q={search}")
    elif(cmd == "joke"):
        scrape_jokes()
        joke = random.choice(all_jokes)
        print(joke)
    elif(cmd=="exit"):
        break
    with open("history.txt","a") as f:
            f.write(cmd + "\n")



