<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "ActivityView",
	data: () => ({
		activity: {} as { [key: string]: any },
	}),
	async created() {
		await this.fetchActivity(parseInt(this.$route.params.id));
	},
	methods: {
		async fetchActivity(id: number) {
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/teacher/activities/" + id + "/",
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
			<v-card-title class="text-h3 mt-4">{{ activity.title }} </v-card-title>
			<v-card-subtitle class="pl-4 grey--text">
				{{ activity.category.title }}
			</v-card-subtitle>
			<v-card-subtitle
				class="text-h5 mb-4"
				v-html="activity.description.replace('\n', '<br/>')"
			></v-card-subtitle>
		</v-card>
	</div>
</template>
