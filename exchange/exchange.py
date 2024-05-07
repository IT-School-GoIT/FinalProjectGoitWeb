import requests
from bs4 import BeautifulSoup
from .models import Currencies


def clear_currency_database():
    Currencies.objects.all().delete()


def save_currencies_to_database(currencies_list):
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

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    eur_buy = soup.find("td", {"data-currency-eurbuy": True}).text
    eur_sell = soup.find("td", {"data-currency-eursell": True}).text
    usd_buy = soup.find("td", {"data-currency-usdbuy": True}).text
    usd_sell = soup.find("td", {"data-currency-usdsell": True}).text
    pln_buy = soup.find("td", {"data-currency-plnbuy": True}).text
    pln_sell = soup.find("td", {"data-currency-plnshell": True}).text

    return [
        {
            "bank_name": "Pumb",
            "eur_buy": eur_buy,
            "eur_sell": eur_sell,
            "usd_buy": usd_buy,
            "usd_sell": usd_sell,
            "pln_buy": pln_buy,
            "pln_sell": pln_sell,
            "url_link": "https://about.pumb.ua/info/currency_converter",
        }
    ]


def minfin_currency(url="https://minfin.com.ua/currency/"):
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
