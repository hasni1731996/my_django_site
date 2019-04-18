from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.views.generic import TemplateView
from companies import views
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.contrib.auth import views as auth_views
 ############if u need to include url against ModelViewSet than u need to do this as here #######
# state_list_view = Model_Viewsets_.as_view({
#             'get':'list',
#             'post':'create'
#             })
#############Ends ----->>>> include this stastate_list_view to any url in url patterns ##########

###########App's Routers are here ##########
router =DefaultRouter()
router.register('model_view_modelviewsets',views.Model_Viewsets_,base_name='router_viewsets')
############Ends ###########
urlpatterns = [
        path('',include(router.urls)),

        path('stock_data/<int:pk>/', views.Detailed_view.as_view()),   #display single instance from model

        path('stocks_compl/', views.StocksList.as_view()), #display all instances from model

        path('state_filteration/', views.Real_state_filters.as_view()), #Get all instances against requested User

        path('getupdateinstance/<int:pk>/', views.Get_single_Instaance_update.as_view()), #Get and update realstatedata model's instance

        path('search_filtering/', views.Search_filtering_backend.as_view()), # search & filtering,ordering here
        

    #     url(r'^user_count_data/$', views.user_count_view),
    #
    #     url(r'^firstview',views.firs_view),
    #
    #     url(r'^testview',views.test_view),
    #
    #     url(r'^redirectview',views.redirect_view),
    #
    #     url(r'^adminmail',views.sendAdminsEmail),
    #
    #     url(r'^statictemp',TemplateView.as_view(template_name = 'firststatic.html')),
    #
    #     #url(r'^$', views.index),
    #
    #     url(r'^getdata/', views.index),
    #
    #     url(r'^signup/', views.signupform),
    #
    #     url(r'^insert', views.insert, name="insert"),
    #
    #     url(r'^multiple_queries/', views.annotation_obj),
    #
    #     url(r'^gettingblog/(?P<id>[0-9]+)/$', views.blog_get),
    #
    #     url(r'^profile/',TemplateView.as_view(template_name = 'profile.html')),
    #
    #     url(r'^saved/', views.SaveProfile, name = 'saved'),
    #
    #     url(r'^cookie_handling/', TemplateView.as_view(template_name = 'cookie.html')),#cookies handling in django
    #
    #     url(r'^get_cookie/(?P<id>[0-9]+)/$', views.cookie_func),        #{{COOKIES HANDLINS AS WELL AS
    #
    #                                                                     #SESSION HANDLING IN DJANGO# }}
    #
    #     url(r'^checking_cookie/', views.cookies_available),
    #
        path(r'^customserializers/(?P<id>[0-9]+)/$', views.customserialization),
    #
    #     url(r'^users/$', views.users_get),
    #
    #     url(r'^bootstrap_gettemp/', TemplateView.as_view(template_name='bootstrap_signup.html')),#template in bootstrap
    #
    #     url(r'^bootstrap_formsubmit/',views.bootstrap_signup_user),
    #
    #     url(r'^logintemplate/', TemplateView.as_view(template_name='login.html')),
    #
    #     url(r'^googlelogin/$', views.googleloginuser,name='googlelogin'),#login user through google
    #
    #     url(r'^auth/complete/google-oauth2/(?P<code>[a-zA-Z0-9!@#$&()\\-`.+,/\"]+)$', views.googleloginuser, name='googlelogin'),
    #
    # #NOTIFICATIONS ULRS HERE<<<>>>>>>>#####
    #
    # url(r'^user_notifications/(?P<reciver>[-\w.,/_\-].+?)/(?P<sender>[-\w.,/_\-].+?)/$', views.first_notifications),
    #
    # url(r'^angular_form/',views.form_submitting),#submitting form usng angular on front end
    #
    # url(r'^angular_form_edit_del/(?P<username>[-\w.,/_\-].+?)/$',views.user_put_del_angular),#put/del user's record
    #
    # url(r'^music_generating/$', views.Getmusic),
    ]
#urlpatterns = format_suffix_patterns(urlpatterns)