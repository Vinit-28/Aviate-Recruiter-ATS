# Importing Dependencies #
from ATS.models import Candidate
from rest_framework.views import APIView
from rest_framework.response import Response
from ATS.serializers import CandidateSerializer
from django.db.models import Q, Case, When, Value, IntegerField, Sum, F
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


# View for Candidate Create Operations #
class CandidateListView(ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


# View for Candidate Create Operations #
class CandidateCreateView(CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


# View for Candidate Update Operations #
class CandidateUpdateView(UpdateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


# View for Candidate Delete Operations #
class CandidateDeleteView(DestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


# View for Candidates Search Operations #
class CandidatesSearchView(APIView):
    def get(self, request, searchQuery):
        queryWords = searchQuery.lower().split()
        # Making the Relevance Score Fields #
        relevanceScoreFields = dict()
        relevanceFieldSum = Value(0)
        for idx, word in enumerate(queryWords):
            relevanceScoreFields[f'relevanceCountField_{idx}']=Case(
                When(
                    name__icontains=word, 
                    then=Value(1)            
                ),
                default=Value(0),
                output_field=IntegerField(),
            )
            relevanceFieldSum = relevanceFieldSum + F(f'relevanceCountField_{idx}')

        candidates = Candidate.objects.all().annotate(**relevanceScoreFields)
        # Summing Up the All the Relevance Score Fields & Removing the records having relevance score = 0 #
        candidates = candidates.annotate(
            relevanceScore = relevanceFieldSum
        ).filter(
            relevanceScore__gt=0
        ).order_by(
            '-relevanceScore', 
            'name'
        )
        candidatesSerializer = CandidateSerializer(candidates, many=True)
        return Response(candidatesSerializer.data)
