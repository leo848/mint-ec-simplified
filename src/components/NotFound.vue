<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "NotFound",
});
</script>

<template>
	<div class="wrapper text-center">
		<h1 class="text-h3 mt-8">Seite nicht gefunden</h1>
		<h2 class="text-h5 text--secondary">{{ $route.fullPath }}</h2>
		<h3 class="font-weight-regular mt-n4 red--text" style="font-size: 250px">
			404
		</h3>
		<v-btn to="/" x-large>Zurück zur Startseite</v-btn>
	</div>
</template>
