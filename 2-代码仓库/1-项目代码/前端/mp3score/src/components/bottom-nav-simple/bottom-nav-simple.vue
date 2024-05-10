<template>
    <div class='wrapper'>
      <div class="nav-area">
        <div class="nav-item">关于我们</div>
        <div class="nav-item">法律声明及隐私政策</div>
        <div class="nav-item">联系我们</div>
        <div class="nav-item">关注我们</div>
      </div>

      <div class="cop">长沙三尺剑网络科技有限公司</div>

      <div class="beianhao">湘45ASD</div>
    </div>
</template>

<script>
export default{
    name:'bottomNavSimple',
}
</script>

<style scoped>
  .wrapper{
    width: 100%;
    height: 100%;
    background: rgba(67, 70, 79, 1);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 16px;
    color: rgba(186, 181, 181, 1);
    line-height: 40px;

  }
  .nav-area{
    display: flex;
    justify-content: space-around;
  }
  .nav-item:not(:first-child){
    margin-left: 20px;
  }
  .cop{
    margin-top: 2px;
    color: #ffffff;
  }
  .beianhao{
    margin-top: 2px;
  }
</style>