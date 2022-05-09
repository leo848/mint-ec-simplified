<script lang="ts">
import Vue from "vue";
export default Vue.extend({
	name: "StudentsView",
	data: () => ({
		user: {} as { [key: string]: any },
		loading: false,
		students: [],
		grades: [
			{ number: 5, string: "5" },
			{ number: 6, string: "6" },
			{ number: 7, string: "7" },
			{ number: 8, string: "8" },
			{ number: 9, string: "9" },
			{ number: 10, string: "EF" },
			{ number: 11, string: "Q1" },
			{ number: 12, string: "Q2" },
		],
	}),
	async created() {
		if (JSON.parse(sessionStorage.getItem("user") as string).role !== 1)
			this.$router.replace("/");
		await this.fetchStudents();
	},
	methods: {
		async fetchStudents() {
			this.loading = true;
			let response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/teacher/students/",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			this.students = await response.json();
			this.loading = false;
		},
	},
	computed: {
		requiredGrades() {
			return this.grades.filter(
				(g: { number: number; string: string }) =>
					this.students.some(
						(s: { [key: string]: any }) => s.grade === g.number,
					),
				0,
			);
		},
	},
});
</script>

<template>
	<div class="wrapper">
		<v-row>
			<v-col
				cols="12"
				md="6"
				v-for="grade in requiredGrades"
				:key="grade.number"
				class="class-card md-4"
			>
				<v-card>
					<v-card-title class="text-h3">{{ grade.string }}</v-card-title>
					<v-card-text>
						<v-row
							><v-col
								cols="6"
								v-for="student in students.filter(
									(s) => s.grade === grade.number,
								)"
								:key="student.id"
								><v-card
									><v-card-text
										><v-avatar
											color="primary"
											class="font-weight-bold text-h5"
											>{{
												student.first_name.charAt(0) +
												student.last_name.charAt(0)
											}}</v-avatar
										></v-card-text
									><v-card-title
										>{{ student.first_name }}
										{{ student.last_name }}</v-card-title
									></v-card
								></v-col
							></v-row
						>
					</v-card-text>
				</v-card>
			</v-col></v-row
		>
	</div>
</template>
