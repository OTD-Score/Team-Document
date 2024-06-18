<template>
    <div class="main-wrapper">
        <!-- 白云之类的悬浮 -->
        <img src="@/assets/index/cloud-1.png" class="cloud-1"/>
        <img src="@/assets/index/cloud-2.png" class="cloud-2"/>
        <img src="@/assets/index/yuan-1.png" class="yuan-1"/>
        <img src="@/assets/index/yuan-2.png" class="yuan-2"/>
        <img src="@/assets/index/intro-title.png" class="intro-title"/>
        <!-- 拖文件的功能区 -->
        <div class="func-area">
            <div class="section">
                <div class="section-item" :class="{'section-item-active' : chooseIndex == '1' }" data-index="1" @click="chooseFuc">音频转MIDI</div>
                <div class="section-item" :class="{'section-item-active' : chooseIndex == '2' }" data-index="2" @click="chooseFuc">音频转PDF</div>
                <div class="section-item" :class="{'section-item-active' : chooseIndex == '3' }" data-index="3" @click="chooseFuc">音频分离</div>
                <div class="section-item" :class="{'section-item-active' : chooseIndex == '4' }" data-index="4" @click="chooseFuc">AI音乐生成</div>
            </div>
            <!-- 音频转MIDI拖区 -->
            <div class="audio2midi" v-if="chooseIndex == '1' || chooseIndex == '2'">
              <div class="file-drag">
                  <img src="@/assets/index/music-icon.png" class="music-icon"/>
                  <img src="@/assets/index/music-hint.png" class="music-hint"/>
                  <input class="file-input" type="file" accept="audio/mpeg, audio/wav" @change="fileUpload">
              </div>
              <div class="options" style="position:relative;left: -8px;">
                <div class="options-a">
                    <input type="radio" id="piano" value="1" v-model="modelChoose" >
                    <label for="option1">纯钢琴</label>
                </div>
                <div style="margin-left: 15px;">
                    <input type="radio" id="guitar" value="2" v-model="modelChoose">
                    <label for="option2">纯吉他</label>
                </div>
                <div>
                    <input type="radio" id="bass" value="3" v-model="modelChoose">
                    <label for="option1">纯贝斯</label>
                </div>
                <div style="margin-left: 15px;">
                    <input type="radio" id="vocal" value="4" v-model="modelChoose">
                    <label for="option2">纯人声</label>
                </div>
                <!-- <input type="button" @click="startQuery"> -->
              </div>
              <div style="margin-left: 6px;margin-top: 6px;">建议上传纯钢琴曲，效果更佳</div>

            </div>
            <!-- 其他功能区 -->
            <div class="othes-func" v-else>
              <div class="file-drag">
                  <img src="@/assets/index/music-icon.png" class="music-icon"/>
                  <img src="@/assets/index/other-hint.png" class="music-hint others-hint"/>
              </div>
            </div>
            
        </div>
    </div>
</template>

<script>
let fileIndex = 0;
import Req from '@/utils/request'

