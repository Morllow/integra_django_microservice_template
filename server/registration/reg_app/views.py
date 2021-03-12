from django.shortcuts import render
from django.contrib.auth.models import Group, User
from .forms import SignUpForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
