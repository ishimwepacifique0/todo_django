from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('dashboardd/',views.dashboard,name="dashboard"),
    path('manage_student/',views.manage_student,name='manage_student'),
    path('create_student/',views.create_student,name="create_student"),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('edit_student/<int:id>',views.edit_student,name='edit_student'),
    path('',views.send_request,name='send_request')
]