import { createRouter, createWebHistory } from 'vue-router';

import Home from '@/components/Home.vue';
import Model from '@/components/Model.vue';
import About from '@/components/About.vue';
import Evaluation from '@/components/Evaluation.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/model',
    name: 'model',
    component: Model,
  },
  {
    path: '/about',
    name: 'about',
    component: About,
  },
  {
    path: '/evaluation',
    name: 'evaluation',
    component: Evaluation,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;