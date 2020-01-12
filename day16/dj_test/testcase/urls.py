from django.urls import path
from . import views,views_new,view3

urlpatterns = [
    # path('add_case_set',views.case_set),
    # path('case_set',views.case_set_all),
    #
    path('case_set_new',views_new.CaseSet.as_view()),
    # path('case',views_new.CaseView.as_view()),

    path('project',view3.ProjectView.as_view()),
    path('case',view3.CaseView.as_view()),

    path("login",view3.LoginView.as_view())

]