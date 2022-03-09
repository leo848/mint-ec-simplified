<script lang="ts">
import Vue from "vue";

export default Vue.extend({
	name: "RegisterDialog",

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
        Registrieren
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">Registrieren</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field label="Vorname*" required></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field label="Nachname*" required></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                label="Schul-Email-Adresse"
                hint="Im Format max.mustermann@gymnasium-essen-werden.de"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                label="Passwort*"
                type="password"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-select
                :items="['5', '6', '7', '8', '9', 'EF', 'Q1', 'Q2']"
                label="Stufe*"
                required
              ></v-select>
            </v-col>
            <v-col cols="12" sm="6">
              <v-autocomplete
                :items="[
                  'Skiing',
                  'Ice hockey',
                  'Soccer',
                  'Basketball',
                  'Hockey',
                  'Reading',
                  'Writing',
                  'Coding',
                  'Basejump',
                ]"
                label="Interests"
                multiple
              ></v-autocomplete>
            </v-col>
          </v-row>
        </v-container>
        <small>*indicates required field</small>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="show = false"> Close </v-btn>
        <v-btn color="blue darken-1" text @click="show = false"> Save </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
