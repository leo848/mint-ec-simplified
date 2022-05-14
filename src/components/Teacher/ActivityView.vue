<script lang="ts">
import Vue from "vue";
import UserCard from "./UserCard.vue";
import ActivityReviewItem from "../ActivityReviewItem.vue";

export default Vue.extend({
	name: "ActivityView",
	components: { UserCard, ActivityReviewItem },
	data: () => ({
		activity: {} as { [key: string]: any },
		id: 0,
	}),
	async created() {
		this.id = parseInt(this.$route.params.id);
		await this.fetchActivity();
	},
	methods: {
		async fetchActivity() {
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT +
					"/teacher/activities/" +
					this.id +
					"/",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			this.activity = await response.json();
		},
	},
});
</script>

<template>
	<div class="wrapper">
		<v-card>
			<v-card-title class="text-h3 text-center mt-4"
				>{{ activity.title }}
			</v-card-title>
			<v-card-subtitle class="text-h5 pl-4" v-if="activity.category">
				{{ activity.category.title }}
			</v-card-subtitle>
			<v-card-subtitle
				class="text-h6 mb-4 font-weight-regular text--disabled"
				v-html="
					(activity.description || 'Keine erweiterte Beschreibung').replace(
						'\n',
						'<br/>',
					)
				"
			></v-card-subtitle>
			<v-card-text>
				<UserCard :user="activity.created_by" />
			</v-card-text>
			<v-card-actions>
				<ActivityReviewItem
					v-if="activity.id"
					:activity="activity"
					min-width="300px"
					card
					teacher
					@edit="fetchActivity"
				/>
			</v-card-actions>
		</v-card>
	</div>
</template>
