#! /usr/bin/env python3

'''
searchpypi.py - Open browser with all top search results in new tabs
for PyPI

https://pypi.org/search/?q=<SEARCH_QUERY> - user will supply SEARCH_QUERY
'''
import webbrowser, sys, bs4, requests, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)

FNAME = sys.argv[0]
USAGE_TXT = f'usage: python3 {FNAME} search_term'
URL = 'https://pypi.org/search/?q='

logging.debug('Start of program')
# Read command line arguments from sys.argv.
if len(sys.argv) < 2:
    print(USAGE_TXT, file=sys.stderr)
    sys.exit(1)
search_query = sys.argv[1:]

# TODO: Fetch the search result page with the requests module.
print('Searching...')
pypi_res = requests.get(URL + ' '.join(search_query))
pypi_res.raise_for_status()

# TODO: Find the links to each search result.
results_soup = bs4.BeautifulSoup(pypi_res.text, 'lxml')
links_elems = results_soup.select('.package-snippet')
logging.debug(f'Links found\n{links_elems}')

# TODO: Call the webbrowser.open() function to open the web browser.
num_open = min(5, len(links_elems))     # At most, open 5 tabs.
for i in range(num_open):
    url_to_open = 'https://pypi.org' + links_elems[i].get('href')
    print(f'Opening {url_to_open}..')
    webbrowser.open(url_to_open)

