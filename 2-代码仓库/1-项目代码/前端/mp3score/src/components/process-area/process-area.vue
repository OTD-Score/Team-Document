<template>
    <div class='wrapper'>
        <div class="main-area">
            <!-- 列表头 -->
            <div class="progress-area">
                <div class="left-wrap">
                    <div class="progress-lab" :class="{ 'progress-lab-animation' : (uploadFlag=='1' || uploadFlag=='2') }">
                        <template v-if="uploadFlag=='1'">
                            <p class="progress-num">运算中</p>
                        </template>
                        <template v-else-if="uploadFlag=='2'">
                            <p class="progress-num">上传中</p>
                        </template>
                        <template v-else>
                            <img src="@/assets/progress-area/progress-icon.png" class="progress-icon">
                            <p class="progress-num">100%</p>
                        </template>
                    </div>
                    <div class="file-size">
                        <div>{{ uploadFlag == '1' || '2' ? '任务进行中（请耐心等待）' : '任务已完成' }}</div>
                        <div>{{ allSize + 'M' }}</div>
                    </div>
                </div>
                <!-- <div class="files-btn">
                    全部记录
                </div> -->
            </div>
            <!-- 列表框 -->
            <div class="result-list">
                <!-- 列表项 -->
                <div class="result-item" v-for="(file,index) in fileList" :v-key="index" >
                    <div class="result-left-wrap">
                        <img src="@/assets/progress-area/icon-midi.png" class="file-icon">
                        <div class="file-name">{{ file.name }}</div>
                    </div>

                    <div class="result-right-wrap">
                        <!-- <img src="@/assets/progress-area/preview-btn.png" class="btn preview-btn"/> -->
                        <img src="@/assets/progress-area/dowload-btn.png" :data-download-job_id="file.job_id" :data-download-name='file.name'
                         :data-download-type="file.type" @click="dowloadFile" class="btn dowload-btn"/>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import Req from '@/utils/request'
export default{
    name:'processArea',
    props : {
        fileData : Object ,
        uploadFlag : { //1-运算中 2-上传中 其他-完成了
            type : String,
            default : '1'
        } ,
    },
    data(){
        return {
            fileList : []
        }
    },
    computed : {
        allSize(){
            if(!this.fileList || this.fileList.length == 0){
                return ;
            }
            let sumSize = 0 ;
            for(let i=0;i<this.fileList.length;i++){
                sumSize += this.fileList[i].size
            }
            return sumSize;
        }
    },
    watch : {
        fileData(newData,oldData){
            if(!newData){
                return;
            }
            if(newData.job_id){
                //如果存在job_id,
                let index = newData.fileIndex ;
                this.fileList[index].job_id = newData.job_id ;
            }else{
                let type = newData.type
                let name = newData.name.split('.')[0].concat(`.${type}`) ;
                let size = parseFloat((newData.size/1024/1024).toFixed(2)) ;
                this.fileList.push({name,size,type})
            }
        }
    }, 
    methods : {
        dowloadFile(e){
            let job_id = e.target.dataset.downloadJob_id ;
            let name = e.target.dataset.downloadName.split('.')[0] ;
            let downloadType = e.target.dataset.downloadType ;

            let request_file_type = (downloadType == 'mxml' ? 'xml' : downloadType);  ; //接口后缀   transcrip的时候叫mxml , dowload的时候叫xml

            let download_file_type = this.suffixHandeler(downloadType); //文件后缀   请求的接口名是/midi ,但是文件后缀是.mid

            if(!job_id){
                window.alert('请等待完成后再下载')
                return;
            }
            return Req.fileDownLoad_Klangio(job_id,request_file_type,download_file_type,name)
        },
        suffixHandeler(filename){
            switch(filename) {
                case 'midi':
                    return 'mid' ;
                case 'mxml':
                    return 'xml'
                default:
                    return filename ;
            }
        }
    }

}
</script>

<style scoped>
    .wrapper{
        display: flex;
        justify-content: center;
    }
    .main-area{
        width: 1202px;
        min-height: 252px;
        box-shadow: 0px 10px 12px  rgba(0, 0, 0, 0.25);
        border-radius: 8px;
        position: relative;
        top:-16px;
        z-index: 100;
    }
    .progress-area{
        width: 100%;
        height: 120px;
        background: rgba(79, 66, 56, 1);
        border-radius: 8px 8px 0 0 ;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .progress-lab{
        display: flex;
        width: 207.14px;
        height: 83.13px;
        border-radius: 8px;
        background: rgba(101, 94, 78, 1);
        box-shadow:inset 0px -3px 2px  rgba(0, 0, 0, 0.25);
        align-items: center;
        margin-left: 30px;
        justify-content: center;
    }
    .progress-icon{
        width: 54px;
        height: 54px;
    }

    .progress-lab-animation{
        background: linear-gradient(rgb(12, 132, 223) 0 0) 0/0% no-repeat rgba(101, 94, 78, 1);
        animation: cartoon 2s infinite linear;
    }

    @keyframes cartoon {
        100% {
        background-size: 100%;
        }
    }
    .progress-num{
        font-size: 39px;
        margin-left: 13px;
        color: #ffffff;
    }
    .file-size{
        margin-left: 18px;
        font-size: 24px;
        color: #ffffff;
        line-height: 36px;
        text-align: center;
    }
    .left-wrap{
        display: flex;
        align-items: center;
    }
    .files-btn{
        width: 176.04px;
        height: 83.13px;
        border-radius: 8px;
        background: rgba(213, 181, 134, 1);
        box-shadow:inset 0px -3px 2px  rgba(0, 0, 0, 0.25);
        margin-right: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        color: #ffffff;
    }
    .result-list{
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 23px 0 38px;
        box-sizing: content-box;
    }
    .result-item{
        margin-bottom: 25px;
        width: 1127px;
        height: 104.64px;
        border-radius: 12px;
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 10px 20px  rgba(0, 0, 0, 0.25);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .result-left-wrap{
        display: flex;
        margin-left: 24px;
        align-items: center;
    }
    .file-icon{
        width: 54.77px;
        height: 54.77px;
    }
    .file-name{
        margin-left: 11px;
        font-size: 20px;
        color: rgba(74, 79, 56, 1);
        font-weight: 700;
    }
    .result-right-wrap{
        display: flex;
        align-items: center;
        margin-right: 47px;
    }
    .btn{
        display: block;
    }
    .preview-btn{
        width: 80px;
        height: 32px;
    }
    .dowload-btn{
        width: 75px;
        height: 32px;
        margin-left: 15px;
    }
</style>