<script lang="ts">
import Vue from "vue";
import CreateActivityDialog from "./CreateActivityDialog.vue";

export default Vue.extend({
	name: "ActivityView",
	data: () => ({
		user: {},
		activities: [] as { [key: string]: any }[],
		loading: false,
		unfilteredOverviewItems: [
			{
				title: "Gesamte Aktivitäten",
				color: "blue",
				value: "total",
			},
			{
				title: "davon angenommen",
				color: "green",
				value: "accepted",
			},
			{
				title: "davon unbearbeitet",
				color: "secondary",
				value: "other",
			},
			{
				title: "davon abgelehnt",
				color: "red",
				value: "rejected",
			},
		],
	}),
	components: { CreateActivityDialog },
	async created() {
		this.user = JSON.parse(sessionStorage.getItem("user") as string);
		this.loading = true;
		await this.fetchActivities();
		this.loading = false;
	},
	methods: {
		async fetchActivities() {
			let response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/student/activities/",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			this.activities = await response.json();
		},
	},
	computed: {
		activityOverview() {
			return {
				total: this.activities.length,
				accepted: this.activities.filter((a) => a.review_status === 1).length,
				rejected: this.activities.filter((a) => a.review_status === -1).length,
				other: this.activities.filter((a) => a.review_status === 0).length,
			} as { [key: string]: any };
		},
		overviewItems() {
			let overview = this.activityOverview as { [key: string]: any };
			return this.unfilteredOverviewItems.filter((o) => overview[o.value]);
		},
	},
});
</script>

<template>
	<div class="wrapper">
		<h1 class="text-h3 mt-4 mb-4">Deine Aktivitäten</h1>
		<v-row>
			<v-col cols="12">
				<v-card
					><v-card-title class="text-h4 justify-center">Übersicht</v-card-title
					><v-card-text>
						<v-row>
							<v-col v-for="(card, i) in overviewItems" :key="i">
								<v-card :color="card.color" :loading="loading">
									<v-card-title class="text-h2 justify-center">{{
										activityOverview[card.value]
									}}</v-card-title>
									<v-card-subtitle class="text-h6 text-center">{{
										card.title
									}}</v-card-subtitle>
								</v-card>
							</v-col>
						</v-row>
					</v-card-text></v-card
				>
			</v-col>
			<v-col
				cols="12"
				sm="6"
				xl="4"
				v-for="activity in activities"
				:key="activity.id"
			>
				<v-card class="mx-auto" dense>
					<v-card-title> {{ activity.title }} </v-card-title>
					<v-card-subtitle> {{ activity.category.title }} </v-card-subtitle>
					<v-card-text>
						<v-chip-group>
							<v-chip disabled v-for="tag in activity.tags" :key="tag.id">
								{{ tag.title }}
							</v-chip>
						</v-chip-group>
					</v-card-text>
					<v-card-actions>
						<v-tooltip bottom>
							<template v-slot:activator="{ on, attrs }">
								<v-btn
									icon
									v-if="activity.review_status === 0"
									v-bind="attrs"
									v-on="on"
								>
									<v-icon large>mdi-clock-time-eight</v-icon>
								</v-btn>
								<v-btn
									icon
									v-else-if="activity.review_status === 1"
									v-bind="attrs"
									v-on="on"
								>
									<v-icon large color="green">mdi-check-circle</v-icon>
								</v-btn>
								<v-btn
									icon
									v-else-if="activity.review_status === -1"
									v-bind="attrs"
									v-on="on"
								>
									<v-icon large color="red">mdi-close-circle</v-icon>
								</v-btn>
							</template>
							<span>
								{{
									activity.review_status === 0
										? "Noch nicht bearbeitet"
										: activity.review_status === 1
										? "Bestätigt"
										: activity.review_status === -1
										? "Abgelehnt"
										: "Unbekannter Status"
								}}
							</span>
						</v-tooltip>
						<v-spacer />
						<v-btn icon>
							<v-icon>mdi-pencil</v-icon>
						</v-btn>
					</v-card-actions>
				</v-card>
			</v-col>
		</v-row>
		<CreateActivityDialog @done="fetchActivities" />
	</div>
</template>
