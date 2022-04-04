<script lang="ts">
import Vue from "vue";
import LoginScreen from "./LoginScreen.vue";
import StudentView from "./StudentView.vue";
import NavDrawer from "./NavDrawer.vue";
import NavBar from "./NavBar.vue";

export default Vue.extend({
	name: "MainPage",

	components: { NavBar, NavDrawer, LoginScreen, StudentView },

	data: () => ({
		loggedIn: false,
		drawerVisible: true,
		appTitle: "Dashboard",
	}),

	methods: {},
});
</script>

<template>
	<v-app>
		<NavBar
			v-if="loggedIn"
			:title="appTitle"
			@drawerVisibilityToggle="drawerVisible = !drawerVisible"
		/>
		<NavDrawer
			v-if="loggedIn"
			:visible="drawerVisible"
			@update:visible="(v) => (drawerVisible = v)"
		/>
		<v-main>
			<!-- <router-view> -->
			<LoginScreen v-if="!loggedIn" @done="() => (loggedIn = true)" />
			<StudentView v-else />
		</v-main>
	</v-app>
</template>
