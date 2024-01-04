from django.urls import path
from . import views


app_name = 'main'


urlpatterns = [
    path("", views.showdasboard, name="dashboard"),
    path("about/", views.showabout, name="about"),
    path("projects/", views.showproject, name="projects"),
    path("upcoming_events/", views.showevents, name="events"),
    path("contact_us/", views.showcontact, name="contact_us"),
    path("team/", views.showteam, name="team"),
    path("blog/", views.showBlog, name="blog"),
    path("faq/",views.showfaq,name="faq"),
]