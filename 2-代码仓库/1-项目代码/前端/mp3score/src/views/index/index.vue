<template>

  <div class="wrapper">
    <!-- 顶部功能区 -->
    <div class="top-area">
      <func-area @start-stop-upload="startOrStopUpLoad" @upload-file-data="getUploadFileData"></func-area>
    </div>

    <!-- 进度条区 -->
    <div class="process-area" :class=" showProgress ? 'show-class'  : 'hidden-class'">
      <process-area :file-data="fileData" :upload-flag="uploadFlag"></process-area>
    </div>

    <!-- 我们的产品 -->
    <div class="product-wrapper">
      <our-product></our-product>
    </div>

    <!-- 常见问题 -->
    <div class="faq-warpper">
      <q-a-area></q-a-area>
    </div>

    <!-- 底部导航 -->
    <div class="bottom-wrapper">
      <bottom-nav></bottom-nav>
    </div>
  </div>

</template>

<script>
  import FuncAreaComponent from '@/components/func-area/func-area.vue';
  import ProcessAreaComponent from '@/components/process-area/process-area.vue';
  import TopNavComponent from '@/components/top-nav/top-nav.vue';
  import OurProductComponent from '@/components/our-product/our-product.vue';
  import QAComponent from '@/components/QA-area/qa-area.vue';
  import BottomNavComponent from '@/components/bottom-nav/bottom-nav.vue';

  export default {
      name:'Index-Page',
      data(){
        return {
          showProgress : false ,
          uploadFlag : '0' ,
          fileData : {},
        }
      },
      components:{
        'top-nav' : TopNavComponent,
        'process-area' : ProcessAreaComponent,
        'func-area' : FuncAreaComponent,
        'bottom-nav' : BottomNavComponent ,
        'our-product' : OurProductComponent,
        'q-a-area' :QAComponent,
      },
      methods : {
        startOrStopUpLoad(flag){
          //只要收到，就把进度条区域打开，然后再也不关上
          if(flag){
            this.showProgress = true;
          }
          //把数据传到子组件里去
          this.uploadFlag = flag;
        },
        getUploadFileData(data){
          //组件传上来的数据是data
          this.fileData = data;
        }
      }
  }
</script>

<style lang="css" scoped>
  .wrapper{
      width: 100%;
  }
  .hidden-class{
    position: absolute;
    opacity: 0;
  }
  .show-class{
    position: relative;
    opacity: 1;
  }
</style>


  