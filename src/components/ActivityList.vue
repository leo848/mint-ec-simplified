<script lang="ts">
import Vue from "vue";

import ActivityOverview from "./ActivityOverview.vue";
import ActivityCard from "./ActivityCard.vue";

export default Vue.extend({
	name: "ActivityList",
	components: { ActivityCard, ActivityOverview },
	props: {
		activities: {
			type: Array,
			required: true,
		},
		loading: {
			type: Boolean,
			default: false,
		},
	},
});
</script>

<template>
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
			<ActivityCard :activity="activity" teacher />
		</v-col>
		<v-col cols="12" sm="6" v-if="activities.length === 0">
			<v-card>
				<v-card-title class="text-h4">Keine Aktivitäten</v-card-title>
			</v-card>
		</v-col>
	</v-row>
</template>
