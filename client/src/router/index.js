import Vue from 'vue';
import VueRouter from 'vue-router';
import Twitrender from '../components/Twitrender.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Twitrender',
    component: Twitrender,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
