<script lang="ts">
import Vue from "vue";
export default Vue.extend({
	name: "UserView",
	data: () => ({
		user: {} as { [key: string]: any },
	}),
	async created() {
		await this.fetchUser(parseInt(this.$route.params.id));
	},
	methods: {
		async fetchUser(id: number) {
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/users/" + id,
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			this.user = await response.json();
		},
	},
});
</script>

<template>
	<div class="wrapper">
		<v-card>
			<v-card-title class="text-h3 mt-4"
				>{{ user.first_name }} {{ user.last_name }}
				<span class="pl-4 grey--text"> (#{{ user.id }})</span></v-card-title
			>
			<v-card-subtitle class="text-h5 mb-4">{{ user.email }}</v-card-subtitle>
		</v-card>
	</div>
</template>
