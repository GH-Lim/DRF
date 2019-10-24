from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title='Music API',
        default_version='v1',
        description='음악 관련 API 서비스입니다.',
    )
)


app_name = 'musics'
urlpatterns = [
    path('musics/', views.music_list, name='music_list'),
    path('musics/<int:music_pk>/', views.music_detail, name='music_detail'),

    path('musics/<int:music_pk>/comments/', views.comments_create, name='comments_create'),
    path('artists/', views.artist_list_apply, name='artist_list_apply'),
    path('artists/<int:artist_pk>/', views.artist_detail, name='artist_detail'),

    path('artists/<int:artist_pk>/musics/', views.musics_create, name='musics_create'),
    
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:comment_pk>/', views.comments_update_and_delete, name='comments_update_and_delete'),
    path('artists/<int:comment_pk>/', views.comment_detail, name='comment_detail'),

    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
]
