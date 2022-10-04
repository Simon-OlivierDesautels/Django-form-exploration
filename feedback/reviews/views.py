from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ReviewForm
# from .models import Review


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })


# def review(request):
#     if request.method == "POST":
#         # existing_data = Review.objects.get(pk=1)
#         form = ReviewForm(request.POST)
#         # form = ReviewForm(request.POST, instance=existing_data)

#         if form.is_valid():
#             # **Because model is connected
#             form.save()

#             # review = Review(
#             #     full_name=form.cleaned_data["full_name"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     rating=form.cleaned_data["rating"])
#             # review.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
