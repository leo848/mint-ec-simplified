<script lang="ts">
import Vue from "vue";
export default Vue.extend({
	name: "StudentsView",
	data: () => ({
		user: {} as { [key: string]: any },
		loading: false,
		search: "",
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
		studentSearched(student: { [key: string]: any }): boolean {
			return `${student.first_name} ${student.last_name} ${student.grade}${student.cls}`
				.toLowerCase()
				.includes(this.search.toLowerCase());
		},
		highlight(student: { [key: string]: any }): string {
			let initialString = `${student.first_name} ${student.last_name}`;
			if (!this.search.length) return initialString;
			return initialString.replace(
				new RegExp(`${this.search}`, "gi"),
				(match) =>
					`<span class="font-weight-bold deep-orange darken-4">${match}</span>`,
			);
		},
		initials(student: { [key: string]: any }): string {
			return student.first_name.charAt(0) + student.last_name.charAt(0);
		},
	},
	computed: {
		requiredGrades() {
			return this.grades.filter(
				(grade: { number: number; string: string }): boolean =>
					this.students.some(
						(student: { [key: string]: any }): boolean =>
							student.grade === grade.number && this.studentSearched(student),
					),
				0,
			);
		},
	},
});
</script>

<template>
	<div class="wrapper">
		<v-toolbar rounded elevation="4" class="mb-4">
			<v-text-field
				v-model="search"
				hide-details
				prepend-icon="mdi-magnify"
				single-line
				clearable
				placeholder="Filtern..."
			/>
		</v-toolbar>
		<v-row>
			<v-col
				cols="12"
				sm="6"
				md="4"
				v-for="grade in requiredGrades"
				:key="grade.number"
				class="class-card md-4"
			>
				<v-card>
					<v-card-title class="text-h3">{{ grade.string }}</v-card-title>
					<v-card-text>
						<v-list>
							<v-list-item
								two-line
								v-for="student in students
									.filter((s) => s.grade === grade.number)
									.filter((s) => studentSearched(s))"
								:key="student.id"
								:href="'/user/' + student.id"
							>
								<v-list-item-avatar
									><v-avatar color="primary" class="white--text text-h6">{{
										initials(student)
									}}</v-avatar></v-list-item-avatar
								><v-list-item-content
									><v-list-item-title v-html="highlight(student)">
									</v-list-item-title>
									<v-list-item-subtitle>
										<span v-if="student.cls">{{
											student.grade + student.cls
										}}</span>
									</v-list-item-subtitle>
								</v-list-item-content>
							</v-list-item></v-list
						>
					</v-card-text>
				</v-card>
			</v-col></v-row
		>
	</div>
</template>
