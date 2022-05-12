import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import LoginScreen from "../components/LoginScreen.vue";
import ActivitiesView from "../components/ActivitiesView.vue";
import AccountView from "../components/AccountView.vue";

import NotFound from "../components/NotFound.vue";

import StudentsView from "../components/Teacher/StudentsView.vue";
import UserView from "../components/Teacher/UserView.vue";
import ActivityView from "../components/Teacher/ActivityView.vue";

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
		component: ActivitiesView,
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
	{
		path: "/user/:id",
		name: "user",
		component: UserView,
		meta: { title: "Account-Seite" },
	},
	{
		path: "/activities/:id",
		name: "activity",
		component: ActivityView,
		meta: { title: "Aktivität" },
	},

	{
		path: "/:pathMatch(.*)*",
		name: "not-found",
		component: NotFound,
		meta: { title: "404 - Nicht gefunden" },
	},
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

export default router;
