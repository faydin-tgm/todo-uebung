import Vue from 'vue'
import Router from 'vue-router'
import TodoClient from '@/components/TodoClient'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'TodoClient',
      component: TodoClient
    }
  ]
})
