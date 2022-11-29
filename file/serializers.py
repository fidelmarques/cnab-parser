from rest_framework import serializers

from .models import File

from transactions.models import Transaction

from utils.dataParser import dataParser


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "file",
        ]

    def create(self, validated_data):
        file = File.objects.create(**validated_data)

        with file.file.open(mode="r") as f:
            for line in f:
                data = dataParser(line)
                transaction = Transaction(**data)
                print(transaction.value)

                transaction.full_clean()
                transaction.save()

        return file

    def get(self, validated_data):
        return {"GET": "Please upload a file below."}
