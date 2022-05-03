<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "AccountView",
	data: function () {
		return {
			loading: false,
			valid: true,
			data: {} as { [key: string]: any },
			user: {} as { [key: string]: any },
		};
	},
	async created() {
		this.user = JSON.parse(sessionStorage.getItem("user") as string);
		this.loading = true;
		await this.fetchUser();
		this.loading = false;
	},
	methods: {
		logout() {
			localStorage.removeItem("token");
			this.$router.replace("/login");
		},
		async fetchUser() {
			let response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/user/me",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			this.user = await response.json();
			this.data = { ...this.data, ...this.user };
			console.log(this.data);
		},
	},
	computed: {
		userModified(): boolean {
			for (const key in this.user) {
				if (this.data[key] != this.user[key]) return true;
			}
			return false;
		},
	},
});
</script>

<template>
	<div class="wrapper">
		<h1 class="text-h3 mt-4 mb-4">Dein Account</h1>
		<v-btn color="primary" x-large @click="logout"> Ausloggen </v-btn>
		<v-card :loading="loading" max-width="700px" class="mt-4">
			<v-card-title>
				<span class="text-h5">Account-Informationen bearbeiten</span>
			</v-card-title>
			<v-card-text>
				<v-form v-model="valid">
					<v-container>
						<v-row>
							<v-col cols="12">
								<v-text-field label="Anzeigename" v-model="data.display_name" />
							</v-col>
							<v-col cols="6">
								<v-text-field
									label="Vorname"
									v-model="data.first_name"
									disabled
								/>
							</v-col>
							<v-col cols="6">
								<v-text-field
									label="Nachname"
									v-model="data.last_name"
									disabled
								/>
							</v-col>
							<v-col cols="12">
								<v-text-field
									label="E-Mail-Adresse"
									v-model="data.email"
									disabled
								/>
							</v-col>
						</v-row>
					</v-container>
				</v-form>
			</v-card-text>
			<v-card-actions>
				<v-spacer />
				<v-btn
					color="blue darken-1"
					:disabled="!valid || !userModified"
					text
					@click="show = false"
					>Speichern</v-btn
				>
			</v-card-actions>
		</v-card>
	</div>
</template>
