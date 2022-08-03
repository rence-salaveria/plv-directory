from prisma import Prisma
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from prisma.models import subjects
from prisma.partials import SubjectInformation

app = FastAPI()

# === TRUSTED HOSTS/REQUEST ORIGINS ===

origins = ['http://127.0.0.1:5173']

# === ADD MIDDLEWARE TO APPLICATION ===

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.get('/courses')
def get_courses():
    return {'courses': 'Hawo'}


@app.post('/add_course')
async def add_course(subject_info: SubjectInformation):
    prisma = Prisma()
    await prisma.connect()
    new_subject = await prisma.subjects.create(
        data={
            'subject_code': subject_info.subject_code,
            'subject_title': subject_info.subject_title,
            'subject_description': subject_info.subject_description,
            'student_course': subject_info.student_course
        }
    )
    await prisma.disconnect()
    return new_subject


@app.get('/export/excel')
async def export_to_excel():
    # logic to edit the excel
    # get the actual file
    pass
