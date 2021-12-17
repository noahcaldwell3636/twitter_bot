from bs4 import BeautifulSoup
import requests
import sitemap_tester.http_helper as http_helper

# 'https://www.noahcaldwell.io/sitemap.xml'
def urls_from_sitemap(sitemap_url: str):
    html_text = requests.get(sitemap_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    urls = list(soup.find_all('loc'))
    formatted_urls = []
    for url in urls:
        url = str(url).replace('<loc>', '').replace('</loc>', '')
        formatted_urls.append(url)
    return formatted_urls
    
def print_url_response(url: str, response_code: http_helper.ResponseCode):
    print(f"\n \n checking http response for {url}"
    f"\n {response_code.STATUS_CODE}, {response_code.NAME}"
    f"\n -------------------DEFINTION--------------------"
    f"\n {response_code.GROUPING}: {response_code.DESCRIPTION}"
    f"\n" #new lines at the beginning and end to create double
    # spaces between responses in the cases of this method being\
    # called in a for loop      
    )
        

def get_all_request_codes(urls: list, verbose=False):
    # parse each url (found in the sitemap using 'urls_from_sitemap')
    for url in urls: 
        # get http status code 
        status_code = requests.get(url).status_code
        # aquire info related to status code with http_helper
        response_code = http_helper.ResponseCode(status_code)
        # if verbose parameter
        if verbose: 
            print_url_response(response_code=response_code, url=url)
        else: # not verbose (parameter)
            print(url, response_code.STATUS_CODE)
            if response_code.IS_CRITICAL: print_url_response(
                response_code=response_code,
                url=url,
            )


#print(soup.prettify())
#jobs = soup.get()

if __name__ == '__main__':
    request_codes = urls_from_sitemap('https://www.noahcaldwell.io/sitemap.xml')
    get_all_request_codes(request_codes, verbose=False)