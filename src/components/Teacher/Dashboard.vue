<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "TeacherView",
	data: () => ({
		user: {},
		cards: [
			{
				title: "Schüler",
				description:
					"Eine Liste aller Schüler. Von hier aus kann auf die Profile der Schüler navigiert werden.",
				color: "red darken-3",
				link: "/students",
				icon: "mdi-format-list-bulleted-square",
			},
			{
				title: "Alle Aktivitäten",
				description:
					"Suche nach Aktivitäten und filtere nach Tags, Namen und Kategorien.",
				color: "green darken-3",
				link: "/activities",
				icon: "mdi-counter",
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
		<v-row>
			<v-col v-for="(card, i) in cards" :key="i" cols="12" sm="6">
				<v-card :color="card.color" :to="card.link" height="200px" hover>
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
