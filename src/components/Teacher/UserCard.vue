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
});
</script>

<template>
	<v-list-item two-line :href="'/user/' + user.id">
		<v-list-item-avatar
			><v-avatar color="primary" class="white--text text-h6">{{
				initials(user)
			}}</v-avatar></v-list-item-avatar
		><v-list-item-content
			><v-list-item-title v-html="highlight(user)"> </v-list-item-title>
			<v-list-item-subtitle>
				<span v-if="user.cls">{{ user.grade + user.cls }}</span>
			</v-list-item-subtitle>
		</v-list-item-content>
	</v-list-item>
</template>
