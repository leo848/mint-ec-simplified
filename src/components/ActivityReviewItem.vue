<script lang="ts">
import Vue from "vue";

import UserCard from "./Teacher/UserCard.vue";

export default Vue.extend({
	name: "ActivityReviewItem",
	components: { UserCard },
	props: {
		activity: Object,
		setStatus: {
			type: Number,
			default: 0,
		},
		noIconColor: {
			type: Boolean,
			default: false,
		},
		noTooltip: {
			type: Boolean,
			default: false,
		},
		card: {
			type: Boolean,
			default: false,
		},
		teacher: {
			type: Boolean,
			default: false,
		},
		minWidth: String,
	},
	data: function () {
		return {
			status: this.setStatus as number,
			loading: false,
		};
	},
	created() {
		this.status = this.activity ? this.activity.review_status : this.status;
	},
	computed: {
		reviewColor(): string | null {
			return (
				{ "-1": "red", "0": null, "1": "success" }[String(this.status)] || null
			);
		},
		statusName(): string {
			return (
				{
					"-1": "Abgelehnt",
					"0": "Noch nicht bearbeitet",
					"1": "Bestätigt",
				}[String(this.status)] || "Unbekannter Status"
			);
		},
	},
	methods: {
		async setReviewStatus(status: number) {
			this.loading = true;
			await fetch(
				process.env.VUE_APP_BACKEND_ROOT +
					"/teacher/activities/" +
					this.activity.id +
					"/review/",
				{
					method: "POST",
					headers: {
						"Content-Type": "application/json",
						"Authorization": "Bearer " + localStorage.token,
					},
					body: JSON.stringify({
						status: status,
					}),
				},
			);
			this.loading = false;
			this.$emit("edit");
		},
		async resetReviewStatus() {
			await this.setReviewStatus(0);
		},
	},
});
</script>

<template>
	<v-card
		v-if="card"
		:loading="loading"
		loading-height="20"
		:min-width="minWidth"
		:color="reviewColor"
	>
		<v-card-title>
			<ActivityReviewItem
				:activity="activity"
				:key="activity.id"
				no-icon-color
				no-tooltip />
			<span class="ml-4">{{ statusName }}</span>
			<v-spacer
		/></v-card-title>
		<v-card-subtitle class="mt-1" v-if="activity.reviewed_by"
			>Bearbeitet von: <UserCard :user="activity.reviewed_by"
		/></v-card-subtitle>
		<v-card-actions v-if="teacher">
			<v-menu offset-y>
				<template v-slot:activator="{ on, attrs }">
					<v-btn
						v-on="on"
						v-bind="attrs"
						:color="reviewColor + ' darken-2'"
						x-large
						v-if="!status"
					>
						Bearbeiten
					</v-btn>
					<v-btn fab v-on="on" v-bind="attrs" v-else
						><v-icon>mdi-pencil</v-icon></v-btn
					>
				</template>
				<v-list>
					<v-list-item @click="setReviewStatus(1)">
						<v-list-item-title>Annehmen</v-list-item-title>
						<v-list-item-icon
							><ActivityReviewItem :set-status="1" no-tooltip
						/></v-list-item-icon>
					</v-list-item>
					<v-list-item @click="setReviewStatus(-1)">
						<v-list-item-title>Ablehnen</v-list-item-title>
						<v-list-item-icon
							><ActivityReviewItem :set-status="-1" no-tooltip
						/></v-list-item-icon>
					</v-list-item>
				</v-list>
			</v-menu>
			<v-spacer />
			<v-btn fab v-if="status" @click="resetReviewStatus"
				><v-icon>mdi-delete</v-icon></v-btn
			>
		</v-card-actions>
	</v-card>
	<v-tooltip bottom :disabled="noTooltip" v-else>
		<template v-slot:activator="{ on, attrs }">
			<v-btn icon v-if="status === 0" v-bind="attrs" v-on="on">
				<v-icon large :color="!noIconColor ? reviewColor : null"
					>mdi-clock-time-eight</v-icon
				>
			</v-btn>
			<v-btn icon v-else-if="status === 1" v-bind="attrs" v-on="on">
				<v-icon large :color="!noIconColor ? reviewColor : null"
					>mdi-check-circle</v-icon
				>
			</v-btn>
			<v-btn icon v-else-if="status === -1" v-bind="attrs" v-on="on">
				<v-icon large :color="!noIconColor ? reviewColor : null"
					>mdi-close-circle</v-icon
				>
			</v-btn>
		</template>
		<span>
			{{ statusName }}
		</span>
	</v-tooltip>
</template>
