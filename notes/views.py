from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .forms import NoteForm, TagForm
from .models import Note, Tag


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        """
        The get_queryset function is a method that returns the queryset of objects to be displayed in the view.
        The default implementation simply returns self.model._default_manager.all(), but it may be overridden to customize the behavior of all list views.
        
        :param self: Refer to the current object
        :return: A queryset that is filtered by the current user
        :doc-author: Trelent
        """
        note_query = self.request.GET.get("note_query")
        tag_query = self.request.GET.get("tag_query")
        queryset = super().get_queryset().filter(owner=self.request.user)

        if note_query:
            queryset = queryset.filter(name__icontains=note_query)

        if tag_query:
            queryset = queryset.filter(tags__name__icontains=tag_query)

        return queryset

    def get_context_data(self, **kwargs):
        """
        The get_context_data function is a method that Django calls when rendering the template.
        It allows us to add extra context variables to the template, which we can then use in our templates.
        
        :param self: Refer to the current instance of the class
        :param **kwargs: Pass keyword arguments to the function
        :return: A dictionary with the key &quot;all_tags&quot; and value of all tags for the current user
        :doc-author: Trelent
        """
        context = super().get_context_data(**kwargs)
        context["all_tags"] = Tag.objects.filter(owner=self.request.user)
        return context


@require_POST
def toggle_note_done(request, pk):
    """
    The toggle_note_done function is a view that toggles the done status of a note.
    It takes an HTTP request and the primary key of a note as arguments, gets the
    note with get_object_or_404, toggles its done attribute, saves it back into
    the database and redirects back to the list view.
    
    :param request: Pass the request object to the view
    :param pk: Retrieve the note object from the database
    :return: A redirect to the note_list view
    :doc-author: Trelent
    """
    note = get_object_or_404(Note, pk=pk)
    note.done = not note.done
    note.save()
    return redirect("notes:note_list")


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"

    def get_context_data(self, **kwargs):
        """
        The get_context_data function is a method that Django calls when rendering the template.
        It allows us to add extra context data to the template, which we can then use in our templates.
        In this case, we're adding a list of all tags owned by the current user.
        
        :param self: Refer to the current object
        :param **kwargs: Pass keyworded, variable-length argument list to a function
        :return: A dictionary
        :doc-author: Trelent
        """
        context = super().get_context_data(**kwargs)
        context["user_tags"] = Tag.objects.filter(owner=self.request.user)
        return context


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = "notes/note_form.html"
    form_class = NoteForm

    def form_valid(self, form):
        """
        The form_valid function is called when a form is submitted and valid.
        It's passed the form object, which contains all of the data entered by
        the user. The function should return an HttpResponseRedirect to redirect
        to another page or render_to_response() to display a template.
        
        :param self: Refer to the current instance of a class
        :param form: Pass the form to the view
        :return: The superclass form_valid function
        :doc-author: Trelent
        """
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        The get_success_url function is a helper function that returns the URL to redirect to after processing a form.
        The default implementation will return the value of success_url, if it's set. Otherwise, it'll try and determine
        the correct URL by looking at the object's get_absolute_url method.
        
        :param self: Refer to the object that is calling the function
        :return: The url of the page that we want to go to after a successful form submission
        :doc-author: Trelent
        """
        return reverse("notes:note_list")

    def get_context_data(self, **kwargs):
        """
        The get_context_data function is a method that Django calls when rendering the template.
        It allows us to add extra context data to the template, which we can then use in our templates.
        In this case, we're adding a list of all tags owned by the current user.
        
        :param self: Refer to the current object
        :param **kwargs: Pass keyword arguments to the view
        :return: A dictionary of data that is passed to the template
        :doc-author: Trelent
        """
        context = super().get_context_data(**kwargs)
        context["user_tags"] = Tag.objects.filter(owner=self.request.user)
        return context


class NoteEditView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = "notes/note_form.html"
    form_class = NoteForm

    def get_success_url(self):
        """
        The get_success_url function is a helper function that returns the URL to redirect to after processing a form.
        The default implementation will return the value of success_url, if it's set. Otherwise, it'll try and determine
        the correct URL by looking at the object's get_absolute_url method.
        
        :param self: Refer to the current instance of the class
        :return: The url of the note list page
        :doc-author: Trelent
        """
        return reverse("notes:note_list")

    def get_context_data(self, **kwargs):
        """
        The get_context_data function is a method that Django calls when rendering the template.
        It allows us to add extra context data to the template, which we can then use in our templates.
        In this case, we're adding a list of all tags owned by the current user.
        
        :param self: Refer to the current object
        :param **kwargs: Pass keyworded, variable-length argument list to a function
        :return: A dictionary of context data
        :doc-author: Trelent
        """
        context = super().get_context_data(**kwargs)
        context["user_tags"] = Tag.objects.filter(owner=self.request.user)
        return context


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"

    def get_success_url(self):
        """
        The get_success_url function is a helper function that returns the URL to redirect to after processing a form.
        The default implementation will return the value of success_url, if it's set. Otherwise, it'll try and determine
        the correct URL by looking at the object's get_absolute_url method.
        
        :param self: Refer to the current object
        :return: The url of the note list view
        :doc-author: Trelent
        """
        return reverse("notes:note_list")


class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = "notes/tag_list.html"
    context_object_name = "tags"

    def get_queryset(self):
        """
        The get_queryset function is a method that returns the queryset of objects
        that will be used to create this view. By default, it returns model._default_manager.all(),
        but we override it here to return only the notes owned by the current user.
        
        :param self: Refer to the current object
        :return: A queryset that filters the objects by owner
        :doc-author: Trelent
        """
        queryset = (
            super(TagListView, self).get_queryset().filter(owner=self.request.user)
        )
        if self.request.user.is_authenticated:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "notes/tag_form.html"
    form_class = TagForm

    def form_valid(self, form):
        """
        The form_valid function is called when a form is submitted and valid.
        It's passed the form object, which contains all of the data entered by
        the user. The function should return an HttpResponseRedirect to redirect
        to another page or render_to_response() to display a template.
        
        :param self: Refer to the current instance of a class
        :param form: Access the form that was submitted
        :return: The super() of the form_valid function
        :doc-author: Trelent
        """
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        The get_success_url function is a helper function that returns the URL to redirect to after successful form submission.
        
        :param self: Refer to the current object
        :return: The url of the tag_list view
        :doc-author: Trelent
        """
        return reverse("notes:tag_list")


class TagEditView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = "notes/tag_form.html"
    form_class = TagForm

    def get_success_url(self):
        """
        The get_success_url function is a helper function that returns the URL to redirect to after successful form submission.
        
        :param self: Refer to the current object
        :return: The url of the tag_list view
        :doc-author: Trelent
        """
        return reverse("notes:tag_list")


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy("notes:tag_list")

    def get_success_url(self):
        """
        The get_success_url function is a helper function that returns the URL to redirect to after processing a valid form.
        It's used by both CreateView and UpdateView, but it can be overridden if you need custom logic.
        
        :param self: Represent the instance of the object
        :return: The success_url variable
        :doc-author: Trelent
        """
        return self.success_url
