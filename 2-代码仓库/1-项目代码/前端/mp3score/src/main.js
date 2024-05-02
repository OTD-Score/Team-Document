import { createApp } from 'vue'
import App from './App.vue'
import Router from '@/router/index'
// import axios from 'axios';
/*引入自动适应不同分辨率配置*/
import '@/utils/rem'


const app = createApp(App);

app
.use(Router)
// .use(axios)
.mount('#app')
