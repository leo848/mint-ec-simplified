import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import LoginScreen from "../components/LoginScreen.vue";
import ActivityView from "../components/ActivityView.vue";
import AccountView from "../components/AccountView.vue";

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
		// route level code-splitting
		// this generates a separate chunk (about.[hash].js) for this route
		// which is lazy-loaded when the route is visited.
		// (not yet, maybe later)
		/* component: () => */
		/* 	import(/1* webpackChunkName: "about" *1/ "../views/AboutView.vue"), */
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
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

export default router;
