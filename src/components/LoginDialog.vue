<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "LoginDialog",

	data: () => ({
		show: false,
		valid: true,
		data: { username: null, password: null },
		rules: {
			username: [(v: string) => !!v || "Bitte gib einen Benutzernamen ein"],
			password: [(v: string) => !!v || "Bitte gib ein Passwort ein"],
		},
	}),

	methods: {},
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
			<v-card-title>
				<span class="text-h5">Einloggen</span>
			</v-card-title>
			<v-card-text>
				<v-form v-model="valid">
					<v-container>
						<v-row>
							<v-col cols="12">
								<v-text-field
									label="Benutzername"
									v-model="data.username"
									:rules="rules.username"
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
					text
					@click="show = false"
				>
					Einloggen
				</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>
