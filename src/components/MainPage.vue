<script lang="ts">
import Vue from "vue";
import LoginScreen from "./LoginScreen.vue";

export default Vue.extend({
	name: "MainPage",

	components: { LoginScreen },

	data: () => ({
		loggedIn: false,
	}),

	methods: {},
});
</script>

<template>
  <LoginScreen />
</template>
