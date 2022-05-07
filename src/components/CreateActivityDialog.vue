<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	data: () => ({
		show: false,
		loading: false,
		error: false,
		errorMsg: "",
		valid: true,
		activeDatePicker: "YEAR",
		data: {
			title: "",
			description: "",
			date: null,
			category: null,
			website: "",
			tags: [],
		},
		dateMenu: false,
		categoryList: [],
		tagList: [],
		websitePreview: null as null | { [key: string]: string | boolean },
		cardError: false,
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
		async upload() {
			this.error = false;
			this.loading = true;

			this.data.tags = this.data.tags.map((t) => (t["title"] ? t["title"] : t));
			if (this.data.category == null) return;
			const data = {
				title: this.data.title,
				description: this.data.description,
				date: this.data.date,
				website: this.data.website,
				category_id: this.data.category["id"],
				tags: this.data.tags,
			};
			console.log(JSON.stringify(data));
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/student/activities/",
				{
					method: "POST",
					headers: {
						"content-type": "application/json",
						"Authorization": "Bearer " + localStorage.token,
					},
					body: JSON.stringify(data),
				},
			);
			this.loading = false;
			if (!response.ok) {
				this.error = true;
				if (response.status === 500) {
					this.errorMsg =
						"Ein Serverfehler ist aufgetreten, bitte versuche es später erneut.";
				} else
					this.errorMsg =
						"Ein unbekannter Fehler ist aufgetreten. Überprüfe die Konsole für Details.";
				return;
			}
			this.show = false;
			this.$emit("done");
		},
		async fetchRequiredData() {
			let categoryRequest = fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/categories/",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			let tagRequest = fetch(process.env.VUE_APP_BACKEND_ROOT + "/tags/", {
				headers: { Authorization: "Bearer " + localStorage.token },
			});
			let [categories, tags] = await Promise.all([categoryRequest, tagRequest]);
			[this.categoryList, this.tagList] = await Promise.all([
				categories.json(),
				tags.json(),
			]);
		},
		async getLinkPreview() {
			this.cardError = false;
			// requires linkpreview API key
			if (!this.data.website || !process.env.VUE_APP_LINK_PREVIEW_API_KEY) {
				this.websitePreview = null;
				return;
			}
			this.websitePreview = { loading: true };
			if (!/^https?:\/\//.test(this.data.website))
				this.data.website = "https://" + this.data.website;
			const request = await fetch("https://api.linkpreview.net/", {
				method: "POST",
				body: `key=${process.env.VUE_APP_LINK_PREVIEW_API_KEY}&q=${this.data.website}`,
			});
			if (!request.ok) {
				this.cardError = true;
				return;
			}
			this.websitePreview = (await request.json()) as { [key: string]: string };
		},
		truncateString(str: string, len: number) {
			return str.length <= len ? str : str.slice(0, len - 3) + "...";
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
			<v-alert v-if="error" dismissible type="error">{{ errorMsg }}</v-alert>
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
									:hint="`${
										(data.category || {}).description || 'Bitte auswählen'
									}`"
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
							<v-col cols="12" sm="5">
								<v-text-field
									label="Website (optional)"
									v-model="data.website"
									:rules="rules.website"
									prepend-icon="mdi-web"
									clearable
									clear-icon="mdi-close"
									@blur="getLinkPreview()"
								/>
							</v-col>
							<v-col cols="12" sm="7" v-if="websitePreview">
								<v-card
									dense
									:loading="websitePreview.loading"
									:color="cardError ? 'red' : 'gray'"
								>
									<v-list-item three-line>
										<v-list-item-content>
											<div class="text-overline mb-2">VORSCHAU</div>
											<v-list-item-title class="text-h5 mb-1">
												{{
													cardError
														? "Fehler beim Laden der Vorschau"
														: websitePreview.title
												}}
											</v-list-item-title>
											<v-list-item-subtitle>{{
												websitePreview.description
											}}</v-list-item-subtitle>
										</v-list-item-content>

										<v-list-item-avatar tile size="100">
											<v-img :src="websitePreview.image"
										/></v-list-item-avatar>
									</v-list-item>
								</v-card>
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
							<v-col cols="12">
								<v-combobox
									v-model="data.tags"
									:items="tagList"
									item-text="title"
									item-value="id"
									label="Tags"
									@click="fetchRequiredData"
									chips
									multiple
								/>
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
					>Fertig</v-btn
				>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>
