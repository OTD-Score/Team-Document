<template>
    <div class='wrapper'>
        <div class="content-wrapper">
            <img src="@/assets/login-page/cloud-l.png" class="abo cloud-l">
            <img src="@/assets/login-page/cloud-r.png" class="abo cloud-r">
            <img src="@/assets/login-page/maizi-l.png" class="abo maizi-l">
            <img src="@/assets/login-page/maizi-r.png" class="abo maizi-r">
            <img src="@/assets/login-page/yuan-1.png" class="abo yuan-1">
            <img src="@/assets/login-page/yuan-2.png" class="abo yuan-2">

            <img src="@/assets/login-page/txt.png" class="abo txt-pic">

            <div class="abo login-wrapper">
                <login-input></login-input>
            </div>
        </div>
        <div class="nav-bottom-wrapper">
            <bottom-nav-simple></bottom-nav-simple>
        </div>
    </div>
</template>

<script>
import bottomNavSimple from '@/components/bottom-nav-simple/bottom-nav-simple.vue';
import LoginInput from '@/components/login-input/login-input.vue';


export default{
    name:'loginPage',
    components : {
        'bottom-nav-simple' : bottomNavSimple,
        'login-input' : LoginInput
    }
}
</script>

<style scoped>
    .wrapper{
        width: 100%;
        height: 100%;
    }
    .content-wrapper{
        width: 1920px;
        height: 904px;

        height: 84%;
        background: linear-gradient(180deg, rgba(168, 226, 255, 1) 0%, rgba(255, 255, 255, 1) 49.02%, rgba(255, 251, 240, 1) 100%);
        /* background-image: url('@/assets/login-page/bg.png');
        background-size: 100% 100%; */
        position: relative;
    }
    .nav-bottom-wrapper{
        /* height: 176px; */
        height: 16%;
        z-index: 99;
        position: relative;
    }
    .abo{
        position: absolute;
    }
    .cloud-l{
        width: 548px;
        height: 548px;
        top: -81px;
        right: 156px;
    }
    .cloud-r{
        width: 832px;
        height: 833px;
        top: -262px;
        left: 0px;
    }

    .maizi-l{
        width: 407px;
        height: 229px;
        left: 0;
        bottom: -53px;
    }
    .maizi-r{
        width: 863px;
        height: 233px;
        right: 0;
        bottom: 0;
    }
    .txt-pic{
        width: 508px;
        height: 236px;
        top: 240px;
        left: 392px;
    }
    .yuan-1{
        width: 80px;
        height: 80px;
        left: 961px;
        top: 594px;
    }
    .yuan-2{
        width: 50px;
        height: 50px;
        left: 304px;
        top: 349px;
    }
    .login-wrapper{
        top: 198px;
        left: 961px;
    }
</style>