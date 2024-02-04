import axios from 'axios'
// import BASE from '@/utils/api'


//baseUrl 根据不同环境引入不同api 自动从打包配置中读取
const baseUrl =  'https://yingji.irootech.com/' ;

const BASE = {
    login : 'eemd/login',
}




const service = axios.create({
    baseURL : [baseUrl],
    // withCredentials: true, // send cookies when cross-domain requests
    timeout: 10000 // request timeout
})

//request interceptor
service.interceptors.request.use(
    config => {
        //处理请求前url拼接token 或其他鉴权
        return config
    }
)

service.interceptors.response.use(
    response => {
        //对服务器相应数据先处理一遍
        return response;
    }
  )

const utils = {
    postReq(url,data){
        return service.post(baseUrl + BASE[url],data)
    },

    getReq(){

    },

    fileUpLoad(){

    },

    fileDownLoad(){

    }
}


export default utils;