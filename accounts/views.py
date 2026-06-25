from django.shortcuts import render


def choose_account(request):

    return render(
        request,
        "accounts/choose_account.html"
    )