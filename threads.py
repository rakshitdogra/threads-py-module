#Copyright 2023 Rakshit Dogra
#Refer to Disclaimer.txt for Disclaimer.
#MIT License

#Copyright (c) 2023 Rakshit Dogra

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

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
