# Importing Dependencies #
from django.urls import path
from ATS.views import CandidateListView, CandidateCreateView, CandidateUpdateView, CandidateDeleteView, CandidatesSearchView

# App Name Configuration #
app_name = 'ATS'

# URL Patterns for App ATS #
urlpatterns = [
    path('candidates/list/', CandidateListView.as_view(), name='CandidateListView'),
    path('candidate/create/', CandidateCreateView.as_view(), name='CandidateCreateView'),
    path('candidate/update/<int:pk>', CandidateUpdateView.as_view(), name='CandidateUpdateView'),
    path('candidate/delete/<int:pk>', CandidateDeleteView.as_view(), name='CandidateDeleteView'),
    path('candidates/search/<searchQuery>', CandidatesSearchView.as_view(), name='CandidatesSearchView'),
]