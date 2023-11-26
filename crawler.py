import requests
from bs4 import BeautifulSoup
import time
import os

def url_i(i):
    #Get the URL of every page
    url = "https://www.findamasters.com/masters-degrees/msc-degrees/?PG={}".format(i)
    return url

def get_MasterURLS():
    for i in range(1, 401):
        links_list = set()
        url = url_i(i)
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find all the links in the HTML
            links = soup.find_all('a', href=True)
            # Print all the links
            for link in links:
                l = link['href']
                splitted = l.split("/")
                if splitted[-1][0:2] == "?i" and len(splitted[-1].split("#")) != 2:
                    links_list.add(l)
        if len(links_list) == 15:
            with open("links.txt", 'a') as f:
                for l in links_list:
                    f.write(l+ '\n')
        time.sleep(1)

def main():

    get_MasterURLS()

    j = 0

    with open('links.txt', 'r') as file:
        # Read the content of the file
        file_content = file.readlines()
        
    for page in range(1, 401):
        folder_name = "page_{}".format(page)
        #Create a directory for the page if not exists
        if not os.path.exists(folder_name):
                os.makedirs(folder_name)
        for web in range(j, 15 + j):
            #Save HTML content for every master page
            website = "https://www.findamasters.com" + file_content[web].replace("\n", "")
            response = requests.get(website)
            #Sleep to don't saturate the server
            time.sleep(2)
            with open(folder_name + "/" + "page{}_master{}.html".format(page, web), 'a', encoding='utf-8') as file:
                file.write(response.text)
        j = page * 15
        print("Page " + str(page) + " has been completed.")
main()