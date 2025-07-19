from rest_framework import serializers
from ..models import Education

class EducationSerializer(serializers.ModelSerializer):
    end_year = serializers.IntegerField(required=False, allow_null=True)
    
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
        required_fields = ['institution_name', 'qualification', 'field_of_study', 'degree']
        for field in required_fields:
            if field not in data or not str(data[field]).strip():
                raise serializers.ValidationError(f"{field.replace('_', ' ').title()} must be provided")
        
        # Validate degree choice
        if data['degree'] not in dict(Education.DEGREE_CHOICES):
            raise serializers.ValidationError("Degree must be one of the predefined choices")
        
        # Validate start year
        if 'start_year' not in data:
            raise serializers.ValidationError("Start year must be provided")
        
        if not (1900 <= data['start_year'] <= 2100):
            raise serializers.ValidationError("Start year must be between 1900 and 2100")
        
        if data.get('is_current', False):
            data['end_year'] = None  # Force end_year to be None if is_current is True
        elif 'end_year' in data and data['end_year'] is not None:
            if not (1900 <= data['end_year'] <= 2100):
                raise serializers.ValidationError("End year must be between 1900 and 2100")
            if data['start_year'] > data['end_year']:
                raise serializers.ValidationError("End year must be after start year")
        else:
            if not data.get('is_current', False):
                raise serializers.ValidationError("Either end year or 'is current' must be provided")
        
        return data