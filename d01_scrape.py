from bs4 import BeautifulSoup
import requests
import urllib

# a script used to scrape pdfs off the following website
url = r'https://www.utsc.utoronto.ca/~atafliovich/cscd01/project.html'
base_url = r'https://www.utsc.utoronto.ca/~atafliovich/cscd01/'
source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')


def main():
    # finds all the lecture pdfs in the table and downloads to current directory
    table = soup.find('table')
    table_anchors = table.find_all('a')

    for i in range(len(table_anchors)):
        cur_file = table_anchors[i]['href']
        file_name = cur_file.split('/')[-1]
        urllib.request.urlretrieve(base_url+cur_file, file_name)
        print("Successfully downloaded: " + cur_file + " and saved as: " + file_name)

if __name__ == "__main__":
    main()
