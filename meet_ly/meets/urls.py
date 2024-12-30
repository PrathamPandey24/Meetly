from django.urls import path
from . import views

urlpatterns = [
    path("meets/",views.MainPage.as_view(),name="MainPage"),
    path("meets/all/",views.AllMeets.as_view(),name="allmeet"),
    path('<int:pk>/', views.MeetDetail.as_view(), name='meet'),
    path('meets/all/add/', views.AddMeetView.as_view(), name='add_meet'),
    path('<int:pk>/delete/', views.DeleteMeetView.as_view(), name='Deletes_meet'),  
]