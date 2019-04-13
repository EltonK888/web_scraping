from bs4 import BeautifulSoup
import fpdf
import requests
import urllib

# a script used to scrape pdfs off the following website
url = r'https://thierrysans.me/CSCC09/lectures/'
source = requests.get(url).text

# instantiate a pdf to write all assigned readings to
pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
soup = BeautifulSoup(source, 'lxml')


def main():
    # finds the name of every lecture pdf and saves it to current directory
    # writes all reading links to a pdf called c01_readings.pdf
    table_notes = soup.find_all('div', class_='notes')
    table_urls = soup.find_all('div', class_='readings')
    for i in range(len(table_notes)):
        try:
            cur_files = table_notes[i].find_all('a')
            cur_urls = table_urls[i].find_all('a')
            #print(cur_urls)
        except:
            pass
        else:
            for j in range(len(cur_files)):
                cur = cur_files[j]['href']
                file_name = cur.split('/')[-1]
                urllib.request.urlretrieve(url+cur, file_name)
                print("Successfully downloaded: " + cur + " and saved as: " + file_name)
            for k in range(len(cur_urls)):
                cur_url = cur_urls[k]['href']
                pdf.write(5, cur_url+'\n', cur_url)
                print('wrote ' + cur_url + " to pdf file")
    pdf.output('c09_urls.pdf')

if __name__ == "__main__":
    main()
