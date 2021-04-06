from django.urls import path

from product.views import ProductFilterView, SearchView

urlpatterns = [
    path('', ProductFilterView.as_view()),
    path('/search', SearchView.as_view())
]
