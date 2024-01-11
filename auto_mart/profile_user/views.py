from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from car.models import Car
from . models import Purchase
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LogoutView


# Function based views:
# def register(request):
#     if request.method == 'POST':
#         register_form = forms.RegistrationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             messages.success(request, 'Account Created Successfully')
#             return redirect('register')
    
#     else:
#         register_form = forms.RegistrationForm()
#     return render(request, 'register.html', {'form' : register_form, 'type' : 'Register'})




# Class based views:
class RegisterView(View):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        register_form = forms.RegistrationForm()
        return render(request, self.template_name, {'form': register_form, 'type': 'Register'})

    def post(self, request, *args, **kwargs):
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')

        return render(request, self.template_name, {'form': register_form, 'type': 'Register'})

# Function based views:
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username=user_name, password=user_pass)
#             if user is not None:
#                 messages.success(request, 'Logged in Successfully')
#                 login(request, user)
#                 return redirect('profile')
#             else:
#                 messages.warning(request, 'Login information incorrect')
#                 return redirect('register')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'register.html', {'form' : form, 'type' : 'Login'})


# Class based views:
class UserLoginView(View):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form, 'type': 'Login'})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login information incorrect')
                return redirect('register')

        return render(request, self.template_name, {'form': form, 'type': 'Login'})


# Function based views:
# @login_required
# def profile(request):
#     purchases = Purchase.objects.filter(user = request.user)
#     return render(request, 'profile.html', {'purchases' : purchases})
    

# Class based views:
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        purchases = Purchase.objects.filter(user=request.user)
        return render(request, self.template_name, {'purchases': purchases})








# function based views:
@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})
    


# Class based views:
# @method_decorator(login_required, name='dispatch')
# class EditProfileView(UpdateView):
#     template_name = 'update_profile.html'
#     form_class = UserChangeForm
#     success_url = reverse_lazy('profile')

#     def get_object(self, queryset=None):
#         return self.request.user

#     def form_valid(self, form):
#         messages.success(self.request, 'Profile Updated Successfully')
#         return super().form_valid(form)




# function based views:
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
        form.fields['new_password1'].help_text = ''
        form.fields['new_password2'].help_text = ''
    return render(request, 'pass_change.html', {'form' : form})
    

# Class based views:
# @method_decorator(login_required, name='dispatch')
# class PasswordChangeCustomView(PasswordChangeView):
#     template_name = 'pass_change.html'
#     success_url = '/profile/'  # Change this to your desired success URL

#     def get_form(self, form_class=None):
#         form = super().get_form(form_class)
#         form.fields['new_password1'].help_text = ''
#         form.fields['new_password2'].help_text = ''
#         return form

#     def form_valid(self, form):
#         messages.success(self.request, 'Password Updated Successfully')
#         return super().form_valid(form)







# Function based views:
# def user_logout(request):
#     logout(request)
#     return redirect('homepage')




# Class based views:
class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(self.request, 'Logged out successfully')
        return redirect('user_login')




# function based views:
@login_required
def buy_now(request, id):
    car = get_object_or_404(Car, pk=id)

    if car.make_purchase(request.user):
        messages.success(request, 'Purchase successful!')
        return redirect('profile')
    else:
        messages.error(request, 'Not enough quantity available for purchase.')
        return redirect('detail_car')



# Class based views:
# @method_decorator(login_required, name='dispatch')
# class BuyNowView(DetailView):
#     model = Car
#     template_name = 'buy_now.html'
#     context_object_name = 'car'

#     def post(self, request, *args, **kwargs):
#         car = self.get_object()

#         if car.make_purchase(request.user):
#             messages.success(request, 'Purchase successful!')
#             return redirect('profile')
#         else:
#             messages.error(request, 'Not enough quantity available for purchase.')
#             return redirect('detail_car', pk=car.pk)

#     def get_success_url(self):
#         return reverse_lazy('profile')