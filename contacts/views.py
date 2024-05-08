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
    """
    The contact_list function is a view that displays all contacts in the database.
    It takes an HTTP request as its first argument and returns an HTTP response.
    The contact_list function uses the render() shortcut to generate a template response, which means it will return an HttpResponse object with the rendered template content filled in.
    
    :param request: Get the user's contacts
    :return: A rendered template, which is the html for the contacts page
    :doc-author: Trelent
    """
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'comander/contacts.html', {'contacts': contacts})


@login_required
def create_contact(request):
    """
    The create_contact function is used to create a new contact.
    The function first checks if the request method is POST, which means that the user has submitted data via a form.
    If so, it creates an instance of ContactForm and passes in the POST data from the request object as an argument.
    It then sets form's request attribute equal to request (this will be explained later).  Next, it checks if form is valid by calling its is_valid() method.  If so, it saves contact without committing changes to database yet by calling save(commit=False) on form and assigning result to variable named contact;
    
    :param request: Get the request object
    :return: A redirect to the contact_list view
    :doc-author: Trelent
    """
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
    """
    The edit_contact function is used to edit a contact.
    It takes the request and contact_id as parameters,
    gets the object or 404 error if it doesn't exist,
    checks if the method is POST and then saves it.
    
    :param request: Get the current request
    :param contact_id: Retrieve the contact from the database
    :return: An httpresponseredirect object
    :doc-author: Trelent
    """
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
    """
    The delete_contact function is a view that allows the user to delete a contact.
    The function takes two arguments: request and contact_id. The request argument is an HTTP Request object, which contains information about the current web request that has triggered this view. The contact_id argument is an integer representing the primary key of the Contact instance we want to delete.
    
    :param request: Get the current request
    :param contact_id: Identify the contact to be deleted
    :return: A render function
    :doc-author: Trelent
    """
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:contact_list')
    return render(request, 'comander/delete_contact.html', {'contact': contact})


@login_required
def search_contacts(request):
    """
    The search_contacts function takes a request and returns a rendered template.
    The request is expected to be an HTTP GET with the query parameter 'q' set to
    the search term. The function will return all contacts whose name contains the
    search term in any case.
    
    :param request: Pass the request object to the view
    :return: A list of contacts that match the query
    :doc-author: Trelent
    """
    query = request.GET.get('q')
    contacts = Contact.objects.filter(name__icontains=query)
    return render(request, 'comander/search_all.html',
                  {'contacts': contacts, 'query': query})


@login_required
def get_contacts_with_birthday_in(request):
    """
    The get_contacts_with_birthday_in function takes a request object as its only argument.
    It then extracts the days_until_birthday parameter from the GET data of that request, and attempts to convert it into an integer.
    If this conversion fails, or if the resulting number is not positive, we render a search error page and return immediately.
    Otherwise we calculate target date end by adding days until birthday to current date (which is calculated using timezone now).
    We then use Q objects to filter our contacts with birthdays in that range.
    
    :param request: Get the user's input from the search box
    :return: A rendered template with the contacts that have a birthday within
    :doc-author: Trelent
    """
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
