from django.shortcuts import render
from django.shortcuts import redirect

from .models import Currencies
from .exchange import (
    privat_currency,
    save_currencies_to_database,
    clear_currency_database,
    pumb_currency,
    minfin_currency,
    finance_currency,
)


def list_currency(request):
    """
    The list_currency function is used to display the exchange rate of different banks.
    It takes a request as an argument and returns a render function with the following arguments:
    - request, which is passed from the view;
    - &quot;home/exchange_rate.html&quot;, which is a template for displaying data;
    - {&quot;privat&quot;

    : privat, &quot; pumb&quot;: pumb, &quot;minfin&quot;: minfin, &quot;finance&quot;: finance},
                where privat = Currencies.objects.filter(bank_name=&quot;PrivatBank&quot;), 
                pumb = Currencies.objects.filter(bank
    
    :param request: Pass the request object to the view
    :return: The exchange rate for each bank
    :doc-author: Trelent
    """
    privat = Currencies.objects.filter(bank_name="PrivatBank")
    pumb = Currencies.objects.filter(bank_name="Pumb")
    minfin = Currencies.objects.filter(bank_name="Minfin")
    finance = Currencies.objects.filter(bank_name="Finance.ua")
    # return render(request, '_fragments/TestimonialStart.html', {'privat': privat, 'pumb': pumb, 'minfin': minfin, "finance": finance})exchange_rate.html
    return render(
        request,
        "home/exchange_rate.html",
        {"privat": privat, "pumb": pumb, "minfin": minfin, "finance": finance},
    )


def add_currency(request):
    """
    The add_currency function is used to add currency data from four different sources
    to the database. The function takes in a request object and returns an HttpResponseRedirect
    object that redirects the user to the currency page.
    
    :param request: Get the data from the form
    :return: The redirect function, which is used to return an http response with a url to the client
    :doc-author: Trelent
    """
    clear_currency_database()
    privat = privat_currency("https://privatbank.ua")
    pumb = pumb_currency("https://about.pumb.ua/info/currency_converter")
    minfin = minfin_currency("https://minfin.com.ua/currency/")
    finance = finance_currency("https://finance.ua/ru/currency")
    save_currencies_to_database(privat)
    save_currencies_to_database(pumb)
    save_currencies_to_database(minfin)
    save_currencies_to_database(finance)
    # return render(request, '_fragments/exc.html' )
    return redirect("currency")
