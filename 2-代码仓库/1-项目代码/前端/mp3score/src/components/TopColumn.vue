<template>
  <div id="header">
    <div id="headchild1"></div>
    <div id="headchild2"><p>麦片谱</p></div>
    <div id="headchild3">首页</div>
    <div id="headchild4"><p>关于我们</p></div>
    <div id="headchild5"><p>转录记录</p></div>
    <div id="headchild6">登录</div>
  </div>
</template>

<script>
export default {
   name:'Top-Column'
}
</script>

<style lang="css" scoped>
#header{
    left: 4px;
    top: 0px;
    width: 100%;
    height: 96px;
    opacity: 1;
    border-radius: 4px;
    background: rgba(255, 255, 255, 0.24);
    border: 1px solid rgba(255, 255, 255, 1);
    box-shadow: 0px 2px 10px  rgba(0, 0, 0, 0.15),inset 0px 0px 4px 2px rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(100px);
    position: fixed;
    z-index: 1;
  }
  #headchild1{
    left: 5%;
    top: 25%;
    width: 42.95px;
    height: 42.95px;
    opacity: 1;
    background: rgba(245, 223, 184, 1);
    position:absolute;
  }
  p{
    font-size: 25px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 21.12px;
    color: rgba(101, 94, 78, 1);
    text-align: left;
    vertical-align: middle;  
  }
  #headchild2{
    left: 8%;
    top: 10%;
    width: 82px;
    height: 22px;
    opacity: 1; 
    position:absolute;
  }
  #headchild3{
    left: 65%;
    top: 48%;
    width: 62px;
    height: 22px;
    opacity: 1;
    position: absolute;
    font-size: 25px;
    font-weight: 700;
    letter-spacing: 0px;
    line-height: 0px;
    color: rgba(101, 94, 78, 1);
    text-align: left;
    /* vertical-align: top; */
  }
  #headchild4{    
    left: 71%;
    top: 10%;
    width: 104px;
    height: 24.55px;
    opacity: 1;
    position:absolute;    
  }
  #headchild5{    
    left: 80%;
    top: 10%;
    width: 104px;
    height: 24.55px;
    opacity: 1;
    position:absolute;  
  }
  #headchild6{    
    left: 88%;
    top: 25%;
    width: 104px;
    height: 24.55px;
    opacity: 1;
    display: flex;
    position:absolute;
    border-radius: 4px;
    background: rgba(245, 223, 184, 1);
    box-shadow:inset 0px -2px 1px  rgba(0, 0, 0, 0.25);
    justify-content: center;
    align-items: center;
    padding: 9px 29px 9px 29px;
    font-size: 22px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 21.12px;
    color: rgba(101, 94, 78, 1);
    vertical-align: middle;  
  }
</style>