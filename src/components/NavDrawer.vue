<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "NavDrawer",
	data: () => ({
		navItems: [
			{ title: "Dashboard", icon: "mdi-view-dashboard", route: "/" },
			{ title: "Entdecken", icon: "mdi-compass" },
			{
				title: "Aktivitäten",
				icon: "mdi-format-list-bulleted-square",
				route: "/activities",
			},
		],
	}),
	methods: {
		logout() {
			localStorage.removeItem("token");
		},
	},
	props: {
		visible: Boolean,
	},
	computed: {
		navModel: {
			get(): boolean {
				return this.visible;
			},
			set(value: boolean) {
				this.$emit("update:visible", value);
			},
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
			<v-list-item
				v-for="item in navItems"
				:key="item.title"
				:to="item.route"
				link
			>
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
