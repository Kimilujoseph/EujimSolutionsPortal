# jobseeker/serializers/education_serializer.py
from rest_framework import serializers
from ..models import Education

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'id',
            'institution_name',
            'qualification',
            'degree',
            'field_of_study',
            'start_year',
            'end_year',
            'is_current',
            'description',
            'school_logo',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def validate(self, data):
        if data.get('end_year') and data['start_year'] > data['end_year']:
            raise serializers.ValidationError("End year must be after start year")
        if data.get('is_current') and data.get('end_year'):
            raise serializers.ValidationError("Current education cannot have an end year")
        return data