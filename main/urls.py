from django.urls import path

from . import views

urlpatterns = [
    # ex: /bikeroute/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /bikeroute/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /bikeroute/5/results/
    path('<int:pk>/reviews/', views.ReviewsView.as_view(), name='reviews'),
    # ex: /bikeroute/5/review/
    path('<int:bikeroute_id>/review/', views.review, name='review'),
]