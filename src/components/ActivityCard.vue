<script lang="ts">
import Vue from "vue";
import ActivityReviewItem from "./ActivityReviewItem.vue";

export default Vue.extend({
	name: "ActivityCard",
	components: { ActivityReviewItem },
	props: { activity: Object, teacher: Boolean },
	computed: {
		link(): string | null {
			return this.teacher ? `/activities/${this.activity.id}` : null;
		},
	},
});
</script>

<template>
	<v-card class="mx-auto" :href="link" dense>
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
			<ActivityReviewItem :activity="activity" />
		</v-card-actions>
	</v-card>
</template>
