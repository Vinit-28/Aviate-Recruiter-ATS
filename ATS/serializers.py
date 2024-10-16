# Importing Dependencies #
from rest_framework import serializers
from ATS.models import Candidate, Gender


# Candidate Serializer #
class CandidateSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=Gender.choices)
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'age', 'gender', 'email', 'phoneNumber']