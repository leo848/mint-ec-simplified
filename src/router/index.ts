import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import LoginScreen from "../components/LoginScreen.vue";
import ActivityView from "../components/ActivityView.vue";
import AccountView from "../components/AccountView.vue";

import StudentsView from "../components/Teacher/StudentsView.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
	{
		path: "/",
		name: "dashboard",
		component: Dashboard,
		meta: { title: "Dashboard" },
	},
	{
		path: "/login",
		name: "login",
		component: LoginScreen,
		meta: { title: "Einloggen" },
	},
	{
		path: "/activities",
		name: "activities",
		component: ActivityView,
		meta: { title: "Aktivitäten" },
	},
	{
		path: "/account",
		name: "account",
		component: AccountView,
		meta: { title: "Account" },
	},
	{
		path: "/students",
		name: "students",
		component: StudentsView,
		meta: { title: "Alle Schüler" },
	},
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

export default router;
