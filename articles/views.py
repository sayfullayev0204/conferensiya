from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test



# Create your views here.

# class SuperUserPage(ListView):
#     @user_passes_test(lambda u: u.is_superuser)
#     def superuser_page(request):
#         return render(request, 'adminpage.html')

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

    def get_queryset(self):
       return Article.objects.filter(approved=True)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'summary', 'body', 'document')

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        # Avtomatik ravishda hozirgi foydalanuvchini author sifatida qo'shish
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class AdminPageView(ListView, View):
    model=Article
    template_name='adminpage.html'
    list_display = ('title', 'author', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    actions = ['approve_articles']  # Admin uchun tasdiqlash uchun action
    context_object_name = 'articles' 

    # def approve_articles(self, request, queryset):
    #     queryset.update(approved=True)

    def get_queryset(self):
       return Article.objects.filter(approved=False)
    
    def post(self, request):
        article_id = request.POST.get('article_id')
        action = request.POST.get('action')

        if article_id and action:
            try:
                article = Article.objects.get(id=article_id)
                if action == 'approve':
                    article.approved = True
                    article.save()
                    # self.message_user(request, "Maqola tasdiqlandi.")
                elif action == 'delete':
                    article.delete()
                    # self.message_user(request, "Maqola o'chirildi.")
            except Article.DoesNotExist:
                pass

        return redirect('article_list')  # Maqolalar ro'yxatiga qaytish