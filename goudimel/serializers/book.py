from goudimel.models.book import Book
from goudimel.serializers.piece import PieceSerializer
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):
    pieces = PieceSerializer()
    class Meta:
        model = Book
