import IndexPage from '@/views/index/IndexPage';
// import IndexPage from '@/views/index';
import RecordPage from '@/views/record';
// import LoginPage from '@/views/login/login.vue'
import LoginPage from '@/views/login/login'

import { createRouter,createWebHashHistory } from 'vue-router'

const routes = [
    { path: '/login', component: LoginPage },
    { path: '/', component : IndexPage},
    { path: '/record',component : RecordPage}

]

const router = createRouter({
    history: createWebHashHistory(),
    routes ,
})

// 路由守卫
// router.beforeEach((to,from,next)=>{
//     const isLogin=localStorage.MP3SCORE_login?true:false;
//     if(to.path=='/login'){
//         next();
//     }else{
//         //是否在登录状态下
//         isLogin?next():next('/login');
//     }
// }
// );

// 路由守卫
// router.beforeEach((to, from, next) => {
//     const token = localStorage.getItem('token'); // 从本地缓存获取token
//     const tokenExpiration = localStorage.getItem('tokenExpiration'); // 获取token过期时间

//     if (to.path === '/') {
//         // 如果用户访问首页，则直接跳转
//         next();
//     } else {
//         // 检查token是否存在且未过期
//         if (token && tokenExpiration && new Date(tokenExpiration) > new Date()) {
//             next(); // 已登录且token未过期，允许访问
//         } else {
//             // token过期或不存在
//             if (to.path === '/login') {
//                 next(); // 如果是访问登录页面，则直接跳转
//             } else {
//                 // 提示登录已过期
//                 alert('登录已过期');
//                 setTimeout(() => {
//                     next('/login'); // 跳转到登录页面
//                 }, 1000);
//             }
//         }
//     }
// });

export default router ;