from django.http import HttpResponseForbidden
from .models import CustomUser


def account_ownership_required(func):
    def decorated(request, *args, **kwardgs):
        user = CustomUser.objects.get(pk=kwardgs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwardgs)

    return decorated