export default{
    name:'func-area',
    data(){
      return {
        chooseIndex : '1', //1音频转midi 2音频转pdf 
        modelChoose : '1',//1纯钢琴 2纯吉他 3纯贝斯 4纯人声
        fileList : [],
        fileUpLoading : false ,
        job_id : '',//当前任务ID
      }
    },
    computed : {
      outputs(){ //返回文件类型后缀
        switch (this.chooseIndex) {
          case '1':
            return 'midi'
          case '2':
            return 'pdf'
        }
        return 'midi'
      },
      modelinputs(){
        switch (this.modelChoose) {
          case '1':
            return 'piano'
          case '2':
            return 'guitar'
          case '3':
            return 'bass'
          case '4':
            return 'vocal'
        }
        return 'piano'
      }
    },  
    methods : {
      chooseFuc(e){
        let chooseIndex = e.target.dataset.index || '1' ;
        this.chooseIndex = chooseIndex ;
      },
      fileUpload(e){
        let _this = this ;
        const originalFile = e.target.files[0] || null;
        if(!originalFile){
          return ;
        }
        if(this.fileUpLoading){
          window.alert('请等待当前任务处理完成后再提交')
          return ;
        }
        this.fileUpLoading = true ;

        //发送，'开始上传'的信号  开始上传是2  计算中是1 其他是完成
        this.emitThings('startStopUpload','2');

        this.$nextTick(()=>{
          //把文件数据传出去给进度条那边展示
          let fileData = {
            name : originalFile.name,
            size : originalFile.size,
            fileIndex : fileIndex,
            type : _this.outputs
          }
          this.emitThings('uploadFileData',fileData);

          //创建formData
          const formData = new FormData();
          formData.append('file', originalFile);
          formData.append('outputs',this.outputs);
          
          //网络进度
          Req.fileUpLoad_Klangio(this.modelinputs,formData)
          .then(response => {
            // 处理响应数据
            if(response.status == 200){
              let job_id = response.data.job_id ;
              this.startQuery(job_id);
            }else{
              throw new Error();
            }
          })
          .catch(error => {
            // 处理错误情况
            console.error(error);
            _this.emitThings('startStopUpload','3');
          }).finally(()=>{
            //发送，'停止传输'的信号
            _this.emitThings('startStopUpload','1');
            _this.fileUpLoading = false ;
          });
        })
      },
      startQuery(job_id){
        let _this = this ;
        const getStatus = () => {return Req.getReq_Klangio('status',job_id)};
        const condition =  data => data.status === 'COMPLETED' ;
        
        Req.pollApi(getStatus,condition).then(()=>{
          //轮询，只到COMPLETED才开始下一步
          // 将job_id发到外面组件
          let file_data = {
            fileIndex : fileIndex++,
            job_id : job_id
          }
          _this.emitThings('uploadFileData',file_data);
        }).finally(()=>{
          //发送，'停止传输'的信号
          _this.emitThings('startStopUpload','done');
          _this.fileUpLoading = false ;
        });
      },
      emitThings(key,data){
        this.$emit(key,data);
      }
    }
}
</script>

<style scoped>
.main-wrapper{
    width:100%;
    height:702px;
    background-image:url('@/assets/index/main-bg.png');
    background-size:100% 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
  }
  .cloud-1{
    position: absolute;
    width: 550px;
    height: 550px;
    right: 156px;
    top: -22%;
  }
  .cloud-2{
    position: absolute;
    width: 832px;
    height: 832px;
    left: 0;
    top: -50%;  
  }
  .yuan-1{
    width: 101px;
    height: 101px;
    position: absolute;
    left: 1040px;
    bottom: -30px;
  }
  .yuan-2{
    width: 70px;
    height: 70px;
    position: absolute;
    left: 290px;
    top: 390px;
  }
  .intro-title{
    display:block;
    width: 322px;
    height: 239px;
    margin-right: 158px;
  }
  .func-area{
    width:511px;
    height:368px;
    background: rgba(255, 255, 255, 0.35);
    border-radius: 8px;
    box-shadow:inset 0px 0px 4px 2px rgba(255, 255, 255, 0.15), 0px 6px 15px  rgba(0, 0, 0, 0.25);
    z-index: 50;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .audio2midi{
    margin-top: 8px;
  }
  .section{
    display: flex;
    justify-content: space-around;
    padding: 10px 0;
    width: 466px;
  }
  .section-item{
    width:124px;
    height:48px;
    font-size: 18px;
    line-height: 48px;
    text-align: center;
  }
  .section-item:hover{
    text-decoration: underline;
  }
  .section-item-active{
    border-radius: 98.55px;
    background: linear-gradient(180deg, rgba(245, 223, 184, 1) 73.61%, rgba(230, 196, 145, 1) 100%);
  }
  .ant-tabs-tab-active{
    color: rgba(61, 70, 78, 1);
  }
  .ant-tabs-tab-btn{
    color: rgba(61, 70, 78, 1);

  }
  .file-drag{
    position: relative;
    display: flex;
    justify-content: center;
    flex-direction:column;
    align-items:center;
    width: 463px;
    height:216px;
    border-radius: 7.92px;
    border: 1px dashed rgba(176, 164, 141, 1);
    background: rgba(255, 255, 255,0);
  }
  .file-drag:hover{
    background:rgba(229, 229, 229, 0.25);
  }
  .file-input{
    width: 100%;
    height: 100%;
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0;
  }
  .music-icon{
    width: 90px;
    height: 90px;
  }
  .music-hint{
    margin-top: 18px;
    width: 288px;
    height: 32px;
  }
  .others-hint{
    width:120px;
    height:40px;
  }
  .options{
    display: flex;
    align-self: flex-start;
    margin-top: 13px;
    justify-content: space-around;
  }

  .options-a{
    display: flex;
    align-items: center;
  }
</style>