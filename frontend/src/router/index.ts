import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/DashboardView.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/LoginView.vue'),
  },
  {
    path: '/team',
    name: 'TeamMemberList',
    component: () => import('@/views/TeamMemberListView.vue'),
  },
  {
    path: '/team/:id',
    name: 'TeamMemberDetail',
    component: () => import('@/views/TeamMemberDetailView.vue'),
    props: true,
  },
  {
    path: '/goals',
    name: 'ObjectiveList',
    component: () => import('@/views/ObjectiveListView.vue'),
  },
  {
    path: '/meetings',
    name: 'MeetingLog',
    component: () => import('@/views/MeetingLogView.vue'),
  },
  {
    path: '/actions',
    name: 'ActionItemList',
    component: () => import('@/views/ActionItemListView.vue'),
  },
  {
    path: '/ai',
    name: 'AIInsights',
    component: () => import('@/views/AIInsightsView.vue'),
  },
  // fallback route
  {
    path: '/:pathMatch(.*)*',
    redirect: '/',
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
