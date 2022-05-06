<script lang="ts">
import Vue from "vue";
import LoginDialog from "./LoginDialog.vue";
import RegisterDialog from "./RegisterDialog.vue";

export default Vue.extend({
	name: "LoginScreen",
	components: { LoginDialog, RegisterDialog },

	data: () => ({ error: false, errorMsg: "" }),

	created() {
		if (localStorage.token) this.login();
	},

	methods: {
		async login() {
			const response = await fetch(
				process.env.VUE_APP_BACKEND_ROOT + "/user/me/",
				{
					headers: { Authorization: "Bearer " + localStorage.token },
				},
			);
			if (!response.ok) {
				this.error = true;
				if (response.status === 401)
					this.errorMsg = "Bitte logge dich erneut ein.";
				else
					this.errorMsg =
						"Unbekannter Fehler. Bitte versuche es später erneut.";
				localStorage.removeItem("token");
				return;
			}
			sessionStorage.setItem("user", JSON.stringify(await response.json()));

			window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
		},
	},
});
</script>

<template>
	<v-container fill-height fluid class="bg">
		<v-row align="center" justify="center">
			<v-col class="text-center" cols="12">
				<v-row justify="center">
					<v-alert class="col-4" dense dismissible type="error" v-model="error">
						{{ errorMsg }}
					</v-alert>
				</v-row>
				<h1 class="mb-2 text-h2">Willkommen bei mint-ec-simplified.</h1>
				<h2 class="subheading mb-8">Bitte logge dich ein, um fortzufahren.</h2>
				<v-row align="center" justify="center">
					<LoginDialog @done="login" />
					<RegisterDialog @done="login" />
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
	min-width: 100vw;
}
</style>
