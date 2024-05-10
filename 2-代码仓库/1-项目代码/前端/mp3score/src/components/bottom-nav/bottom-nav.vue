<template>
    <div class='wrapper'>
      <div class="top-area">
        <div class="item">
          <div class="title">功能地图</div>
          <div class="nav-item">MP3转MIDI文件</div>
          <div class="nav-item">MP3转PDF谱</div>
          <div class="nav-item">伴奏分离</div>
          <div class="nav-item">AI音乐生成</div>
          <div class="nav-item">转录记录</div>
        </div>
        
        <div class="item item-1">
          <div class="title">规则条款</div>
          <div class="nav-item">服务条款</div>
          <div class="nav-item">隐私政策</div>
          <div class="nav-item">关于我们</div>
        </div>
        <div class="item item-1">
          <div class="title">联系我们</div>
          <div class="nav-item">联系方式：15575936492</div>
          <div class="nav-item">邮箱：569513303@qq.com</div>
          <div class="nav-item">地址：湖南省长沙市长沙理工大学</div>
        </div>

        <div class="item item-2">
          <div class="title">关注我们</div>
          <img src="@/assets/bottom-nav/icon-bili.png" class="icon">
          <img src="@/assets/bottom-nav/icon-wechat.png" class="icon">
          <img src="@/assets/bottom-nav/icon-dy.png" class="icon">
          <img src="@/assets/bottom-nav/icon-git.png" class="icon">
        </div>
      </div>

      <div class="bottom-area">
        <div class="beianhao">备案号:湘A222222</div>
      </div>
    </div>
</template>

<script>
export default{
    name:'bottom-nav',
}
</script>

<style scoped>
  .wrapper{
    width: 1920px;
    height: 450px;
    background: rgba(67, 70, 79, 1);
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .top-area{
    padding-top: 70px;
    display: flex;
    justify-content: center;
  }
  .item{
    line-height: 40px;
  }
  .item-1{
    margin-left: 90px;
  }
  .item-2{
    margin-left: 112px;
  }
  .item-3{
    margin-left: 110px;
  }
  .title{
    color: #ffffff;
  }
  .nav-item{
    font-size: 14px;
    color: rgba(181, 186, 182, 1);
  }
  .bottom-area{
    margin-top: 50px;
    width: 1200px;
    border-top: 1px solid rgba(125, 125, 125, 1);
  }
  .beianhao{
    margin-top: 20px;
    text-align: center;
    color: #ffffff;
  }
  .icon{
    width: 41px;
    height: 41px;
    margin-right: 10px;
  }
</style>