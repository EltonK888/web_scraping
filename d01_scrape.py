import urllib
from bs4 import BeautifulSoup
import requests

# a script used to scrape pdfs off the following website
URL = r'https://www.utsc.utoronto.ca/~atafliovich/cscd01/lectures.html'
BASE_URL = r'https://www.utsc.utoronto.ca/~atafliovich/cscd01/'
SOURCE = requests.get(URL).text

SOUP = BeautifulSoup(SOURCE, 'lxml')


def main():
    '''
    Finds all the lecture pdfs in the table and downloads to current directory
    '''
    table = SOUP.find('table')
    table_anchors = table.find_all('a')

    for i in range(len(table_anchors)):
        cur_file = table_anchors[i]['href']
        file_name = cur_file.split('/')[-1]
        urllib.request.urlretrieve(BASE_URL+cur_file, file_name)
        print("Successfully downloaded: " + cur_file + " and saved as: " + file_name)

if __name__ == "__main__":
    main()
