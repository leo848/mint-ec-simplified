<script lang="ts">
import Vue from "vue";
import MainPage from "./components/MainPage.vue";

export default Vue.extend({
	name: "App",

	components: {
		MainPage,
	},

	data: () => ({
		//
	}),
});
</script>

<template>
	<MainPage />
</template>
