from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from functools import wraps


def admin_only(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Periksa apakah user adalah superuser
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'common/forbidden.html')
    return _wrapped_view
