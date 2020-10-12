from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import BikeRoute, Review

class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'bikeroute_list'

    def get_queryset(self):
        """Return the last five published routes."""
        return BikeRoute.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = BikeRoute
    template_name = 'main/detail.html'

class ReviewsView(generic.ListView):
    template_name = 'main/reviews.html'
    context_object_name = 'reviews_list'

    def get_queryset(self):
        return Review.objects.all()

def review(request, bikeroute_id):
    bikeroute = get_object_or_404(BikeRoute, pk=bikeroute_id)
    return render(request, 'main/review.html', {'bikeroute': bikeroute})