<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	data: () => ({
		show: false,
		valid: true,
		data: { title: "", description: "" },
		rules: {
			title: [
				(v: string) => !!v || "Bitte gib einen Titel ein.",
				(v: string) => v.length >= 10 || "Bitte gib mehr als 10 Zeichen ein.",
				(v: string) =>
					v.length < 200 || "Bitte gib nicht mehr als 200 Zeichen ein.",
			],
			description: [
				(v: string) =>
					!v || v.length >= 10 || "Bitte gib mehr als 10 Zeichen ein.",
				(v: string) =>
					!v ||
					v.length <= 2000 ||
					"Bitte gib nicht mehr als 2000 Zeichen ein.",
			],
			website: [
				(v: string) =>
					!v ||
					/^(?:https?:\/\/)?(?:www.)?(?:[^#/]+?\.)+?[a-zA-Z]{2,5}(?:\/[^#/]+?)?\/?$/.test(
						v,
					) ||
					"Keine gültige Website-URL",
			],
		},
	}),
});
</script>

<template>
	<v-dialog v-model="show" persistent max-width="900px">
		<template v-slot:activator="{ on, attrs }">
			<v-btn
				v-bind="attrs"
				v-on="on"
				color="primary"
				elevation="2"
				class="mr-4"
				fab
				fixed
				bottom
				right
			>
				<v-icon>mdi-plus</v-icon>
			</v-btn>
		</template>
		<v-card>
			<v-card-title>
				<span class="text-h5">Neue Aktivität hinzufügen</span>
			</v-card-title>
			<v-card-text>
				<v-form v-model="valid">
					<v-container>
						<v-row>
							<v-col cols="12" sm="12">
								<v-text-field
									label="Titel"
									v-model="data.title"
									:rules="rules.title"
									counter="200"
									clearable
									clear-icon="mdi-close"
									required
								/>
							</v-col>
							<v-col cols="12" sm="12">
								<v-textarea
									label="Beschreibung"
									v-model="data.description"
									:rules="rules.description"
									counter="2000"
									clearable
									clear-icon="mdi-close"
								></v-textarea>
							</v-col>
							<v-col cols="12" sm="6">
								<v-text-field
									label="Website"
									v-model="data.website"
									:rules="rules.website"
									clearable
									clear-icon="mdi-close"
								></v-text-field>
							</v-col>
						</v-row>
					</v-container>
				</v-form>
			</v-card-text>
			<v-card-actions>
				<v-spacer />
				<v-btn color="blue darken-1" text @click="show = false"
					>Abbrechen</v-btn
				>
				<v-btn
					color="blue darken-1"
					:disabled="!valid"
					text
					@click="show = false"
					>Registrieren</v-btn
				>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>
