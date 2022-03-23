<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "NavBar",
	data: () => ({
		navModel: null,
		navItems: [
			{ title: "Dashboard", icon: "mdi-view-dashboard" },
			{ title: "Entdecken", icon: "mdi-compass" },
			{ title: "Aktivitäten", icon: "mdi-format-list-bulleted-square" },
		],
	}),
	methods: {
		logout() {
			localStorage.removeItem("token");
		},
	},
});
</script>

<template>
	<v-navigation-drawer app v-model="navModel">
		<v-list-item>
			<v-list-item-content>
				<v-list-item-title class="text-h5">
					mint-ec-simplified
				</v-list-item-title>
				<v-list-item-subtitle> subtext </v-list-item-subtitle>
			</v-list-item-content>
		</v-list-item>

		<v-divider />

		<v-list nav>
			<v-list-item v-for="item in navItems" :key="item.title" link>
				<v-list-item-icon>
					<v-icon>{{ item.icon }}</v-icon>
				</v-list-item-icon>

				<v-list-item-content>
					<v-list-item-title>{{ item.title }}</v-list-item-title>
				</v-list-item-content>
			</v-list-item>
		</v-list>

		<v-divider />

		<v-list-item link>
			<v-list-item-icon>
				<v-icon>mdi-account</v-icon>
			</v-list-item-icon>
			<v-list-item-content>
				<v-list-item-title>Account</v-list-item-title>
			</v-list-item-content>
		</v-list-item>
	</v-navigation-drawer>
</template>
