# urls.py
from django.urls import path
from .views import LoginView, LogoutView, OfficeUserView, OfficeUserCreateView, OfficeUserUpdateView, OfficerUserView, OfficerUserCreateView, OfficerUserCreateView, OfficerUserUpdateView, SubHeadUserView, SubHeadUserCreateView, SubHeadUserUpdateView, HelperUserView, HelperUserCreateView, HelperUserUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('office_user/', OfficeUserView.as_view(), name='office_user_page'),
    path('office_user/create/', OfficeUserCreateView.as_view(), name='office_user_create'),
    path('office_user/update/', OfficeUserUpdateView.as_view(), name='office_user_update'),
    path('officer_user/', OfficerUserView.as_view(), name='officer_user_page'),
    path('officer_user/create/', OfficerUserCreateView.as_view(), name='officer_user_create'),
    path('officer_user/update/', OfficerUserUpdateView.as_view(), name='officer_user_update'),
    path('sub_head_user/', SubHeadUserView.as_view(), name='sub_head_user_page'),
    path('sub_head_user/create/', SubHeadUserCreateView.as_view(), name='sub_head_user_create'),
    path('sub_head_user/update/', SubHeadUserUpdateView.as_view(), name='sub_head_user_update'),
    path('helper_user/', HelperUserView.as_view(), name='helper_user_page'),
    path('helper_user/create/', HelperUserCreateView.as_view(), name='helper_user_create'),
    path('helper_user/update/', HelperUserUpdateView.as_view(), name='helper_user_update'),
]
