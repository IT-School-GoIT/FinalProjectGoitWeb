from django.http import HttpResponse


class HttpResponseConflict(HttpResponse):
    status_code = 409

    def __init__(self, message, *args, **kwargs):
        content = str(message)
        super().__init__(content, *args, **kwargs)
