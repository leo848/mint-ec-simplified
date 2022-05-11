<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "NavBar",
	data: () => ({}),
	created() {
		const darkMode = localStorage.getItem("darkMode");
		if (darkMode === null) {
			this.$vuetify.theme.dark = false;
			this.toggleMode();
		} else {
			this.$vuetify.theme.dark = JSON.parse(darkMode);
		}
	},
	methods: {
		logout() {
			localStorage.removeItem("token");
		},
		toggleMode() {
			this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
			localStorage.setItem(
				"darkMode",
				JSON.stringify(this.$vuetify.theme.dark),
			);
		},
	},
});
</script>

<template>
	<v-app-bar app elevate-on-scroll>
		<v-app-bar-nav-icon
			@click="$emit('drawerVisibilityToggle')"
		></v-app-bar-nav-icon>
		<v-toolbar-title>{{ $route.meta.title }}</v-toolbar-title>
		<v-spacer />
		<v-btn icon @click="toggleMode"><v-icon>mdi-brightness-6</v-icon></v-btn>
	</v-app-bar>
</template>
