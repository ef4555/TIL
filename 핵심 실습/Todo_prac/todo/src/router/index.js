import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodo from '../views/AllTodoPage.vue'
import ImportantTodo from '../views/ImportantTodoPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'AllTodo',
    component: AllTodo
  },
  {
    path: '/today',
    name: 'today',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/TodayTodoPage.vue')
  },
  {
    path: '/important',
    name: 'important',
    component: ImportantTodo
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
