import {readable} from "svelte/store";
import type {StudentCourse} from "../types/Course";

let emptyCourses: StudentCourse[] = []

const courses: StudentCourse[] = [
    {
        studentCourseId: 1,
        studentCourseName: "Bachelor of Early Childhood Education"
    },
    {
        studentCourseId: 2,
        studentCourseName: "Bachelor of Secondary Education Major in English"
    },
    {
        studentCourseId: 3,
        studentCourseName: "BS Civil Engineering"
    },
    {
        studentCourseId: 4,
        studentCourseName: "BS Information Technology"
    },
    {
        studentCourseId: 5,
        studentCourseName: "BS Accountancy"
    }
]

export const studentCourseStore = readable(emptyCourses, function(set) {
    set(courses);
    return function stop() {
        console.log('Ended Transaction');
    }
})