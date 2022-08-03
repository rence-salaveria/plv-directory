export interface CourseSubject {
    studentCourse: StudentCourse,
    subjectCode: string,
    subjectTitle: string,
    subjectDescription: string,
}

export interface StudentCourse {
    studentCourseId: number,
    studentCourseName: string
}