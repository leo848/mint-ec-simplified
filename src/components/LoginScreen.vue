<script lang="ts">
import Vue from "vue";
import LoginDialog from "./LoginDialog.vue";
import RegisterDialog from "./RegisterDialog.vue";

export default Vue.extend({
	name: "LoginScreen",
	components: { LoginDialog, RegisterDialog },

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
          <LoginDialog />
          <RegisterDialog />
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
