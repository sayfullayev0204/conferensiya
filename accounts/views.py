from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, UserForm

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class LoginView(View):
    form_class = UserForm
    template_name = 'registration/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Muvaffaqiyatli kirgandan keyin
            else:
                return render(request, self.template_name, {
                    'form': form,
                    'error': "Noto'g'ri foydalanuvchi nomi yoki parol."
                })

        return render(request, self.template_name, {'form': form})
# class SignUpView(View, CreateView):
#     def get(self, request):
#         form = CustomUserCreationForm()
#         return render(request, 'registration/signup.html', {'form': form})

    # def post(self, request):
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('login')  # Yoki boshqa sahifaga yo'naltirish
    #     else:
    #         return render(request, 'accounts/signup.html', {'form': form})