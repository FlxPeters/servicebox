import Vue from "vue";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import VueRouter from "vue-router";

import App from "./App.vue";
import Home from "./components/pages/Home.vue";
import ServiceList from "./components/pages/services/ServiceList.vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "typeface-ubuntu";
import "./assets/scss/main.scss";

Vue.config.productionTip = false;

// Install BootstrapVue
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

// Router
Vue.use(VueRouter);

const routes = [
  { path: "/", component: Home },
  { path: "/services", component: ServiceList },
];
const router = new VueRouter({
  routes, // short for `routes: routes`
});

new Vue({
  render: (h) => h(App),
  router,
}).$mount("#app");
