from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services.job_posting_skill_service import JobPostingSkillService
from ..serializer import JobPostingSkillSerializer
from ..permission import recruiter_required

service  = JobPostingSkillService()

class JobPostingAddingRequiredSkills(APIView):
    @recruiter_required
    def post(self,request,job_posting_id):
        if not request.data or not isinstance(request.data,dict):
            Response({"details":"please provide valid skill data"},status=status.HTTP_400_BAD_REQUEST)
        serializer = JobPostingSkillSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        print(serializer.validated_data)  
        skillAdded = service.add_required_skills(job_posting_id,serializer.validated_data)
        return Response({"sucessfully added the course"},status=status.HTTP_200_OK)
        
    def delete(self,request,job_posting_id,skill_id):
        if not job_posting_id or not skill_id:
            return Response({"details":"please provide valid job posting id and skill id"},status=status.HTTP_400_BAD_REQUEST)
        service.delete_required_skill(job_posting_id,skill_id)
        return Response({"details":"sucessfully deleted the skill from the job posting"},status=status.HTTP_200_OK)
