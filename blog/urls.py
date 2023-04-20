from . import views
from django.urls import path


urlpatterns = [
    path('blog/', views.BlogList.as_view(), name='blog'),
    path('post/', views.PostList.as_view(), name='post'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='open_post'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('update/<slug:slug>', views.UpdateView.as_view(), name='edit_post'),
    path('delete/<slug:slug>', views.DeleteView.as_view(), name='delete_post'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_details.html'),
    path('like/<slug:slug>', views.BlogLike.as_view(), name='blog_like'),
    path('profile/', views.ProfilePage.as_view(), name='profile_page'),

]
