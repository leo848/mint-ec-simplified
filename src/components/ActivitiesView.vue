<script lang="ts">
import Vue from "vue";
import StudentActivitiesView from "./Student/ActivitiesView.vue";
import TeacherActivitiesView from "./Teacher/ActivitiesView.vue";

export default Vue.extend({
	name: "ActivitiesView",
	data: function () {
		return {
			user: {},
		};
	},
	components: { StudentActivitiesView, TeacherActivitiesView },
	created() {
		this.user = JSON.parse(sessionStorage.getItem("user") as string);
	},
});
</script>

<template>
	<StudentActivitiesView v-if="user.role === 0" />
	<TeacherActivitiesView v-else-if="user.role === 1" />
</template>
