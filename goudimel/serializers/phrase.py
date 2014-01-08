from goudimel.models.phrase import Phrase
from rest_framework import serializers

class PhraseSerializer(serializers.HyperlinkedModelSerializer):
    piece_title = serializers.Field(source="piece_title")
    class Meta:
        model = Phrase