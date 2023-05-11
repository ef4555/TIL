import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import DogView from '@/views/DogView'

Vue.use(VueRouter)
const isLoggedIn = true

const routes = [
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 함')
        next({name : 'home'})
      } else {
        next() // 원래 가야할 곳으로 보내준다 : 로그인 페이지로 이동
      }
    }
  },
  {
    path:'/dog/:breed',
    name: 'dog',
    component: DogView,
  },
  {
    path: '*', // 위에 해당하지 않는 모든 것....
    redirect: '/404', 
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router/index.js
// router.beforeEach((to, from, next) => { //beforeEach : 모든 페이지에서 실행됨
//   // 로그인 여부를 판단
//   const isLoggedIn = false // 로그인이 안 된 상태
//   // const isLoggedIn = true // 로그인 된 상태
//   // 로그인이 필요한 페이지 지정
//   // const authPages = ['hello', 'about', 'home']
//   const allowAuthPages = ['login'] // 로그인을 안해도 되는 페이지만 설정
//   // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
//   const isAuthRequired = !allowAuthPages.includes(to.name)

//   // 로그인이 필요한 페이지인데 로그인이 안되어 있다면 
//   if (isAuthRequired && !isLoggedIn) {
//     console.log('login으로 이동')
//     alert('로그인 해주세요')
//     next({name: 'login'}) // next는 한번만 실행되도록
//   } else {
//     console.log('to로 이동!')
//     next()
//   }
// })

export default router
