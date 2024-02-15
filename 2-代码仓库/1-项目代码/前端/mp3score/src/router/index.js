import IndexPage from '@/views/index';
import RecordPage from '@/views/record'

import { createRouter,createWebHashHistory } from 'vue-router'

const routes = [
    { path: '/', component : IndexPage},
    { path: '/record',component : RecordPage}

]

const router = createRouter({
    history: createWebHashHistory(),
    routes ,
})

export default router ;