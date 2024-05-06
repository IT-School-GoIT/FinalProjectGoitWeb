from django.shortcuts import render
from django.shortcuts import redirect

from .models import Currencies
from .exchange import privat_currency, save_currencies_to_database, clear_currency_database, pumb_currency, minfin_currency, finance_currency


def list_currency(request):
    privat = Currencies.objects.filter(bank_name='PrivatBank')
    pumb = Currencies.objects.filter(bank_name="Pumb")
    minfin = Currencies.objects.filter(bank_name="Minfin")
    finance = Currencies.objects.filter(bank_name="Finance.ua")
    # return render(request, '_fragments/TestimonialStart.html', {'privat': privat, 'pumb': pumb, 'minfin': minfin, "finance": finance})exchange_rate.html
    return render(request, 'home/exchange_rate.html', {'privat': privat, 'pumb': pumb, 'minfin': minfin, "finance": finance})

def add_currency(request):
    clear_currency_database()
    privat = privat_currency('https://privatbank.ua')
    pumb = pumb_currency('https://about.pumb.ua/info/currency_converter')
    minfin = minfin_currency('https://minfin.com.ua/currency/')
    finance = finance_currency('https://finance.ua/ru/currency')
    save_currencies_to_database(privat)
    save_currencies_to_database(pumb)
    save_currencies_to_database(minfin)
    save_currencies_to_database(finance)
    # return render(request, '_fragments/exc.html' )
    return redirect('currency')



