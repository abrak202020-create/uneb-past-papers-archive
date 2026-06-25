from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def role_required(*allowed_roles):

    def decorator(view_func):

        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return redirect("login")

            profile = getattr(request.user, "userprofile", None)

            if profile is None:
                messages.error(
                    request,
                    "User profile not found."
                )
                return redirect("login")

            if profile.role not in allowed_roles:
                messages.error(
                    request,
                    "You do not have permission to access this page."
                )
                return redirect("/")

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator