from django.urls import path
from . import views
from .views import (
    TaskList, TaskDetail,TaskCreate,
    TaskUpdate,TaskDelete,TaskLoginView,
    RegiserTodo
    )
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",TaskList.as_view(),name="tasks"),
    path("task/<int:pk>/",TaskDetail.as_view(),name="task"),
    path("create_task/",TaskCreate.as_view(),name="create_task"),
    path("edit_task/<int:pk>/",TaskUpdate.as_view(),name="edit_task"),
    path("delete_task/<int:pk>/",TaskDelete.as_view(),name="delete_task"),
    path("login/",TaskLoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(next_page="login"),name="logout"),
    path("register/",RegiserTodo.as_view(),name="register"),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'), #追加
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'), #追加
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'), #追加
    path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'), #追加
    ]
