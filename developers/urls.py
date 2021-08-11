from developers.tests import DeveloperViewsTest
from developers.views import DeveloperByIdView, DeveloperView
from django.urls import path

urlpatterns = [
    path("developers", DeveloperView.as_view()),
    path("developers/<int:developer_id>", DeveloperByIdView.as_view())
]