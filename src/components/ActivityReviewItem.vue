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
		card: {
			type: Boolean,
			default: false,
		},
		teacher: {
			type: Boolean,
			default: false,
		},
	},
	data: function () {
		return {
			status: this.setStatus as number,
		};
	},
	created() {
		this.status = this.activity ? this.activity.review_status : this.status;
	},
	computed: {
		reviewColor(): string | null {
			return (
				{ "-1": "error", "0": null, "1": "success" }[String(this.status)] ||
				null
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
		setReviewStatus() {
			this.$emit("edit");
		},
		async resetReviewStatus() {
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT +
					"/teacher/activities/" +
					this.activity.id +
					"/review",
				{
					method: "POST",
					headers: {
						"Content-Type": "application/json",
						"Authorization": "Bearer " + localStorage.token,
					},
					body: JSON.stringify({
						status: 0,
					}),
				},
			);
			this.$emit("edit");
		},
	},
});
</script>

<template>
	<v-card v-if="card" :color="reviewColor">
		<v-card-title>
			<ActivityReviewItem
				:activity="activity"
				:key="activity.id"
				no-icon-color
			/>
			<span class="ml-2">{{ statusName }}</span></v-card-title
		>
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
					>
						Bearbeiten
					</v-btn>
				</template>
				<v-list>
					<v-list-item>
						<v-list-item-title>Annehmen</v-list-item-title>
					</v-list-item>
					<v-list-item>
						<v-list-item-title>Ablehnen</v-list-item-title>
					</v-list-item>
				</v-list>
			</v-menu>
			<v-spacer />
			<v-btn icon v-if="status" @click="resetReviewStatus"
				><v-icon>mdi-delete</v-icon></v-btn
			>
		</v-card-actions>
	</v-card>
	<v-tooltip bottom v-else>
		<template v-slot:activator="{ on, attrs }">
			<v-btn icon v-if="status === 0" v-bind="attrs" v-on="on">
				<v-icon large>mdi-clock-time-eight</v-icon>
			</v-btn>
			<v-btn icon v-else-if="status === 1" v-bind="attrs" v-on="on">
				<v-icon large :color="!noIconColor ? reviewColor : null"
					>mdi-check-circle</v-icon
				>
			</v-btn>
			<v-btn icon v-else-if="status === -1" v-bind="attrs" v-on="on">
				<v-icon large color="!noIconColor ? reviewColor : null"
					>mdi-close-circle</v-icon
				>
			</v-btn>
		</template>
		<span>
			{{ statusName }}
		</span>
	</v-tooltip>
</template>
