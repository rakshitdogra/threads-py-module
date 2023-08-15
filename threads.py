#Copyright 2023 Rakshit Dogra
#Refer to Disclaimer.txt for Disclaimer and License purposes.

import requests
from bs4 import BeautifulSoup
import re
def userpfp(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    image_meta_tag = soup.find('meta', {'name': 'twitter:image'})
    image_content = image_meta_tag.get('content')
    print(image_content)
def username(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    title_meta_tag = soup.find('meta', {'name': 'twitter:title'})
    title_content = title_meta_tag.get('content')
    pattern = r'\((.*?)\)'  # Regular expression pattern to match text within parentheses
    matches = re.findall(pattern, title_content)
    for match in matches:
        print(match.strip())
def name(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    title_meta_tag = soup.find('meta', {'name': 'twitter:title'})
    title_content = title_meta_tag.get('content')
    pattern = r'^(.*?)\('  # Regular expression pattern to match text before opening parenthesis
    matches = re.findall(pattern, title_content)
    for match in matches:
        print(match.strip())  # Use strip to remove any leading/trailing whitespace
def description(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    description_meta_tag = soup.find('meta', {'name': 'twitter:description'})
    description_content = description_meta_tag.get('content')
    print(description_content)
