<script lang="ts">
import Vue from "vue";
import StudentActivityView from "./Student/ActivityView.vue";
import TeacherActivityView from "./Teacher/ActivityView.vue";

export default Vue.extend({
	name: "ActivityView",
	data: function () {
		return {
			user: {},
		};
	},
	components: { StudentActivityView, TeacherActivityView },
	created() {
		this.user = JSON.parse(sessionStorage.getItem("user") as string);
	},
});
</script>

<template>
	<StudentActivityView v-if="user.role === 0" />
	<TeacherActivityView v-else-if="user.role === 1" />
</template>
