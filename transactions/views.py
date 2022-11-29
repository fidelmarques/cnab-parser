from rest_framework import generics
from django.db.models import Sum


from .models import Transaction
from .serializers import TransactionSerializer, TransactionSubtotalSerializer


class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# class TransactionSubtotalView(generics.ListAPIView):
#     queryset = Transaction.objects.aggregate(subtotal=Sum("value"))
#     serializer_class = TransactionSubtotalSerializer
