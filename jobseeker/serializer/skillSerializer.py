from rest_framework import serializers
from ...skills.models import Skill,SkillSet  

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skill_name', 'description']
        read_only_fields = ['id']


class SkillSetSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()
    
    class Meta:
        model = SkillSet
        fields = [
            'id',
            'skill',
            'proficiency_level',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        skill_data = validated_data.pop('skill')
        skill_serializer = SkillSerializer(data=skill_data)
        
        if skill_serializer.is_valid():
            skill = skill_serializer.save()
            return SkillSet.objects.create(
                skill=skill,
                user_id=self.context['request'].user.id,
                **validated_data
            )
        else:
            raise serializers.ValidationError(skill_serializer.errors)

class SkillSetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillSet
        fields = [
            'skill_id',
            'proficiency_level'
        ]
        
    def validate_skill_id(self, value):
        from ..models import Skill
        if not Skill.objects.filter(id=value).exists():
            raise serializers.ValidationError("Skill does not exist")
        return value