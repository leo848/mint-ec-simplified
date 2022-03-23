<script lang="ts">
import Vue from "vue";
import LoginDialog from "./LoginDialog.vue";
import RegisterDialog from "./RegisterDialog.vue";

export default Vue.extend({
	name: "LoginScreen",
	components: { LoginDialog, RegisterDialog },

	data: () => ({
		loggedIn: false,
	}),

	methods: {
		async done() {
			const response = await fetch(process.env.VUE_APP_BACKEND_ROOT + "/me/", {
				headers: { Authorization: "Bearer " + localStorage.token },
			});
			sessionStorage.setItem("user", JSON.stringify(await response.json()));

			this.$emit("done");
		},
	},
});
</script>

<template>
	<v-container fill-height fluid class="bg">
		<v-row align="center" justify="center">
			<v-col class="text-center" cols="12">
				<h1 class="mb-2 text-h2">Willkommen bei mint-ec-simplified.</h1>
				<h2 class="subheading mb-8">Bitte logge dich ein, um fortzufahren.</h2>
				<v-row align="center" justify="center">
					<LoginDialog @done="done" />
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
	min-width: 100vw;
}
</style>
