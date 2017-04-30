from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf
from accounts.forms import MyRegistrationForm


def register(request):
    print request
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect('/accounts/register/complete')
    else:
        form = MyRegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render(request, 'registration/registration_form.html', token)


def profile(request):
    return render_to_response('registration/profile.html', {'user': request.user})


def registration_complete(request):
    return render_to_response('registration/registration_complete.html')


def logout_complete(request):
    return render_to_response('registration/logout.html')