from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from Todoapp.models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,UpdateView,DeleteView,FormView)
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,views as auth_views
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView, PasswordResetView, 
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
    )
from django.core.mail import send_mail
# Create your views here.
def sendmail(request):
    subject = " タイトル "
    message = " これはメッセージです。 "
    from_email = "magicalbananaaa@gmail.com"
    to = ["aiuai4665@gmail.com"]
    send_mail(subject, message, from_email, to)
    return HttpResponse("メール送信完了") 

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        
        searchText = self.request.GET.get("search")or ""
        if searchText:
            context["tasks"]=context["tasks"].filter(title__startswith=searchText)
        
        context["search"] = searchText
        return context
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = "task"

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
        
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ["title","description","completed"]
    success_url = reverse_lazy("tasks")
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    context_object_name = "tasks"
    
class TaskLoginView(LoginView):
    field = "__all__"
    template_name = "Todoapp/login.html"
    def get_success_url(self):
        return reverse_lazy("tasks")

class RegiserTodo(FormView):
    template_name = "Todoapp/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")
    
    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    """パスワード変更ビュー"""
    success_url = reverse_lazy('password_change_done')
    template_name = 'todoapp/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 継承元のメソッドCALL
        context["form_name"] = "password_change"
        return context


class PasswordChangeDone(LoginRequiredMixin,PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'todoapp/password_change_done.html'

# --- ここから追加
class PasswordReset(PasswordResetView):
    """パスワード変更用URLの送付ページ"""
    subject_template_name = 'todoapp/mail_template/reset/subject.txt'
    email_template_name = 'todoapp/mail_template/reset/message.txt'
    template_name = 'todoapp/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    """パスワード変更用URLを送りましたページ"""
    template_name = 'todoapp/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'todoapp/password_reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    """新パスワード設定しましたページ"""
    template_name = 'todoapp/password_reset_complete.html'