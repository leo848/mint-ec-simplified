<script lang="ts">
import Vue from "vue";
import CreateActivityDialog from "../CreateActivityDialog.vue";
import ActivityList from "../ActivityList.vue";

export default Vue.extend({
	name: "UserView",
	components: { ActivityList, CreateActivityDialog },
	data: () => ({
		user: {} as { [key: string]: any },
		loading: false,
		id: 0,
		activities: [],
	}),
	async created() {
		this.id = parseInt(this.$route.params.id);
		await this.fetchUser();
	},
	methods: {
		async fetchUser() {
			this.loading = true;
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/teacher/students/" + this.id + "/",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			this.user = await response.json();
			await this.fetchActivities();
			this.loading = false;
		},
		async fetchActivities() {
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT +
					"/teacher/students/" +
					this.id +
					"/activities/",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			this.activities = await response.json();
		},
	},
	watch: {
		$route() {
			this.fetchUser();
		},
	},
});
</script>

<template>
	<div class="wrapper">
		<v-card>
			<v-card-title class="text-h3 mt-4"
				>{{ user.first_name }} {{ user.last_name }}
				<span class="pl-4 grey--text">
					({{ user.grade }}<span v-if="user.cls">{{ user.cls }}</span
					>)</span
				></v-card-title
			>
			<v-card-subtitle class="text-h5 mb-4">{{ user.email }}</v-card-subtitle>
		</v-card>
		<ActivityList :activities="activities" :loading="loading" />
		<CreateActivityDialog :user="user" @done="fetchActivities" teacher />
	</div>
</template>
