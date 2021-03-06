from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AdminViewSet, AuthTokenViewClass, CategoryViewSet,
                    CommentViewSet, GenreViewSet, ReviewViewSet, TitleViewSet,
                    UserSignupViewClass, UserViewClass)

router_v1 = DefaultRouter()

router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

router_v1.register('users', AdminViewSet, basename='us')
urlpatterns = [
    path('v1/users/me/', UserViewClass.as_view(), name='user_me'),
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', UserSignupViewClass.as_view(), name='user_signup'),
    path('v1/auth/token/', AuthTokenViewClass.as_view(), name='getting_token'),
]
