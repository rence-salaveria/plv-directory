import asyncio
from prisma import Prisma


async def add_record():
    prisma = Prisma()
    await prisma.connect()

    new_subject = await prisma.subjects.create(
        data={
            'subject_code': 'PF101',
            'subject_title': 'Object Oriented Programming',
            'subject_description': 'Learn OOP concepts in Java and C#',
            'student_course': 4
        }
    )

    await prisma.disconnect()


if __name__ == '__main__':
    asyncio.run(add_record())
