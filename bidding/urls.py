from django.urls import path

from bidding.views import BiddingDetailView, BiddingDetailSaleView

urlpatterns = [
    path('', BiddingDetailView.as_view()),
    path('/sale', BiddingDetailSaleView.as_view()),
]
