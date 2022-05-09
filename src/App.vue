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
			<v-fade-transition hide-on-leave>
				<NavDrawer
					v-if="$router.history.current.name !== 'login'"
					:visible="drawerVisible"
					:role="user.role"
					@update:visible="(v) => (drawerVisible = v)"
			/></v-fade-transition>
			<v-main>
				<v-container fluid>
					<v-slide-x-reverse-transition hide-on-leave>
						<router-view />
					</v-slide-x-reverse-transition>
				</v-container>
			</v-main>
		</v-app>
	</div>
</template>
