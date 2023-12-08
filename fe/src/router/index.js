import { createRouter, createWebHistory } from 'vue-router'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import FeedView from '../views/FeedView.vue'
import MessagesView from '../views/MessagesView.vue'
import SearchView from '../views/SearchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/feed',
      name: 'feed',
      component: FeedView
    },
    {
      path: '/messages',
      name: 'messages',
      component: MessagesView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    }
  ]
})

export default router
