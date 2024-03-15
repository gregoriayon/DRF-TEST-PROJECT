from django.urls import path, include
from app_api.views import *

from rest_framework_simplejwt.views import (
        TokenObtainPairView, 
        TokenRefreshView, 
        TokenVerifyView
    )

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

app_name = "app_api"

API_URL_PREFIX = "api"

router = DefaultRouter()
router.register('viewset/person', PersonViewsetAPI, basename='person_viewset')
router.register('model/viewset/person', PersonModelViewsetAPI, basename='person__model_viewset')
router.register('read/only/model/viewset/person', PersonReadOnlyModelViewsetAPI, basename='person__read_only_model_viewset')
router.register('jwt', JWTAuthViewsetAPI, basename='jwt_auth_api')
router.register('throttling', ThrottlesView, basename='throttling_api')
router.register('throttling/custom', CustomThrottlesView, basename='custom_throttling_api')

# Relational Serializer Views Url
router.register('serializer/relational/singer', SingerModelViewsetAPI)
router.register('serializer/relational/song', SongModelViewsetAPI)
router.register('serializer/students/hyperlinked/model', StudentHyperLinkedViewsetAPI)


# Testing thunder mc
router.register('testing', TestThunderView, basename='testing')


urlpatterns = [
    path(f"{API_URL_PREFIX}/students/list/", get_students_list_view, name="students_list" ),
    path(f"{API_URL_PREFIX}/students/create/", create_student_view, name="students_create" ),

    path(f"{API_URL_PREFIX}/employee/<int:pk>", get_employee_view, name="employee" ),
    path(f"{API_URL_PREFIX}/employee/create/", create_employee_view, name="employee_create" ),
    path(f"{API_URL_PREFIX}/employee/update/<int:pk>", update_employee_view, name="employee_update" ),

    # Class APIView
    path(f"{API_URL_PREFIX}/person/", PersonAPIView.as_view(), name="person_lc" ),
    path(f"{API_URL_PREFIX}/person/<int:pk>", PersonAPIView.as_view(), name="person_rud" ),

    # GenericAPIView & Model Mixin
    path(f"{API_URL_PREFIX}/mixin/person/list/", GenericPersonListAPIView.as_view(), name="mixin_list_person" ),
    path(f"{API_URL_PREFIX}/mixin/person/create/", GenericPersonCreateAPIView.as_view(), name="mixin_create_person" ),
    path(f"{API_URL_PREFIX}/mixin/person/retrieve/<int:pk>", GenericPersonRetrieveAPIView.as_view(), name="mixin_retrieve_person" ),
    path(f"{API_URL_PREFIX}/mixin/person/update/<int:pk>", GenericPersonUpdateAPIView.as_view(), name="mixin_update_person" ),
    path(f"{API_URL_PREFIX}/mixin/person/delete/<int:pk>", GenericPersonDeleteAPIView.as_view(), name="mixin_delete_person" ),

    # GenericAPIView Model Mixin Grouping Class URL
    path(f"{API_URL_PREFIX}/mixin/group/person/", GenericPersonLCView.as_view(), name="mixin_lc_person" ),
    path(f"{API_URL_PREFIX}/mixin/group/person/<int:pk>", GenericPersonRUDView.as_view(), name="mixin_rud_person" ),

    # GenericAPIView Class URL
    path(f"{API_URL_PREFIX}/generic/person/", GenericPersonLCView.as_view(), name="generic_lc_person" ),
    path(f"{API_URL_PREFIX}/generic/person/<int:pk>", GenericPersonRUDView.as_view(), name="generic_rud_person" ),

    # Basic authentication & permission class url
    path(f"{API_URL_PREFIX}/basic/auth/", BasicAuthView.as_view(), name="basic_auth" ),

    # Apply custom authentication & permission view url
    path(f"{API_URL_PREFIX}/basic/auth/custom/permission/", ApplyCustomPermissionView.as_view(), name="custom_permission" ),
    path(f"{API_URL_PREFIX}/basic/auth/custom/authentication/", ApplyCustomAuthenticationView.as_view(), name="custom_authentication" ),

    # Using session authentication class url
    path(f"{API_URL_PREFIX}/session/auth/", SessionAuthView.as_view(), name="session_auth" ),
    path(f"{API_URL_PREFIX}/session/login/", LoginView.as_view(), name="session_login" ),

    # viewsets class using routers url
    path(f'{API_URL_PREFIX}/', include(router.urls)),

    # DRF provide obtain_auth_token for user can create own token using command promt.
    path(f"{API_URL_PREFIX}/auth/gettoken/", obtain_auth_token ),

    # Custom token class generate token for user through url
    path(f"{API_URL_PREFIX}/auth/getcustomtoken/", CustomAuthToken.as_view(), name="custom_auth_token" ),

    # Using token authentication varify user in this url
    path(f"{API_URL_PREFIX}/token/auth/", TokenAuthView.as_view(), name="token_auth" ),

    # JWT authentications urls
    path(f'{API_URL_PREFIX}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_URL_PREFIX}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{API_URL_PREFIX}/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Scoped Throttling url
    path(f"{API_URL_PREFIX}/throttling/lc/", ScopedLCThrottlesView.as_view(), name="lc_throttling" ),
    path(f"{API_URL_PREFIX}/throttling/rud/<int:pk>", ScopedRUDThrottlesView.as_view(), name="rud_throttling" ),

    # Filter View Url
    path(f"{API_URL_PREFIX}/filter/", FilterView.as_view(), name="filter" ),
    path(f"{API_URL_PREFIX}/filter/search/", SearchFilterView.as_view(), name="search_filter" ),
    path(f"{API_URL_PREFIX}/filter/ordering/", OrderingFilterView.as_view(), name="ordering_filter" ),
    path(f"{API_URL_PREFIX}/filter/custom/", CustomFilterView.as_view(), name="custom_filter" ),

    # Paginations View Url
    path(f"{API_URL_PREFIX}/pagination/", PaginationView.as_view(), name="pagination" ),
    path(f"{API_URL_PREFIX}/pagination/limitoffset/", LimitOffsetPaginationView.as_view(), name="limitoffset_pagination" ),
    path(f"{API_URL_PREFIX}/pagination/cursor/", CursorPaginationView.as_view(), name="cursor_pagination" ),

    path('', index_view, name='index'),
]