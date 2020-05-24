from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView
from account.forms import RegistrationForm, AccountAuthenticationForm, ProfileForm
from account.models import Profile

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			mobilenumber = form.cleaned_data.get('mobilenumber')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(mobilenumber=mobilenumber, password=raw_password)
			login(request, account)
			return redirect('index')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)


def logout_view(request):
	logout(request)
	return redirect('login')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("index")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			mobilenumber = request.POST['mobilenumber']
			password = request.POST['password']
			user = authenticate(mobilenumber=mobilenumber, password=password)

			if user:
				login(request, user)
				return redirect("index")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	print(form)
	return render(request, "account/login.html", context)

class ProfileView(TemplateView):
	template_name = 'account/profile.html'


	def get(self, request):
		user = request.user
		profile = Profile.objects.get(account=user)
		form = ProfileForm()
		return render(request, self.template_name, {'form': form, 'profile':profile})

	def post(self, request):
		user = request.user
		profile = Profile.objects.get(account=user)
		form = ProfileForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.account = request.user
			profile.save()
			form = ProfileForm()
			return redirect('index')
		return render(request, self.template_name, {'form':form, 'profile':profile})


#
# def account_view(request):
#
# 	if not request.user.is_authenticated:
# 			return redirect("login")
#
# 	context = {}
# 	if request.POST:
# 		form = AccountUpdateForm(request.POST, instance=request.user)
# 		if form.is_valid():
# 			form.initial = {
# 					"email": request.POST['email'],
# 					"username": request.POST['username'],
# 			}
# 			form.save()
# 			context['success_message'] = "Updated"
# 	else:
# 		form = AccountUpdateForm(
#
# 			initial={
# 					"email": request.user.email,
# 					"username": request.user.username,
# 				}
# 			)
#
# 	context['account_form'] = form
#
# 	blog_posts = BlogPost.objects.filter(author=request.user)
# 	context['blog_posts'] = blog_posts
#
# 	return render(request, "account/account.html", context)
#
#
# def must_authenticate_view(request):
# 	return render(request, 'account/must_authenticate.html', {})


