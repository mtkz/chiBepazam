import requests
from bs4 import BeautifulSoup

import contants


class Crawler:

    def data_getter(self, url):
        try:
            page = requests.get(url)
        except:
            print('internet is not connect :(')
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def data_finder(self, soup):
        lists = soup.select('ol li')
        return lists

    def data_exported(self, lists):
        with open('data.txt', 'w+', encoding='utf-8') as data:
            for list in lists:
                data.write(list.get_text() + "\n")
        data.close()


def main():
    crawler = Crawler()
    main_page = crawler.data_getter(contants.WEBSITE_MUST_TO_CRAWL)

    finded_data = crawler.data_finder(main_page)
    crawler.data_exported(finded_data)


main()
