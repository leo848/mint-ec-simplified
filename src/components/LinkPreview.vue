<script lang="ts">
import Vue from "vue";
export default Vue.extend({
	name: "LinkPreview",
	data: () => ({
		cardError: false,
		websitePreview: null as null | { [key: string]: string | boolean },
	}),
	props: {
		url: String,
		noPreview: {
			type: Boolean,
			default: false,
		},
	},
	async created() {
		await this.fetchPreview();
	},
	watch: {
		async url() {
			await this.fetchPreview();
		},
	},
	methods: {
		async fetchPreview() {
			this.cardError = false;
			// requires linkpreview API key
			if (!this.url || !process.env.VUE_APP_LINK_PREVIEW_API_KEY) {
				this.websitePreview = null;
				return;
			}
			this.websitePreview = { loading: true };
			const request = await fetch("https://api.linkpreview.net/", {
				method: "POST",
				body: `key=${process.env.VUE_APP_LINK_PREVIEW_API_KEY}&q=${this.url}`,
			});
			if (!request.ok) {
				this.cardError = true;
				return;
			}
			this.websitePreview = (await request.json()) as { [key: string]: string };
		},
	},
});
</script>

<template>
	<v-card
		dense
		v-if="websitePreview"
		:loading="websitePreview.loading"
		:color="cardError ? 'red' : 'gray'"
		:href="websitePreview.url"
		target="_blank"
	>
		<v-list-item three-line>
			<v-list-item-content>
				<div class="text-overline mb-2" v-if="!noPreview">VORSCHAU</div>
				<v-list-item-title class="text-h5 mb-1">
					{{
						cardError ? "Fehler beim Laden der Vorschau" : websitePreview.title
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
</template>
