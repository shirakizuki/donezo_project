from django.urls import path
from . import views 

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('user/<int:user_id>/home/<str:section>/', views.home, name='home'),
    path('user/<int:user_id>/filters/', views.filters, name='filters'),
    path('user/<int:user_id>/priority/add/', views.add_priority, name='add_priority'),
    path('user/<int:user_id>/priority/<int:priority_id>/edit/', views.edit_priority, name='edit_priority'),
    path('user/<int:user_id>/priority/<int:priority_id>/delete/', views.delete_priority, name='delete_priority'),
    path('user/<int:user_id>/label/add/', views.add_label, name='add_label'),
    path('user/<int:user_id>/label/<int:label_id>/edit/', views.edit_label, name='edit_label'),
    path('user/<int:user_id>/label/<int:label_id>/delete/', views.delete_label, name='delete_label'),
    path('logout/', views.logout_view, name='logout'),
]
