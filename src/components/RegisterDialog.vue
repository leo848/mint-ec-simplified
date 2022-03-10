<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "RegisterDialog",

	data: () => ({
		show: false,
		data: {
			firstName: null,
			lastName: null,
			displayName: null,
			email: null,
			password: null,
			passwordRepeat: null,
			grade: null,
			classChar: null,
		},
		rules: {
			email: [
				(v: string) => !!v || "Bitte gib eine E-Mail-Adresse ein.",
				(v: string) => /.+@.+/.test(v) || "Keine gültige E-Mail-Adresse.",
				(v: string) =>
					/.{2,50}\..{2,50}@gymnasium-essen-werden.de/.test(v) ||
					"Keine gültige GEW-E-Mail-Adresse.",
			],
			name: [
				(v: string) => !!v || "Bitte gib einen Namen ein.",
				(v: string) =>
					v.length <= 100 ||
					"Dieser Name ist zu lang. Falls dies wirklich dein Name ist, kontaktiere den Systemadministrator.",
			],
			displayName: [
				(v: string) =>
					v.length <= 32 ||
					"Bitte wähle einen Display-Namen mit 32 oder weniger Buchstaben.",
			],
			password: [
				(v: string) => !!v || "Bitte gib ein Passwort ein.",
				(v: string) => v.length >= 8 || "Bitte mehr als 8 Zeichen benutzen.",
			],
		},
		valid: true,
	}),

	methods: {
		passwordRepeat(v: string) {
			return v === this.data.password || "Passwörter stimmen nicht überein.";
		},
	},
});
</script>

<template>
	<v-dialog v-model="show" persistent max-width="600px">
		<template v-slot:activator="{ on, attrs }">
			<v-btn
				v-bind="attrs"
				v-on="on"
				color="primary"
				elevation="2"
				x-large
				class="mr-4"
			>
				Registrieren
			</v-btn>
		</template>
		<v-card>
			<v-card-title>
				<span class="text-h5">Registrieren</span>
			</v-card-title>
			<v-card-text>
				<v-form v-model="valid">
					<v-container>
						<v-row>
							<v-col cols="12" sm="6">
								<v-text-field
									label="Vorname*"
									v-model="data.firstName"
									:rules="rules.name"
									required
								/>
							</v-col>
							<v-col cols="12" sm="6">
								<v-text-field
									label="Nachname*"
									v-model="data.lastName"
									:rules="rules.name"
									required
								/>
							</v-col>
							<v-col cols="12">
								<v-text-field
									label="Anzeigename"
									v-model="data.displayName"
									hint="Name, der im UI verwendet wird."
									:rules="rules.displayName"
									:placeholder="data.firstName"
								/>
							</v-col>
							<v-col cols="12">
								<v-text-field
									label="Schul-Email-Adresse*"
									v-model="data.email"
									hint="Im Format vorname.nachname@gymnasium-essen-werden.de"
									:placeholder="
										data.firstName && data.lastName
											? `${data.firstName.toLowerCase()}.${data.lastName.toLowerCase()}@gymnasium-essen-werden.de`
											: null
									"
									:rules="rules.email"
									required
								/>
							</v-col>
							<v-col cols="12" sm="6">
								<v-text-field
									label="Passwort*"
									v-model="data.password"
									type="password"
									:rules="rules.password"
									required
								/>
							</v-col>
							<v-col cols="12" sm="6">
								<v-text-field
									label="Passwort wiederholen*"
									:v-model="[passwordRepeat]"
									type="password"
									required
								/>
							</v-col>
							<v-col
								cols="12"
								:sm="data.grade && data.grade.length == 1 ? 6 : false"
							>
								<v-select
									:items="['5', '6', '7', '8', '9', 'EF', 'Q1', 'Q2']"
									v-model="data.grade"
									label="Stufe*"
									required
								/>
							</v-col>
							<v-col
								cols="12"
								sm="6"
								v-if="data.grade && data.grade.length === 1"
							>
								<v-select
									:items="['A', 'B', 'C', 'D', 'E', 'F']"
									v-model="data.classChar"
									label="Klasse*"
									required
								/>
							</v-col>
						</v-row>
					</v-container>

					<small>*erforderliches Feld</small>
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
