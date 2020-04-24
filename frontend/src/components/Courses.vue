<!-- src/components/Courses.vue -->

<template>
    <div class="container">
        <h1>Courses</h1>
        <hr>
        <button type="button" class="btn btn-success btn-sm">Add Course</button>
        <table class="table table-hover">
            <tr>
                <th scope="col">Title</th>
                <th scope="col">Author</th>
                <th scope="col">Paperback</th>
            </tr>
            <tbody>
            <tr v-for="(course, index) in courses" :key="index">
                <td>{{ course.title }}</td>
                <td>{{ course.author }}</td>
                <td>
                <span v-if="course.paperback">Yes</span>
                <span v-else>No</span>
                </td>
                <td>
                <button type="button" class="btn btn-info btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<template>
<b-modal ref="addCourseModal"
         id="course-modal"
         title="Add a new course"
         hide-footer>
  <b-form @submit="onSubmit" @reset="onReset" class="w-100">
  <b-form-group id="form-title-group"
                label="Title:"
                label-for="form-title-input">
      <b-form-input id="form-title-input"
                    type="text"
                    v-model="addCourseForm.title"
                    required
                    placeholder="Enter title">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-author-group"
                  label="Author:"
                  label-for="form-author-input">
        <b-form-input id="form-author-input"
                      type="text"
                      v-model="addCourseForm.author"
                      required
                      placeholder="Enter author">
        </b-form-input>
      </b-form-group>
    <b-form-group id="form-read-group">
      <b-form-checkbox-group v-model="addCourseForm.paperback" id="form-checks">
        <b-form-checkbox value="true">Paperback</b-form-checkbox>
      </b-form-checkbox-group>
    </b-form-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>
  </b-form>
</b-modal>
</template>


 <script>
 import axios from 'axios';
 export default {
  data() {
    return {
      courses: [],
    };
  },
  methods: {
    getCourses() {
      const path = 'http://localhost:5000/courses';
      axios.get(path)
        .then((res) => {
          this.courses = res.data.courses;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getCourses();
  },
 };
 </script>