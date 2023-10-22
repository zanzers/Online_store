from django.urls import path

from . import views

app_name = 'items'


urlpatterns = [
    path('', views.browser, name="browser"),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name="detail")
]


# 50:04