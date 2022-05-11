<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	props: {
		activity: Object,
	},
});
</script>

<template>
	<v-tooltip bottom>
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
</template>
