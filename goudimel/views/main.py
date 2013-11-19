from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, XMLRenderer

from goudimel.renderers.custom_html_renderer import CustomHTMLRenderer
from goudimel.models.book import Book
from goudimel.models.piece import Piece
from goudimel.models.phrase import Phrase

from goudimel.serializers.book import BookSerializer
from goudimel.serializers.piece import PieceSerializer
from goudimel.serializers.phrase import PhraseSerializer

def home(request):
    data = {}
    return render(request, "index.html", data)


class BookListHTMLRenderer(CustomHTMLRenderer):
    template_name = "book/book_list.html"


class BookDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "book/book_detail.html"


class BookList(generics.ListCreateAPIView):
    model = Book
    serializer_class = BookSerializer
    renderer_classes = (JSONRenderer, BookListHTMLRenderer)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Book
    serializer_class = BookSerializer
    renderer_classes = (JSONRenderer, BookDetailHTMLRenderer)


class PieceListHTMLRenderer(CustomHTMLRenderer):
    template_name = "piece/piece_list.html"


class PieceDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "piece/piece_detail.html"


class PieceList(generics.ListCreateAPIView):
    model = Piece
    serializer_class = PieceSerializer
    renderer_classes = (JSONRenderer, PieceListHTMLRenderer)


class PieceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Piece
    serializer_class = PieceSerializer
    renderer_classes = (JSONRenderer, PieceDetailHTMLRenderer)


class PhraseListHTMLRenderer(CustomHTMLRenderer):
    template_name = "phrase/phrase_list.html"


class PhraseDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "phrase/phrase_detail.html"


class PhraseList(generics.ListCreateAPIView):
    model = Phrase
    serializer_class = PhraseSerializer
    renderer_classes = (JSONRenderer, PhraseListHTMLRenderer)


class PhraseDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Phrase
    serializer_class = PhraseSerializer
    renderer_classes = (JSONRenderer, PhraseDetailHTMLRenderer)
