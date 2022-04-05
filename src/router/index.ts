import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import LoginScreen from "../components/LoginScreen.vue";
import ActivityView from "../components/ActivityView.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
	{
		path: "/",
		name: "dashboard",
		component: Dashboard,
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
	},
	{ path: "/activities", name: "activities", component: ActivityView },
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

export default router;
