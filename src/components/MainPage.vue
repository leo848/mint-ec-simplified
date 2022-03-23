<script lang="ts">
import Vue from "vue";
import LoginScreen from "./LoginScreen.vue";
import StudentView from "./StudentView.vue";
import NavBar from "./NavBar.vue";

export default Vue.extend({
	name: "MainPage",

	components: { NavBar, LoginScreen, StudentView },

	data: () => ({
		loggedIn: false,
	}),

	methods: {},
});
</script>

<template>
	<v-app>
		<NavBar v-if="loggedIn" />
		<v-main>
			<LoginScreen v-if="!loggedIn" @done="() => (loggedIn = true)" />
			<StudentView v-else />
		</v-main>
	</v-app>
</template>
