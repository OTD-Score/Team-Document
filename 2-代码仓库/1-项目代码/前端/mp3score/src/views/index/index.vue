<template>

  <div class="wrapper">
    <!-- 顶部功能区 -->
    <div class="top-area">
      <func-area></func-area>
    </div>

    <!-- 进度条区 -->
    <div class="process-area">
      <process-area></process-area>
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
      components:{
        'top-nav' : TopNavComponent,
        'process-area' : ProcessAreaComponent,
        'func-area' : FuncAreaComponent,
        'bottom-nav' : BottomNavComponent ,
        'our-product' : OurProductComponent,
        'q-a-area' :QAComponent,
      },
  }
</script>

<style lang="css" scoped>
  .wrapper{
      width: 100%;
  }
  
</style>


  