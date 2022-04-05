<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "StudentView",
	data: () => ({
		user: {},
		cards: [
			{
				title: "Aktivitäten",
				description:
					"Sehe den Status deiner Aktivitäten ein oder füge neue hinzu.",
				color: "red darken-3",
				icon: "mdi-format-list-bulleted-square",
			},
			{
				title: "Entdecken",
				description:
					"Hier kannst du neue Möglichkeiten entdecken, um Punkte zu verdienen.",
				color: "blue darken-3",
				icon: "mdi-compass",
			},
			{
				title: "Status",
				description: "Sehe den Status deines Mint-EC-Zertifikats ein.",
				color: "green darken-3",
				icon: "mdi-counter",
			},
			{
				title: "Platzhalter",
				description:
					"Vestibulum condimentum dui et elit. Pellentesque porttitor ipsum at ipsum. Nam.",
				icon: "mdi-script-text",
			},
		],
	}),
	created() {
		this.user = JSON.parse(sessionStorage.getItem("user") as string);
	},
	methods: {},
});
</script>

<template>
	<div class="wrapper">
		<h1 class="text-h3 mt-4 mb-4">Willkommen, {{ user.display_name }}!</h1>
		<v-alert type="info" text dismissible dense
			>Keine neuen Benachrichtigungen.</v-alert
		>
		<v-row>
			<v-col v-for="(card, i) in cards" :key="i" cols="12" sm="6">
				<v-card :color="card.color" height="200px" hover>
					<v-card-title class="text-h4 mb-4">
						{{ card.title }}
						<v-spacer />
						<v-icon x-large>{{ card.icon }}</v-icon>
					</v-card-title>
					<v-card-subtitle class="subtitle-1">
						{{ card.description }}
					</v-card-subtitle>
				</v-card>
			</v-col>
		</v-row>
	</div>
</template>
