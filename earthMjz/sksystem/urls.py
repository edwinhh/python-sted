from django.urls import path
from . import views
urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('parameter', views.ParameterView.as_view()),
    path('register', views.RegisterView.as_view()),
    path('project', views.ProjectView.as_view()),
    path('interface', views.InterfaceView.as_view()),
    path('case', views.CaseView.as_view()),
    path('get_rely_case', views.RelyCaseView.as_view()),
    path('case_collection', views.CaseCollectionView.as_view()),
    path('join_case', views.JoinCaseView.as_view()),
    path('case_report', views.CaseReportView.as_view()),
    path('report', views.ReportView.as_view()),
    path('collection_report', views.CollectionReport.as_view()),
    path('run', views.CaseRunView.as_view()),
    path('run_collection', views.CollectionRunView.as_view()),
    path('home_page', views.HomePageView.as_view()),
]