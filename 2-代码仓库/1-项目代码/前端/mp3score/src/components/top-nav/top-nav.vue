<template>
    <div class="top-nav">

        <div class="name-wrapper">
            <img class="logo-img" src="@/assets/logo.png"/>
            <div class="name">MP3Score</div>
        </div>
        
        <div class="nav-wrapper">
            <div class="nav-page" data-index="1" @click="navClick">首页</div>
            <div class="nav-page" data-index="2" @click="navClick">关于我们</div>
            <div class="nav-page" data-index="3" @click="navClick">转录记录</div>
            <div class="login-icon" data-index="4" @click="navClick">登录</div>
        </div>

    </div>
  </template>
  
  <script>
  export default {
     name:'top-nav',
     methods : {
        navClick(e){
            let index = e.target.dataset.index ;
            if(index == 1){
                this.$router.push('/')
            }else if(index == 2){
                this.$router.push('/about')
            }
            else if(index == 3){
                this.$router.push('/record')
            }
            else if(index == 4){
                this.$router.push('/login')
            }
        }
     }
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
        z-index: 999;
    }
    .name-wrapper{
        display: flex;
        align-items: center;
        margin-left: 118px;
    }
    .logo-img{
        width: 40px;
        height: 40px;
    }
    .name{
        margin-left: 20px;
    }
    .nav-wrapper{
        display: flex;
        align-items: center;
        margin-right: 121px;
    }
    .nav-page{
        font-weight: 400;
        margin-right: 36px;
        color:rgba(101, 94, 78, 1)
    }
    .nav-page:hover{
        text-decoration: underline;
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