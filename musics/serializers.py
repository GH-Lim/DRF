from rest_framework import serializers
from .models import Music, Artist, Comment


class MusicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name',)


class ArtistDetailSerializer(ArtistSerializer):
    musics = MusicSerializer(many=True)

    class Meta(ArtistSerializer.Meta):
       fields = ArtistSerializer.Meta.fields + ('musics', ) 


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id',)
