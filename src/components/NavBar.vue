<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "NavBar",
	data: () => ({}),
	created() {
		console.log(this.$route);
	},
	methods: {
		logout() {
			localStorage.removeItem("token");
		},
	},
});
</script>

<template>
	<v-app-bar app>
		<v-app-bar-nav-icon
			@click="$emit('drawerVisibilityToggle')"
		></v-app-bar-nav-icon>
		<v-toolbar-title>{{ $route.meta.title }}</v-toolbar-title>
	</v-app-bar>
</template>
