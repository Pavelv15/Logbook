from django.views.generic import UpdateView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserEditForm,ProfileEditForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Profile

class ChangeFormView(UpdateView):
    form_class = PasswordChangeForm
    template_name = 'users/password_reset_confirm.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super(ChangeFormView, self).get_form_kwargs()
        kwargs['user'] = kwargs.pop('instance')
        return kwargs

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
       # if user_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'users/edit.html', {'user_form': user_form, 'profile_form': profile_form})
        
