from django.core.exceptions import ValidationError


def validate_file_extention(value):
    import os
    ext = os.path.splitext(value.name)[1]  # gets file extension from the filename
    valid_extentions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extentions:
        raise ValidationError('Unsupported file extension. Allowed extensions are .pdf, .doc, .docx')