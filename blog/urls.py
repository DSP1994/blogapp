from . import views
from django.urls import path


urlpatterns = [
    path('blog/', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_details.html'),
    path('like/<slug:slug>', views.BlogLike.as_view(), name='blog_like')
]
