<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "UserCard",
	props: {
		user: Object,
		search: {
			type: String,
			default: "",
		},
	},
	methods: {
		highlight(user: { [key: string]: any }): string {
			let initialString = `${user.first_name} ${user.last_name}`;
			if (!this.search.length) return initialString;
			return initialString.replace(
				new RegExp(`${this.search}`, "gi"),
				(match) =>
					`<span class="font-weight-bold deep-orange darken-4">${match}</span>`,
			);
		},
		initials(user: { [key: string]: any }): string {
			return user.first_name.charAt(0) + user.last_name.charAt(0);
		},
	},
	computed: {
		notReviewedActivities(): number {
			if (!this.user.created_activities) return 0;
			const amount = this.user.created_activities.filter(
				(a: { [key: string]: any }) => a.review_status === 0,
			).length;
			return amount;
		},
	},
});
</script>

<template>
	<v-card v-if="user" hover :to="'/user/' + user.id">
		<v-card-text class="pa-0 ma-0">
			<v-list-item two-line>
				<v-list-item-icon>
					<v-badge
						color="red"
						:content="notReviewedActivities"
						:value="notReviewedActivities"
						overlap
					>
						<v-avatar size="36" color="primary" class="white--text text-h6">{{
							initials(user)
						}}</v-avatar>
					</v-badge> </v-list-item-icon
				><v-list-item-content
					><v-list-item-title v-html="highlight(user)"> </v-list-item-title>
					<v-list-item-subtitle>
						<span v-if="user.cls">{{ user.grade + user.cls }}</span>
					</v-list-item-subtitle>
				</v-list-item-content>
			</v-list-item></v-card-text
		></v-card
	>
</template>
