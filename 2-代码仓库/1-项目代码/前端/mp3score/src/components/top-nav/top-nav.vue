<template>
    <div class="top-nav">

        <div class="name-wrapper">
            <div class="logo-img"></div>
            <div class="name">麦片谱</div>
        </div>
        
        <div class="nav-wrapper">
            <div class="nav-page">首页</div>
            <div class="nav-page"><p>关于我们</p></div>
            <div class="nav-page"><p>转录记录</p></div>
            <div class="login-icon">登录</div>
        </div>

    </div>
  </template>
  
  <script>
  export default {
     name:'top-nav'
  }
  </script>
  
  <style lang="css" scoped>
    .top-nav{
        width:100%;
        height: 60px;
        background: rgba(255, 255, 255, 0.24);
        box-shadow: 0px 2px 10px  rgba(0, 0, 0, 0.15),inset 0px 0px 4px 2px rgba(255, 255, 255, 0.15);
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: fixed;
        top: 0;
        z-index: 99;
    }
    .name-wrapper{
        display: flex;
        align-items: center;
        margin-left: 118px;
    }
    .logo-img{
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: red;
    }
    .name{
        margin-left: 4px;
    }
    .nav-wrapper{
        display: flex;
        align-items: center;
        margin-right: 121px;
    }
    .nav-page{
        font-weight: 400;
        margin-right: 36px;
    }
    .login-icon{    
        width: 74px;
        height: 34px;
        border-radius: 4px;
        background: rgba(245, 223, 184, 1);
        line-height: 16px;
        box-shadow:inset 0px -2px 1px  rgba(0, 0, 0, 0.25);
        display: flex;
        justify-content: center;
        align-items: center;
    }
  </style>