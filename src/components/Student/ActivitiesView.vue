<script lang="ts">
import Vue from "vue";
import CreateActivityDialog from "../CreateActivityDialog.vue";
import ActivityCard from "../ActivityCard.vue";
import ActivityOverview from "../ActivityOverview.vue";

export default Vue.extend({
	name: "ActivitiesView",
	components: { CreateActivityDialog, ActivityCard, ActivityOverview },
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
		<v-row>
			<v-col cols="12">
				<ActivityOverview :activities="activities" v-if="!loading" />
				<v-skeleton-loader v-else type="image" />
			</v-col>
			<v-col
				cols="12"
				sm="6"
				xl="4"
				v-for="activity in activities"
				:key="activity.id"
			>
				<ActivityCard :activity="activity" />
			</v-col>
		</v-row>
		<CreateActivityDialog @done="fetchActivities" />
	</div>
</template>
