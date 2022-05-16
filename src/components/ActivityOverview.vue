<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "ActivityOverview",
	props: {
		activities: { type: Array },
	},
	data: () => ({
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
			return this.unfilteredOverviewItems.filter(
				(o, i) => overview[o.value] || !i,
			);
		},
	},
});
</script>

<template>
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
</template>
