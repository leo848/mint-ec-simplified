<script lang="ts">
import Vue from "vue";
import ActivityCard from "../ActivityCard.vue";
import CreateActivityDialog from "../CreateActivityDialog.vue";

export default Vue.extend({
	name: "UserView",
	components: { ActivityCard, CreateActivityDialog },
	data: () => ({
		user: {} as { [key: string]: any },
		activities: [],
	}),
	async created() {
		await this.fetchUser(parseInt(this.$route.params.id));
	},
	methods: {
		async fetchUser(id: number) {
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/teacher/students/" + id + "/",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			this.user = await response.json();
			await this.fetchActivities(id);
		},
		async fetchActivities(id: number) {
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT +
					"/teacher/students/" +
					id +
					"/activities/",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			this.activities = await response.json();
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
		<v-row>
			<v-col
				cols="12"
				sm="6"
				xl="4"
				v-for="activity in activities"
				:key="activity.id"
			>
				<ActivityCard :activity="activity" teacher />
			</v-col>
			<v-col cols="12" sm="6" v-if="activities.length === 0">
				<v-card>
					<v-card-title class="text-h4">Keine Aktivitäten</v-card-title>
				</v-card>
			</v-col>
		</v-row>
		<CreateActivityDialog user="user" teacher />
	</div>
</template>
