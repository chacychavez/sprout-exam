import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import DashboardView from '@/views/DashboardView.vue';

import EmployeeView from '@/views/EmployeeView.vue';
import EditEmployeeView from '@/views/EditEmployeeView.vue';

const routes = [
  {
    path: '/',
    name: "Home",
    component: HomeView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardView,
    meta: { requiresAuth: true },
  },
  {
    path: '/employee/:type/:id',
    name: 'Employee',
    component: EmployeeView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/edit-employee/:type/:id',
    name: 'EditEmployee',
    component: EditEmployeeView,
    meta: { requiresAuth: true },
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router