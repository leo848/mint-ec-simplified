<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "ActivityView",
	data: function () {
		return {
			activity: {} as { [key: string]: any },
		};
	},
});
</script>

<template>
	<div class="wrapper">
		<h1>Activity View</h1>
	</div>
</template>
