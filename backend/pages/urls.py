from django.urls import path
from .views import home, new_detail, contact_us, blog_etries


urlpatterns = [
    path('', home, name="home"),
    path('detail/<int:pk>/', new_detail, name="new_detail"),
    path('contact/us/', contact_us, name="contact_us"),
    path('news/', blog_etries, name="blog_etries"),
]
