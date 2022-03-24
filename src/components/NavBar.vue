<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "NavBar",
	data: () => ({
		navItems: [
			{ title: "Dashboard", icon: "mdi-view-dashboard" },
			{ title: "Entdecken", icon: "mdi-compass" },
			{ title: "Aktivitäten", icon: "mdi-format-list-bulleted-square" },
		],
	}),
	props: {
		title: String,
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
		<v-toolbar-title>{{ title }}</v-toolbar-title>
	</v-app-bar>
</template>
