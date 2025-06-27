from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    # Web Views
    path('', views.index_page, name='index_page'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.sign_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('request_submitted/', views.request_submit, name='request_page'),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('request_list/', views.request_list, name='request_list'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('admin_dashboard/update_status/<int:pk>/', views.update_request_status, name='update_request_status'),

    #New DRF API Endpoints
    path('api/public/', api_views.public_api, name='public_api'),
    path('api/protected/', api_views.protected_api, name='protected_api'),
]
