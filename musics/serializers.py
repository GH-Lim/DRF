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
    musics_count = serializers.IntegerField(source='musics.count')

    class Meta(ArtistSerializer.Meta):
       fields = ArtistSerializer.Meta.fields + ('musics', 'musics_count',) 


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'music_id', 'content',)
