import List from '@/views/list/index';

import { createRouter,createWebHashHistory } from 'vue-router'

const routes = [
    { path: '/', component: List },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes ,
})

export default router ;