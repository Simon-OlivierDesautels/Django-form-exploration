from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView):
    model = Review
    # **This removes the need of the Review form class but gives you less control
    # fields = ["full_name","review_text","rating"]
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    
    
    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Very nice"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # **Will return all items that have a rating greater than 4
    # def get_queryset(self):
    #     base_query =  super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
    

class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
    context_object_name = "review"

