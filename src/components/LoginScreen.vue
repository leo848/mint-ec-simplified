<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "LoginScreen",

  data: () => ({}),

  methods: {},
});
</script>

<template>
  <v-container fill-height fluid class="bg">
    <v-row align="center" justify="center">
      <v-col class="text-center" cols="12">
        <h1 class="mb-4">Willkommen bei mint-ec-simplified.</h1>
        <h2 class="subheading mb-6">Bitte logge dich ein, um fortzufahren.</h2>
        <v-row align="center" justify="center">
          <v-btn color="primary" elevation="2" x-large class="mr-4">
            Login
          </v-btn>
          <v-btn color="primary" elevation="2" x-large class="ml-4">
            Registrieren
          </v-btn>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<style>
.bg {
  background: url("../../public/img/login-background.jpg");
  background-size: cover;
  min-height: 99vh;
}
</style>
