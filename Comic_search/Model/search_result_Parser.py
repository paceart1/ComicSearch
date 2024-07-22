from bs4 import BeautifulSoup

class Parser:
    def __init__(self):
        pass

    def __strip_id(self, link):
        lead = "https://www.ebay.com/itm/"
        if lead not in link:
            raise Exception("Item ID could not be stripped from link.")
        s = len(lead)
        e = link.find('?')
        id = link[s:e]
        if lead + id + "?" not in link:
            raise Exception("Id could not be validated")
        return id

    def parse_data(self, data):
        # Get postings
        html_text = BeautifulSoup(data, "html.parser")

        #Nothing found
        null_found = html_text.find(attrs={'class':'srp-save-null-search'})
        if null_found:
            return []

        main_section = html_text.find(attrs={'id':'mainContent'})
        result_container = main_section.find(attrs={'id':'srp-river-results'})
        listings = result_container.find_all('li', class_='s-item', attrs={'data-viewport':True})

        results = []
        #Convert to python
        for l in listings:
            title = l.find(attrs={'class':'s-item__title'}).findChild('span').text
            link = l.find(attrs={'class':'s-item__link'})['href']
            item_id = self.__strip_id(link)
            shipping = l.find(attrs={'class':'s-item__shipping'})
            price = l.find(attrs={'class':'s-item__price'}).text
            time_remaining = l.find(attrs={'class':'s-item__time-left'})
            end_time = l.find(attrs={'class':'s-item__time-end'})
            img_url = l.find(attrs={'class':'s-item__image-wrapper'}).findChild('img')['src']

            if time_remaining:
                time_remaining = time_remaining.text
            if end_time:
                end_time = end_time.text
            if shipping:
                shipping = shipping.text.replace('+', '')

            item = {"item_id": item_id, "title": title, "link": link, "price": price, "shipping": shipping,
                    "end_time": end_time ,"rem_time": time_remaining, "img_url":img_url}
            results.append(item)
        return results

if __name__ == "__main__":
    pass
    #print("** Testing Parser **")

    #results = parse_data(text)
    #for r in results:
    #    print(r)

