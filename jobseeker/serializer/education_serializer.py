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
        if 'start_year' not in data or data['start_year'] < 1900:
            raise serializers.ValidationError("Start year must be provided and cannot be before 1900")
        if 'end_year' in data and data['end_year'] and data['end_year'] < 1900:
            raise serializers.ValidationError("End year cannot be before 1900")
        if 'is_current' in data and data['is_current'] and 'end_year' in data and data['end_year']:
            raise serializers.ValidationError("Current education cannot have an end year")
        if 'degree' not in data or data['degree'] not in dict(Education.DEGREE_CHOICES):
            raise serializers.ValidationError("Degree must be one of the predefined choices")
        if data.get('start_year') and data['start_year'] < 1900:
            raise serializers.ValidationError("Start year must be after 1900")
        if data.get('end_year') and data['end_year'] < 1900:
            raise serializers.ValidationError("End year must be after 1900")
        if data.get('start_year') and data['start_year'] > 2100:
            raise serializers.ValidationError("Start year must be before 2100")
        if data.get('end_year') and data['end_year'] > 2100:
            raise serializers.ValidationError("End year must be before 2100")
        if data.get('end_year') and data['start_year'] > data['end_year']:
            raise serializers.ValidationError("End year must be after start year")
        if 'institution_name' not in data or not data['institution_name'].strip():
            raise serializers.ValidationError("Institution name must be provided")
        if 'qualification' not in data or not data['qualification'].strip():
            raise serializers.ValidationError("Qualification must be provided")
        if 'field_of_study' not in data or not data['field_of_study'].strip():
            raise serializers.ValidationError("Field of study must be provided")
        if data.get('is_current') and data.get('end_year'):
            raise serializers.ValidationError("Current education cannot have an end year")
        return data