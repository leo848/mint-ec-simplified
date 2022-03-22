<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "LoginDialog",

	data: () => ({
		show: false,
		error: false,
		loading: false,
		valid: true,
		data: { email: null as null | string, password: null as null | string },
		rules: {
			email: [
				(v: string | null) => v != null || "",
				(v: string) => !!v || "Bitte gib eine E-Mail-Adresse ein.",
				(v: string) => /.+@.+/.test(v) || "Keine gültige E-Mail-Adresse.",
				(v: string) =>
					/.{2,50}\..{2,50}@gymnasium-essen-werden.de/.test(v) ||
					"Keine gültige GEW-E-Mail-Adresse.",
			],
			password: [(v: string) => !!v || "Bitte gib ein Passwort ein"],
		},
	}),

	methods: {
		async login() {
			this.loading = true;
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/login/",
				{
					method: "POST",
					headers: { "content-type": "application/x-www-form-urlencoded" },
					body: new URLSearchParams({
						username: this.data.email as string,
						password: this.data.password as string,
					}).toString(),
				},
			);
			this.loading = false;
			if (!response.ok) {
				this.error = true;
				return;
			}
			localStorage.setItem("token", (await response.json()).access_token);
			this.show = false;
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
				Login
			</v-btn>
		</template>
		<v-card>
			<v-alert v-if="error" dismissible type="error"
				>Falsches Passwort.</v-alert
			>
			<v-card-title>
				<span class="text-h5">Einloggen</span>
			</v-card-title>
			<v-card-text>
				<v-form v-model="valid">
					<v-container>
						<v-row>
							<v-col cols="12">
								<v-text-field
									label="E-Mail-Adresse"
									v-model="data.email"
									:rules="rules.email"
									required
								></v-text-field>
							</v-col>
							<v-col cols="12">
								<v-text-field
									label="Passwort"
									v-model="data.password"
									:rules="rules.password"
									type="password"
									required
								/>
							</v-col>
						</v-row>
					</v-container>
				</v-form>
			</v-card-text>
			<v-card-actions>
				<v-spacer></v-spacer>
				<v-btn color="blue darken-1" text @click="show = false">
					Abbrechen
				</v-btn>
				<v-btn
					color="blue darken-1"
					:disabled="!valid"
					:loading="loading"
					text
					@click="login()"
				>
					Einloggen
				</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>
