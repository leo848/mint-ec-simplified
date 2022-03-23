<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "StudentView",
	data: () => ({
		user: {},
	}),
	created() {
		this.user = JSON.parse(sessionStorage.getItem("user") as string);
	},
	methods: {},
});
</script>

<template>
	<v-container fluid>
		<h1>Willkommen, {{ user.display_name }}!</h1>
	</v-container>
</template>
