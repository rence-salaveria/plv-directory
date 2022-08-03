<script lang="ts">
    import type {CourseSubject} from "../lib/types/Course";
    import {studentCourseStore} from "../lib/stores/studentCourseStore";
    import VerticalSpacer from "../lib/components/util/VerticalSpacer.svelte";
    import axios from "$lib/api";
    import {goto} from "$app/navigation";

    let newCourseSubject = {
        student_course: null,
        subject_code: null,
        subject_description: null,
        subject_title: null
    }

    const addSubjectToDatabase = async (e) => {
        try {
            e.preventDefault()
            let response = await axios.post('/add_course', newCourseSubject)
            console.log(response)
        } catch (e) {
            console.log(e)
        }
    }
</script>

<VerticalSpacer height={3} units={"rem"}/>
<div class="d-flex justify-content-center align-items-center">
    <form>
        <div class="mb-3">
            {#await $studentCourseStore}
                <span class="fs-3">Loading data...</span>
            {:then studentCourses}
                <label for="courseDropdown">Student Course</label>
                <select bind:value={newCourseSubject.student_course} class="form-select form-select mb-3"
                        aria-label=".form-select-lg example" id="courseDropdown">
                    <!-- Iterate yung bawat keys       -->
                    <!-- I assign yung value dun sa option value           -->

                    {#each studentCourses as course}
                        <option value={course.studentCourseId}>
                            {course.studentCourseName}
                        </option>
                    {/each}
                </select>
            {:catch err}

            {/await}
        </div>

        <div class="mb-3">
            <label for="subjectCode" class="form-label">Subject Code</label>
            <input type="text" bind:value={newCourseSubject.subject_code} class="form-control" id="subjectCode">
        </div>

        <div class="mb-3">
            <label for="subjectTitle" class="form-label">Subject Title</label>
            <input type="text" bind:value={newCourseSubject.subject_title} class="form-control" id="subjectTitle">
        </div>

        <div class="mb-3">
            <label for="subjectDescription" class="form-label">Subject Description</label>
            <textarea class="form-control" bind:value={newCourseSubject.subject_description} id="subjectDescription" rows="5"></textarea>
        </div>

        <button type="submit" class="btn btn-primary full-width" on:click={addSubjectToDatabase}>Submit</button>

        <VerticalSpacer height={15}/>

        <button type="submit" class="btn btn-primary full-width">Export to Excel</button>
    </form>
</div>


<style>
    .full-width {
        width: 100%
    }
</style>