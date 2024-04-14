import { createApp } from 'vue'
import App from './App.vue'
import Router from '@/router/index'
// import axios from 'axios'

const app = createApp(App);

app
.use(Router)
// .use(axios)
.mount('#app')