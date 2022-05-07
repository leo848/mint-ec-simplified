<script lang="ts">
/* import devtools from "@vue/devtools"; */
import Vue from "vue";

import NavDrawer from "@/components/NavDrawer.vue";
import NavBar from "@/components/NavBar.vue";

export default Vue.extend({
	data: () => ({
		drawerVisible: true,
		appTitle: "Dashboard",
		user: {},
	}),
	async created() {
		const response = await fetch(
			process.env.VUE_APP_BACKEND_ROOT + "/user/me/",
			{
				headers: { Authorization: "Bearer " + localStorage.token },
			},
		);
		if (!response.ok) this.$router.push("/login");
		this.user = await response.json();
	},
	components: { NavDrawer, NavBar },
});
</script>
<template>
	<div id="app">
		<v-app>
			<NavBar
				v-if="$router.history.current.name !== 'login'"
				@drawerVisibilityToggle="drawerVisible = !drawerVisible"
			/>
			<NavDrawer
				v-if="$router.history.current.name !== 'login'"
				:visible="drawerVisible"
				:role="user.role"
				@update:visible="(v) => (drawerVisible = v)"
			/>
			<v-main>
				<v-container fluid>
					<router-view />
				</v-container>
			</v-main>
		</v-app>
	</div>
</template>
