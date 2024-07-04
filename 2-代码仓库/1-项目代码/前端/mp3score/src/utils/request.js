const KlangIo_API = '0xkl-ad5e4946cfaf48c6969e0923977791cd';

import axios from 'axios'


// import BASE from '@/utils/api'


//baseUrl 根据不同环境引入不同api 自动从打包配置中读取
// const baseUrl =  'http://114.55.130.141:8080' ;

let baseUrl = "/";
if(process.env.NODE_ENV === 'production'){
    baseUrl = 'http://114.55.130.141:8080/';
}

const utils = {
    getReq_Klangio(url,job_id){
        return axios.get(`${baseUrl}klang/${url}?jobId=${job_id}`)
    },

    fileUpLoad_Klangio(model = 'piano',formData,outputs){ //前端请求在vue.config.js里配置了代理,/api开头的请求会转发到代理，解决跨域
        return axios.post(`${baseUrl}klang/transcription?model=${model}&output=${outputs}`, formData)
    },

    fileDownLoad_Klangio(job_id,dowload_type='midi',output_type='mid',file_name){
        axios.get(`${baseUrl}klang/download?jobId=${job_id}&fileType=${dowload_type}`,{
            responseType : 'blob',//默认是json，必须指定
        }).then(res=>{
            if(res.status == 200){
                // 导出流 
                const blob = new Blob([res.data], { type: output_type }); // 指定格式
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = `${file_name}.${output_type}`; // 指定导出名称
                link.click();
                URL.revokeObjectURL(link.href);
            }else{
                //下载失败
            }
        })
    },

    // 轮询函数，每隔一定时间执行一次，直至返回的promise成功解决
    pollApi(apiCall, condition, interval = 4000) {
        return new Promise((resolve, reject) => {
            const poll = () => {
            apiCall().then(response => {
                    // 检查条件是否满足
                if (condition(response.data.data)) {
                    resolve(response); // 条件满足，返回结果并停止轮询
                } else {
                    // 条件不满足，继续轮询
                    setTimeout(poll, interval);
                }
            }).catch(error => {
                // 如果API调用失败，则停止轮询
                reject(error);
            });
            };
            // 首次调用API开始轮询
            poll();
        });
    }
}

export default utils;