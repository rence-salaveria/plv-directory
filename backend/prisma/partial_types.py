from prisma.models import subjects

subjects.create_partial('SubjectInformation', include={
    'subject_code',
    'subject_title',
    'subject_description',
    'student_course'
})