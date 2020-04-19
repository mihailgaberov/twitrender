import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import VueCarousel from '@chenfengyuan/vue-carousel';
import App from './App.vue';
import router from './router';

Vue.use(BootstrapVue);
Vue.use(VueCarousel);
Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
