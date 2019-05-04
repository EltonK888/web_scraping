import urllib
import requests
from bs4 import BeautifulSoup

# a script used to scrape pdfs off the following website
URL = r'http://www.utsc.utoronto.ca/~bretscher/a67/lectures.html'
SOURCE = requests.get(URL).text
SOUP = BeautifulSoup(SOURCE, 'lxml')


def main():
    '''
    Downloads all lecture pdfs into the working directory
    from the website specified by URL
    '''
    table = SOUP.find('table')
    table_anchors = table.find_all('a')
    for i in range(len(table_anchors)):
        cur_file = table_anchors[i]['href']
        file_name = cur_file.split('/')[-1]
        try:
            urllib.request.urlretrieve(cur_file, file_name)
            print("Successfully downloaded: " + cur_file + " and saved as: " + file_name)
        except:
            print("Failed to download: " + cur_file)

if __name__ == "__main__":
    main()
