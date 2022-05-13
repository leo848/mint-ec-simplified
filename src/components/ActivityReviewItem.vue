<script lang="ts">
import Vue from "vue";

import UserCard from "./Teacher/UserCard.vue";

export default Vue.extend({
	name: "ActivityReviewItem",
	components: { UserCard },
	props: {
		activity: Object,
		noIconColor: {
			type: Boolean,
			default: false,
		},
		card: {
			type: Boolean,
			default: false,
		},
	},
	computed: {
		reviewColor(): string | null {
			return (
				{ "-1": "error", "0": null, "1": "success" }[
					String(this.activity.review_status)
				] || null
			);
		},
		statusName(): string {
			return (
				{
					"-1": "Abgelehnt",
					"0": "Noch nicht bearbeitet",
					"1": "Bestätigt",
				}[String(this.activity.review_status)] || "Unbekannter Status"
			);
		},
	},
});
</script>

<template>
	<v-card v-if="card" :color="reviewColor">
		<v-card-title>
			<ActivityReviewItem
				:activity="activity"
				:key="activity.id"
				no-icon-color
			/>
			<span class="ml-2">{{ statusName }}</span></v-card-title
		>
		<v-card-subtitle v-if="activity.reviewed_by"
			>Bearbeitet von: <UserCard :user="activity.reviewed_by"
		/></v-card-subtitle>
	</v-card>
	<v-tooltip bottom v-else>
		<template v-slot:activator="{ on, attrs }">
			<v-btn icon v-if="activity.review_status === 0" v-bind="attrs" v-on="on">
				<v-icon large>mdi-clock-time-eight</v-icon>
			</v-btn>
			<v-btn
				icon
				v-else-if="activity.review_status === 1"
				v-bind="attrs"
				v-on="on"
			>
				<v-icon large :color="!noIconColor ? reviewColor : null"
					>mdi-check-circle</v-icon
				>
			</v-btn>
			<v-btn
				icon
				v-else-if="activity.review_status === -1"
				v-bind="attrs"
				v-on="on"
			>
				<v-icon large color="!noIconColor ? reviewColor : null"
					>mdi-close-circle</v-icon
				>
			</v-btn>
		</template>
		<span>
			{{ statusName }}
		</span>
	</v-tooltip>
</template>
