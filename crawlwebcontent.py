import os
import requests
from bs4 import BeautifulSoup

# Set the URL of the website you want to crawl
url = 'https://www.example.com/'

# Set the directory where you want to save the pages
directory = '/path/to/local/folder/'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Send a request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Loop through each link and save its contents into a file
for link in links:
    # Get the URL of the link
    link_url = link.get('href')

    # Send a request to the link URL and get the HTML content
    response = requests.get(link_url)
    html_content = response.content

    # Create a file name based on the link URL
    file_name = link_url.split('/')[-1]

    # Save the contents of the link into a file in the local directory
    with open(os.path.join(directory, file_name), 'wb') as f:
        f.write(html_content)
