from ..models import JobSeekerCertification
from django.core.exceptions import ValidationError
from ..utils.google_drive import GoogleDriveHelper
from django.db import transaction

class CertificationService:
    @staticmethod
    def add_certification(user_id, certification_data):
        try:
    
            upload_path = certification_data.get('upload_path')
            if upload_path:
                file_id = GoogleDriveHelper.validate_drive_link(upload_path)
                certification_data['upload_path'] = GoogleDriveHelper.generate_embed_link(file_id)
            
          
            certification = JobSeekerCertification.objects.create(
                user_id=user_id, 
                issuer=certification_data.get('issuer'),
                upload_path=certification_data.get('upload_path'),
                awarded_date=certification_data.get('awarded_date'),
                description=certification_data.get('description')
            )
            return certification
            
        except Exception as e:
            with transaction.atomic():
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO jobseeker_certification 
                    (userId, issuer, uploadPath, awardedDate, description)
                    VALUES (%s, %s, %s, %s, %s)
                """, [
                    user_id,
                    certification_data.get('issuer'),
                    certification_data.get('upload_path'),
                    certification_data.get('awarded_date'),
                    certification_data.get('description')
                ])
                return JobSeekerCertification.objects.get(pk=cursor.lastrowid)

    @staticmethod
    def delete_certification(user_id, certification_id):
        try:
            certification = JobSeekerCertification.objects.filter(
                user_id=user_id, 
                id=certification_id
            ).first()
            
            if not certification:
                raise ValidationError("Certification not found")
                
            certification.delete()
            return True
        except Exception as e:
            raise ValidationError(str(e))