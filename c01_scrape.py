import urllib
import fpdf
import requests
from bs4 import BeautifulSoup

# a script used to scrape pdfs off the following website
URL = r'https://thierrysans.me/CSCC01/lectures/'
SOURCE = requests.get(URL).text

# instantiate a pdf to write all assigned readings to
PDF = fpdf.FPDF(format='letter')
PDF.add_page()
PDF.set_font("Arial", size=12)
SOUP = BeautifulSoup(SOURCE, 'lxml')


def main():
    '''
    Finds the name of every lecture pdf and saves it to current directory
    writes all reading links to a pdf called c01_readings.pdf
    '''
    table_notes = SOUP.find_all('div', class_='notes')
    table_urls = SOUP.find_all('div', class_='readings')
    for i in range(len(table_notes)):
        try:
            cur_files = table_notes[i].find_all('a')
            cur_urls = table_urls[i].find_all('a')
        except:
            pass
        else:
            for j in range(len(cur_files)):
                cur = cur_files[j]['href']
                file_name = cur.split('/')[-1]
                urllib.request.urlretrieve(URL+cur, file_name)
                print("Successfully downloaded: " + cur + " and saved as: " + file_name)
            for k in range(len(cur_urls)):
                cur_url = cur_urls[k]['href']
                PDF.write(5, cur_url+'\n', cur_url)
                print('wrote ' + cur_url + " to pdf file")
    PDF.output('c01_urls.pdf')

if __name__ == "__main__":
    main()
