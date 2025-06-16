import re
from django.core.exceptions import ValidationError

class GoogleDriveHelper:
    @staticmethod
    def validate_drive_link(link):
        """Validate Google Drive shareable link format"""
        pattern = r'^https:\/\/drive\.google\.com\/.*\/d\/([^\/]+)(?:\/.*)?$'
        match = re.match(pattern, link)
        if not match:
            raise ValidationError("Invalid Google Drive link format")
        return match.group(1)  # Returns file ID

    @staticmethod
    def generate_embed_link(file_id):
        """Generate embeddable view link from file ID"""
        return f"https://drive.google.com/file/d/{file_id}/preview"