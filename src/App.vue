<script lang="ts">
/* import devtools from "@vue/devtools"; */
import Vue from "vue";

import NavDrawer from "@/components/NavDrawer.vue";
import NavBar from "@/components/NavBar.vue";

if (process.env.NODE_ENV === "development") {
	/* devtools.connect(); */
}

export default Vue.extend({
	data: function () {
		return {
			drawerVisible: true,
			appTitle: "Dashboard",
		};
	},
	components: { NavDrawer, NavBar },
});
</script>
<template>
	<div id="app">
		<v-app>
			<NavBar
				:title="appTitle"
				v-if="$router.history.current.name !== 'login'"
				@drawerVisibilityToggle="drawerVisible = !drawerVisible"
			/>
			<NavDrawer
				v-if="$router.history.current.name !== 'login'"
				:visible="drawerVisible"
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
