import Vue from 'vue'
import VueRouter from 'vue-router'
import Table from '@/components/Table'

Vue.use(VueRouter)

const routes = [{
  path: '/',
  name: 'Table',
  component: Table
}]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router