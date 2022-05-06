<script>
import StudentView from "@/components/StudentView.vue";
import TeacherView from "@/components/TeacherView.vue";

export default {
	name: "HomeView",
	data: function () {
		return { user: {} };
	},
	created() {
		this.user = JSON.parse(sessionStorage.getItem("user"));
		if (this.user == null) this.$router.push("/login");
	},
	components: {
		StudentView,
		TeacherView,
	},
};
</script>

<template>
	<StudentView v-if="user.role === 0" />
	<TeacherView v-else-if="user.role === 1" />
</template>
