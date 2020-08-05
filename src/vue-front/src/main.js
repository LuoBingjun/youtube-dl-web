import Vue from 'vue'
import App from './App.vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

import VueRouter from 'vue-router'
Vue.use(VueRouter)

import Home from './components/Home'

import axios from 'axios';
Vue.prototype.$axios = axios;

const routes = [
  { path: '/', name: 'Home', component: Home }
]
const router = new VueRouter({
  routes: routes,
  base: process.env.BASE_URL,
  mode: 'history'
})

Vue.config.productionTip = false

//实例化Vue实例
new Vue({
  render: h => h(App),
  router
}).$mount('#app')