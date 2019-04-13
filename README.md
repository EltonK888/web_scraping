# Web Scraping
Used python to scrape lecture content off course websites

The following websites were used to scrape data:

**CSCC01** - Introduction to Software Engineering: https://thierrysans.me/CSCC01/  
**CSCC09** - Programming on the Web: https://thierrysans.me/CSCC09/  
**CSCD01** - Engineering Large Software Systems: https://www.utsc.utoronto.ca/~atafliovich/cscd01/index.html   

## Dependencies:
- `fpdf`  For writing to a pdf
- `BeautifulSoup`  Used to scrape the web
- `requests`  Requests library
- `lxml`  HTML parser


## To install dependencies:  

- For `fdpf`:   
~~~~
pip install fpdf
~~~~
- For `BeautifulSoup`:   
~~~~
pip install beautifulsoup4
~~~~
- For `requests`:    
~~~~
pip install requests
~~~~
- For `lxml`:    
~~~~
pip install lxml
~~~~

## To run:  

~~~~
python3 <name_of_file>.py
~~~~

This will save all lecture content to the working directory  
Reading urls will be copied into a pdf file
