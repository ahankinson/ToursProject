from goudimel.models.piece import Piece
from goudimel.models.book import Book
from goudimel.serializers.phrase import PhraseSerializer
from rest_framework import serializers

class BookMinimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title','url')


class PieceSerializer(serializers.HyperlinkedModelSerializer):
    phrases = PhraseSerializer()
    book_title = serializers.Field(source="book_title")
    book_id = BookMinimalSerializer()
    class Meta:
        model = Piece
