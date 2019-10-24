from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music, Artist, Comment
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer


@api_view(['GET'])
def music_list(request):
    # 만약에 아티스트아이디가 쿼리 params 로 넘어온다면 필터링한 값만 응답한다.
    artist_pk = request.GET.get('artist_pk')
    params = {}

    if artist_pk is not None:
        params['artist_id'] = artist_pk
    musics = Music.objects.filter(**params)  # 보여주고 싶은 데이터들을 db에서 꺼낸다

    serializer = MusicSerializer(musics, many=True)  # 바꾸고 싶은(꺼낸) 데이터를 첫번째인자에 넣는다
    return Response(serializer.data)  # 


@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
    elif request.method == 'PUT':
        serializer = MusicSerializer(data=request.data, instance=music)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    else:
        music.delete()
        return Response({'message': 'Music has been deleted!'})
    return Response(serializer.data)


@api_view(['POST'])
def musics_create(request, artist_pk):
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  # 검증에 시패하면 400 Bad Request 오류를 발생
        serializer.save(artist_id=artist_pk)  # 얘 때문에 else 없이 validation 에러 발생 시킴
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def artist_list_apply(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
    else:
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)


@api_view(['POST'])
def comments_create(request, music_pk):
    print(request.data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  # 검증에 시패하면 400 Bad Request 오류를 발생
        serializer.save(music_id=music_pk)  # 얘 때문에 else 없이 validation 에러 발생 시킴
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def comments_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({'message': 'Comment has been deleted!'})
