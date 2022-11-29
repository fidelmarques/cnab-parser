from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "type",
            "date",
            "value",
            "cpf",
            "hour",
            "shop_owner",
            "shop_name",
        ]

    def create(self, validated_data):
        print(validated_data)
        Transaction.full_clean(**validated_data)


class TransactionSubtotalSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

    def get_subtotal(self, obj):
        return obj.get_subtotal

    class Meta:
        model = Transaction
        fields = [
            "subtotal",
        ]
