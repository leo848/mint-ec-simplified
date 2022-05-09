<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "NavDrawer",
	data: () => ({
		user: {} as { [key: string]: any },
		preNavItems: [
			{
				title: "Dashboard",
				icon: "mdi-view-dashboard",
				route: "/",
				visibleFor: [0, 1],
			},
			{ title: "Entdecken", icon: "mdi-compass", visibleFor: [0, 1] },
			{
				title: "Aktivitäten",
				icon: "mdi-format-list-bulleted-square",
				route: "/activities",
				visibleFor: [0, 1],
			},
			{
				title: "Schüler",
				icon: "mdi-account-school",
				route: "/students",
				visibleFor: [1],
			},
		],
	}),
	created() {
		this.user = JSON.parse(sessionStorage.getItem("user") as string);
	},
	methods: {
		logout() {
			localStorage.removeItem("token");
		},
	},
	props: {
		visible: Boolean,
		role: Number,
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

		navItems(): { title: string; icon: string; route?: string }[] {
			return this.preNavItems.filter((i) =>
				i.visibleFor.includes(this.user.role),
			);
		},

		subtitle(): string {
			return ["Schüleransicht", "Lehreransicht", "Adminansicht"][
				(this.role as number) || 0
			];
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
				<v-list-item-subtitle> {{ subtitle }} </v-list-item-subtitle>
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

		<v-list nav>
			<v-list-item to="/account" link>
				<v-list-item-icon>
					<v-icon>mdi-account</v-icon>
				</v-list-item-icon>
				<v-list-item-content>
					<v-list-item-title>Account</v-list-item-title>
				</v-list-item-content>
			</v-list-item>
		</v-list>
	</v-navigation-drawer>
</template>
