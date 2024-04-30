<template>

<div class="wrapper">
  <div class="main-wrapper">
    <img src="@/assets/index/cloud-1.png" class="cloud-1"/>
    <img src="@/assets/index/cloud-2.png" class="cloud-2"/>
    <img src="@/assets/index/yuan-1.png" class="yuan-1"/>
    <img src="@/assets/index/yuan-2.png" class="yuan-2"/>
    <img src="@/assets/index/intro-title.png" class="intro-title"/>

    <div class="func-area">
        <div class="section">
          <div class="section-item">音频转MIDI</div>
          <div class="section-item">AI音乐生成</div>
          <div class="section-item">音频分离</div>
          <div class="section-item">音频转谱</div>
        </div>
        <div class="file-drag">
            <img src="@/assets/index/music-icon.png" class="music-icon"/>
            <img src="@/assets/index/music-hint.png" class="music-hint"/>
        </div>
        <div class="options">
          <div>
            <input type="radio" id="option1" name="group1" value="option1">
            <label for="option1">纯钢琴</label>
          </div>
          
          <div style="margin-left: 15px;">
            <input type="radio" id="option2" name="group1" value="option2">
            <label for="option2">多音轨</label>
          </div>
        </div>
    </div>

  </div>

  <div class="product-wrapper">
    <our-product></our-product>

  </div>


  <div class="faq-warpper"></div>

  <div class="bottom-wrapper">
    <!-- <bottom-nav/> -->
  </div>


</div>

</template>

<script>
  // import BottomNavComponent from '@/components/bottom-nav/bottom-nav.vue';
  import TopNavComponent from '@/components/top-nav/top-nav.vue';
  import OurProduct from '@/components/our-product/our-product.vue'
  export default {
      name:'Index-Page',
      components:{
        'top-nav' : TopNavComponent,
        // 'bottom-nav' : BottomNavComponent ,
        'our-product' : OurProduct
      },
  }
</script>

<style lang="css" scoped>
  .wrapper{
      width: 100%;
  }
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
    height:340px;
    background: rgba(255, 255, 255, 0.35);
    border-radius: 8px;
    box-shadow:inset 0px 0px 4px 2px rgba(255, 255, 255, 0.15), 0px 6px 15px  rgba(0, 0, 0, 0.25);
    z-index: 50;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .section{
    display: flex;
    justify-content: space-around;
    padding: 10px 0;
  }
  .section-item{
    width:124px;
    height:48px;
    font-size: 18px;
    line-height: 48px;
    text-align: center;
  }
  .file-drag{
    width: 463px;
    height:220px;
    border-radius: 7.92px;
    background: rgba(255, 255, 255, 0);
    border: 1px dashed rgba(176, 164, 141, 1);
  }
  .file-drag{
    display: flex;
    justify-content: center;
    flex-direction:column;
    align-items:center;
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
  .options{
    display: flex;
    align-self: flex-start;
    margin-top: 13px;
    margin-left: 22px;
  }
</style>


  