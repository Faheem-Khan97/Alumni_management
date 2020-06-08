
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .forms import RegisterForm,UserProfileForm
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import authenticatedUser

User = get_user_model()


# Create your views here.

@login_required(login_url = 'loginPage')
def home(request):

    return render(request, 'UserModule/home.html')


@authenticatedUser
def Register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('UserModule/email_verify.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('An email containing a verification token has been sent to your registered email. Please confirm your email address to complete the registration')

    return render(request, 'UserModule/Register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
        
    else:
        return HttpResponse('Activation link is invalid!')


@authenticatedUser
def loginPage(request):
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'email or password is incorrect')
            return render(request, 'UserModule/login.html')


    
    return render(request, 'UserModule/login.html', context)





@login_required(login_url = 'loginPage')
def User_Profile_settings(request):

    user = request.user.profile
    form = UserProfileForm(instance = user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES, instance = user)
        if form.is_valid():
            form.save()
            return redirect('User_Profile_settings')

    context = {'form': form}
    return render(request, 'UserModule/userprofilesettings.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')
