from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm



def logout_view(request):
    """Log the user out.
    """
    logout(request)
    return HttpResponseRedirect(reverse('my_fridge:home'))


def register(request):
    """Register a new user.
    """
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log the user in and then redirect to home page.
            authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('my_fridge:home'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
