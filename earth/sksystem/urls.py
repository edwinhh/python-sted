from django.urls import path
from . import views
urlpatterns = [
    path('book_add/', views.BookAddView.as_view()),#只有新增
]