<script lang="ts">
import Vue from "vue";
import UserCard from "./UserCard.vue";
import ActivityReviewItem from "../ActivityReviewItem.vue";
import LinkPreview from "../LinkPreview.vue";

export default Vue.extend({
	name: "ActivityView",
	components: { UserCard, ActivityReviewItem, LinkPreview },
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
		formatDate(oldDate: string): string {
			return new Date(oldDate).toLocaleDateString(undefined, {
				weekday: "long",
				year: "numeric",
				month: "long",
				day: "numeric",
			});
		},
	},
	watch: {
		$route() {
			this.fetchActivity();
		},
	},
});
</script>

<template>
	<div class="wrapper">
		<v-row align="stretch"
			><v-col cols="12" md="8">
				<v-card>
					<v-card-title
						class="text-h3 word-wrap mb-2"
						style="word-break: normal"
						>{{ activity.title }}
					</v-card-title>
					<v-card-subtitle class="text-h5 pl-4" v-if="activity.category">
						{{ activity.category.title }} <br />
						{{ formatDate(activity.date) }}
					</v-card-subtitle>
					<v-card-text class="mt-n4">
						<v-chip-group>
							<v-chip disabled v-for="tag in activity.tags" :key="tag.id">
								{{ tag.title }}
							</v-chip>
						</v-chip-group>
					</v-card-text>
					<v-card-subtitle class="text-overline">BESCHREIBUNG</v-card-subtitle>
					<v-card-subtitle
						class="text-h6 mt-n8 mb-4 font-weight-regular text--disabled"
						v-html="
							(activity.description || 'Keine erweiterte Beschreibung').replace(
								'\n',
								'<br/>',
							)
						"
					></v-card-subtitle>
					<v-card-text>
						<UserCard :user="activity.created_by" />
					</v-card-text> </v-card></v-col
			><v-col cols="12" md="4">
				<LinkPreview :url="activity.website" no-preview class="mb-4" />
				<ActivityReviewItem
					v-if="activity.id"
					:activity="activity"
					:key="activity.review_status"
					card
					teacher
					@edit="fetchActivity"
				/> </v-col
		></v-row>
	</div>
</template>
