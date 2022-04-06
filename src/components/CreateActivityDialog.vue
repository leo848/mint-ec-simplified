<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	data: () => ({
		show: false,
		valid: true,
		activeDatePicker: "YEAR",
		data: { title: "", description: "", date: null, category: 0 },
		dateMenu: false,
		categoryList: [],
		tagList: [],
		rules: {
			title: [
				(v: string) => !!v || "Bitte gib einen Titel ein.",
				(v: string) => v.length >= 10 || "Bitte gib mehr als 10 Zeichen ein.",
				(v: string) =>
					v.length < 200 || "Bitte gib nicht mehr als 200 Zeichen ein.",
			],
			description: [
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
	async created() {
		await this.fetchRequiredData();
	},
	methods: {
		upload() {
			this.show = false;
		},
		async fetchRequiredData() {
			let categoryRequest = fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/categories",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			let tagRequest = fetch(process.env.VUE_APP_BACKEND_ROOT + "/tags", {
				headers: { Authorization: "Bearer " + localStorage.token },
			});
			let [categories, tags] = await Promise.all([categoryRequest, tagRequest]);
			[this.categoryList, this.tagList] = await Promise.all([
				categories.json(),
				tags.json(),
			]);
		},
	},
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
							<v-col cols="12" sm="6">
								<v-select
									label="Kategorie"
									:items="categoryList"
									v-model="data.category"
									item-text="title"
									item-value="id"
									:hint="`${data.category.description || 'Bitte auswählen'}`"
									persistent-hint
									return-object
									single-line
									@click="fetchRequiredData"
								/>
							</v-col>
							<v-col cols="12" sm="6">
								<v-menu
									ref="dateMenu"
									v-model="dateMenu"
									:close-on-content-click="false"
									offset-y
									min-width="auto"
								>
									<template v-slot:activator="{ on, attrs }">
										<v-text-field
											v-model="data.date"
											label="Datum"
											prepend-icon="mdi-calendar"
											readonly
											v-bind="attrs"
											v-on="on"
										></v-text-field>
									</template>
									<v-date-picker
										v-model="data.date"
										:active-picker.sync="activeDatePicker"
										no-title
										scrollable
										language="de"
										:max="
											new Date(
												Date.now() - new Date().getTimezoneOffset() * 60000,
											)
												.toISOString()
												.substr(0, 10)
										"
										min="1950-01-01"
									></v-date-picker>
								</v-menu>
							</v-col>
							<v-col cols="12" sm="6">
								<v-text-field
									label="Website (optional)"
									v-model="data.website"
									:rules="rules.website"
									prepend-icon="mdi-web"
									clearable
									clear-icon="mdi-close"
								/>
							</v-col>
							<v-col cols="12" sm="12">
								<v-textarea
									label="Beschreibung (optional)"
									v-model="data.description"
									:rules="rules.description"
									counter="2000"
									rows="3"
									auto-grow
									clearable
									clear-icon="mdi-close"
								></v-textarea>
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
				<v-btn color="blue darken-1" :disabled="!valid" text @click="upload"
					>Registrieren</v-btn
				>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>
