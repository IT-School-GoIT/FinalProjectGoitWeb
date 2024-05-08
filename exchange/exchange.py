import requests
from bs4 import BeautifulSoup
from .models import Currencies


def clear_currency_database():
    """
    The clear_currency_database function deletes all the objects in the Currencies database.
    This is useful for when you want to update your currency database with new data.
    
    :return: Nothing
    :doc-author: Trelent
    """
    Currencies.objects.all().delete()


def save_currencies_to_database(currencies_list):
    """
    The save_currencies_to_database function takes a list of dictionaries as an argument.
    Each dictionary in the list contains information about one bank's currency exchange rates.
    The function creates Currencies objects from each dictionary and saves them to the database.
    
    :param currencies_list: Pass the list of dictionaries to the function
    :return: The number of created objects
    :doc-author: Trelent
    """
    currencies_objects = [
        Currencies(
            bank_name=currencies["bank_name"],
            buy_eur=currencies["eur_buy"],
            sell_eur=currencies["eur_sell"],
            buy_usd=currencies["usd_buy"],
            sell_usd=currencies["usd_sell"],
            pln_buy=currencies["pln_buy"],
            pln_sell=currencies["pln_sell"],
            url_link=currencies["url_link"],
        )
        for currencies in currencies_list
    ]
    Currencies.objects.bulk_create(currencies_objects)


#
def privat_currency(url="https://privatbank.ua"):
    """
    The privat_currency function scrapes the PrivatBank website for currency exchange rates.
    It returns a list of dictionaries containing the following keys:
    bank_name, eur_buy, eur_sell, usd_buy, usd_sell, pln_buy and pln sell.
    
    :param url: Pass the url to the function
    :return: A list of dictionaries
    :doc-author: Trelent
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    eur_buy = soup.find("td", id="EUR_buy").text.strip()
    eur_sell = soup.find("td", id="EUR_sell").text.strip()
    usd_buy = soup.find("td", id="USD_buy").text.strip()
    usd_sell = soup.find("td", id="USD_sell").text.strip()
    pln_buy = soup.find("td", id="PLN_buy").text.strip()
    pln_sell = soup.find("td", id="PLN_sell").text.strip()

    return [
        {
            "bank_name": "PrivatBank",
            "eur_buy": eur_buy,
            "eur_sell": eur_sell,
            "usd_buy": usd_buy,
            "usd_sell": usd_sell,
            "pln_buy": pln_buy,
            "pln_sell": pln_sell,
            "url_link": "https://privatbank.ua",
        }
    ]


def pumb_currency(url="https://about.pumb.ua/info/currency_converter"):
    """
    The pumb_currency function scrapes the Pumb bank's website for currency exchange rates.
    It returns a list of dictionaries with the following keys:
    - bank_name (str)
    - eur_buy (float)
    - eur_sell (float)
    - usd_buy (float)
    - usd_sell(float)
    
    :param url: Specify the url of the page to be scraped
    :return: A list of dictionaries
    :doc-author: Trelent
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    eur_buy = soup.find("td", {"data-currency-eurbuy": True})
    eur_sell = soup.find("td", {"data-currency-eursell": True})
    usd_buy = soup.find("td", {"data-currency-usdbuy": True})
    usd_sell = soup.find("td", {"data-currency-usdsell": True})
    pln_buy = soup.find("td", {"data-currency-plnbuy": True})
    pln_sell = soup.find("td", {"data-currency-plnshell": True})

    if eur_buy and eur_sell and usd_buy and usd_sell and pln_buy and pln_sell:

        return [
            {
                "bank_name": "Pumb",
                "eur_buy": eur_buy.text,
                "eur_sell": eur_sell.text,
                "usd_buy": usd_buy.text,
                "usd_sell": usd_sell.text,
                "pln_buy": pln_buy.text,
                "pln_sell": pln_sell.text,
                "url_link": "https://about.pumb.ua/info/currency_converter",
            }
        ]
    else:
        return []

def minfin_currency(url="https://minfin.com.ua/currency/"):
    """
    The minfin_currency function scrapes the Minfin website for currency exchange rates.
    It returns a list of dictionaries with the following keys: bank_name, eur_buy, eur_sell, usd_buy, usd_sell and pln buy.
    The values are strings representing the current exchange rate.
    
    :param url: Specify the url of the page to scrape
    :return: A list of dictionaries
    :doc-author: Trelent
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    pln_rows = soup.find_all("tr", class_="sc-1x32wa2-4 dKDsVV")[2]
    eur_rows = soup.find_all("tr", class_="sc-1x32wa2-4 dKDsVV")[1]

    usd_buy = (
        soup.select_one("td.sc-1x32wa2-6.bIIiwq")
        .find_next_sibling("td")
        .div.text.strip()[:5]
    )
    usd_sell = (
        soup.select_one("td.sc-1x32wa2-6.bIIiwq")
        .find_next_sibling("td")
        .find_next_sibling("td")
        .div.text.strip()[:5]
    )

    pln_buy = pln_rows.find_all("td")[1].div.text.strip()[:5]
    pln_sell = pln_rows.find_all("td")[2].div.text.strip()[:5]
    eur_buy = eur_rows.find_all("td")[1].div.text.strip()[:5]
    eur_sell = eur_rows.find_all("td")[2].div.text.strip()[:5]

    return [
        {
            "bank_name": "Minfin",
            "eur_buy": eur_buy,
            "eur_sell": eur_sell,
            "usd_buy": usd_buy,
            "usd_sell": usd_sell,
            "pln_buy": pln_buy,
            "pln_sell": pln_sell,
            "url_link": "https://minfin.com.ua/currency/",
        }
    ]


def finance_currency(url="https://finance.ua/ru/currency"):
    """
    The finance_currency function scrapes the Finance.ua website for currency exchange rates and returns a list of dictionaries containing the following keys:
    bank_name - name of the bank (Finance.ua)
    eur_buy - Euro buy rate
    eur_sell - Euro sell rate
    usd_buy - US Dollar buy rate
    usd_sell - US Dollar sell rate
    
    
    :param url: Specify the url of the page that we want to scrape
    :return: A list with one dictionary
    :doc-author: Trelent
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    pln_rows = soup.find_all("tr", class_="minor")[0]
    eur_rows = soup.find_all("tr", class_="major major-last")[0]

    usd_buy = soup.find("td", class_="c2").text.split()[0]
    usd_sell = soup.find("td", class_="c3").text.split()[0]

    pln_buy = pln_rows.find_all("td")[1].text.split()[0]
    pln_sell = pln_rows.find_all("td")[2].text.split()[0]
    eur_buy = eur_rows.find_all("td")[1].text.split()[0]
    eur_sell = eur_rows.find_all("td")[2].text.split()[0]

    return [
        {
            "bank_name": "Finance.ua",
            "eur_buy": eur_buy,
            "eur_sell": eur_sell,
            "usd_buy": usd_buy,
            "usd_sell": usd_sell,
            "pln_buy": pln_buy,
            "pln_sell": pln_sell,
            "url_link": "https://finance.ua/ru/currency",
        }
    ]


if __name__ == "__main__":
    privat = privat_currency("https://privatbank.ua")
    pumb = pumb_currency("https://about.pumb.ua/info/currency_converter")
    minfin = minfin_currency("https://minfin.com.ua/currency/")
    finance = finance_currency("https://finance.ua/ru/currency")
    save_currencies_to_database(privat)
    save_currencies_to_database(pumb)
    save_currencies_to_database(minfin)
    save_currencies_to_database(finance)
