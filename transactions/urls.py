from django.urls import path
from . import views

urlpatterns = [
    path(
        "transactions/",
        views.TransactionView.as_view(),
        name="transactions",
    ),
    # path(
    #     "transactions/subtotal/",
    #     views.TransactionSubtotalView.as_view(),
    #     name="transactions-subtotal",
    # ),
]
