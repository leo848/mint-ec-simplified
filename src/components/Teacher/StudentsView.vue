<script lang="ts">
import Vue from "vue";
export default Vue.extend({
	name: "StudentsView",
	data: function () {
		return { user: {} as { [key: string]: any } };
	},
	created() {
		if (JSON.parse(sessionStorage.getItem("user") as string).role !== 1)
			this.$router.replace("/");
	},
});
</script>

<template>
	<p>All users</p>
</template>
