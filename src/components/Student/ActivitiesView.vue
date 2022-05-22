<script lang="ts">
import Vue from "vue";

import CreateActivityDialog from "../CreateActivityDialog.vue";
import ActivityList from "../ActivityList.vue";

export default Vue.extend({
	name: "ActivitiesView",
	components: { CreateActivityDialog, ActivityList },
	data: () => ({
		user: {},
		activities: [] as { [key: string]: any }[],
		loading: true,
	}),
	async created() {
		this.user = JSON.parse(sessionStorage.getItem("user") as string);
		this.loading = true;
		await this.fetchActivities();
		this.loading = false;
	},
	methods: {
		async fetchActivities() {
			this.loading = true;
			let response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/student/activities/",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			this.activities = await response.json();
			this.loading = false;
		},
	},
	computed: {},
});
</script>

<template>
	<div class="wrapper">
		<h1 class="text-h3 mt-4 mb-4">Deine Aktivitäten</h1>
		<ActivityList :activities="activities" :loading="loading" />
		<CreateActivityDialog @done="fetchActivities" />
	</div>
</template>
