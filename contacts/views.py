from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from contacts.models import Contact
from contacts.forms import ContactForm
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q


@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'comander/contacts.html', {'contacts': contacts})


@login_required
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.request = request
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, "Contact saved successfully")
            return redirect('contacts:contact_list')
        else:
            messages.error(request, "Form is not valid")
    else:
        form = ContactForm()
        form.request = request
    return render(request, 'comander/create_contact.html', {'form': form})


@login_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)
    if request.method == 'POST':
        form: ContactForm = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact edited successfully")
            return redirect('contacts:contact_list')
        else:
            messages.error(request, "Form is not valid")
    else:
        form = ContactForm(instance=contact)
    return render(request, 'comander/edit_contact.html',
                  {'form': form, 'contact': contact, })


@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:contact_list')
    return render(request, 'comander/delete_contact.html', {'contact': contact})


@login_required
def search_contacts(request):
    query = request.GET.get('q')
    contacts = Contact.objects.filter(name__icontains=query)
    return render(request, 'comander/search_all.html',
                  {'contacts': contacts, 'query': query})


@login_required
def get_contacts_with_birthday_in(request):
    days_until_birthday_str = request.GET.get('days_until_birthday', '0')
    try:
        days_until_birthday = int(days_until_birthday_str)
        if days_until_birthday <= 0:
            raise ValueError("Days until birthday must be a positive integer")
    except (ValueError, TypeError):
        return render(request, 'comander/search_error_contact.html')

    current_date = timezone.now().date()
    target_date_end = current_date + timedelta(days=days_until_birthday)

    contacts_with_birthday = Contact.objects.filter(
        Q(user=request.user) &
        Q(birthday__day__gte=current_date.day) &
        Q(birthday__month=current_date.month) &
        Q(birthday__day__lte=target_date_end.day) &
        Q(birthday__month=target_date_end.month)
    )

    return render(request, 'comander/contacts.html',
                  {'contacts': contacts_with_birthday})
