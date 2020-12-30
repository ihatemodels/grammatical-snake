import requests
import time
import csv
from bs4 import BeautifulSoup


def scraper():
    """ One time run script to scrape dictionary.calipers.bg
        for marketing and internet based terminus and definition.
        The output will be stored as .csv for later usage """

    with open('callipers-scrape.csv', 'w+', encoding="utf-8") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Bulgarian', 'English', 'Definition'])

    print('Csv file generated...\n')

    req = requests.get(
        'http://dictionary.calipers.bg/bg/%D0%B2%D1%81%D0%B8%D1%87%D0%BA%D0%B8-%D0%B4%D1%83%D0%BC%D0%B8/')
    links_soup = BeautifulSoup(req.content, 'html.parser').find_all('a', href=True)
    urls = []
    for pos, link in enumerate(links_soup, start=1):

        if pos > 36:
            if link['href'][0:2] == '..':
                if pos % 2 == 0:
                    urls.append(link['href'][2:])

    for url in urls:
        current = 'http://dictionary.calipers.bg/' + url
        print('Current url: ', current)
        single = requests.get(current)
        single_soup = BeautifulSoup(single.content, 'html5lib').find(class_='RightContent')
        bulgarian_name = single_soup.find(class_='TitleLinkBg').get_text()
        english_name = single_soup.find(class_='TitleLinkEn').get_text()
        single_soup.find('div', id=True).extract()
        single_soup.find('div', class_=True).extract()
        single_soup.find(class_='TitleLinkBg').extract()
        single_soup.find(class_='TitleLinkEn').extract()
        termin_definition = single_soup.text
        stack = [bulgarian_name, english_name, termin_definition]

        print('Bg: {}\nEn: {}'.format(bulgarian_name, english_name))

        with open('callipers-scrape.csv', 'a', newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(stack)

        print('Waiting 20 seconds to avoid too many requests based problems...')
        time.sleep(20)


if __name__ == "__main__":
    scraper()
