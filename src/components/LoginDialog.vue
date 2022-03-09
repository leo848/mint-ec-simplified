<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "LoginDialog",

	data: () => ({ show: false }),

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
				<v-container>
					<v-row>
						<v-col cols="12">
							<v-text-field label="Benutzername" required></v-text-field
						></v-col>
						<v-col cols="12">
							<v-text-field
								label="Password"
								type="password"
								required
							></v-text-field>
						</v-col>
					</v-row>
				</v-container>
			</v-card-text>
			<v-card-actions>
				<v-spacer></v-spacer>
				<v-btn color="blue darken-1" text @click="show = false">
					Abbrechen
				</v-btn>
				<v-btn color="blue darken-1" text @click="show = false">
					Einloggen
				</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>
