<template>
    <div class='wrapper'>
        <div class="logo"></div>
        <div class="login-type-area">验证码登录</div>

        <div class="input-wrapper">
            <label class="input-label" for="phone-num">+86</label>
            <input class="input-input" id="phone-num" type="text" placeholder="手机号">
        </div>

        <div class="input-wrapper">
            <label class="input-label" for="sms-code">验证码</label>
            <input class="input-input" id="sms-code" type="text" placeholder="短信验证码">
            <div class="ValidCode-btn">获取验证码</div>
        </div>

        <div class="submit-btn">登录</div>

        <div class="desc">未注册手机验证后自动登录，注册即代表同意<br>
            <span>《麦片谱用户使用协议》</span>
            <span>《隐私协议》</span>
        </div>

    </div>
</template>

<script>
export default{
    name:'loginInput',
}
</script>

<style scoped>
    .wrapper{
        width: 519.28px;
        height: 400.55px;
        border-radius: 24px;
        background: rgba(255, 255, 255, 0.24);
        box-shadow:inset 0px 2px 4px 2px rgba(255, 255, 255, 0.15), 0px 4px 8px  rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(100px);
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .logo{
        margin-top: 36px;
        width: 53px;
        height: 53px;
        background-color: rgba(245, 223, 184, 1);
    }
    .login-type-area{
        margin-top: 29px;
        font-size: 18px;
        color: rgba(56, 56, 56, 1);
    }
    .input-wrapper{
        width: 365px;
        height: 39px;
        border-radius: 24px;
        background: rgba(255, 255, 255, 1);
        display: flex;
        align-items: center;
    }
    .input-wrapper:not(:first-child){
        margin-top: 17px;
    }
    .input-label{
        display: inline-block;
        margin-left: 16px;
        line-height: 39px;
        font-size: 16px;
        color: rgba(128, 128, 128, 1);
    }
    .input-input{
        margin-left: 10px;
        border: none;
        height: 39px;
        line-height: 39px;
        display: inline-block;
        width: 170px;
        vertical-align: middle;
        font-size: 16px;
    }
    .input-input::placeholder{
        font-size: 16px;
        vertical-align: middle;

    }
    .input-input:focus{
        outline: none;
    }
    #phone-num{
        width: 220px;
    }
    .ValidCode-btn{
        margin-left: 6px;
        width: 94px;
        height: 28px;
        border-radius: 24px;
        background: rgba(245, 223, 184, 0.4);
        border: 1px solid rgba(245, 223, 184, 1);
        font-size: 14px;
        color: rgba(167, 145, 124, 1);
        text-align: center;
        line-height: 28px;
    }

    .submit-btn{
        margin-top: 25px;
        width: 365px;
        height: 35px;
        border-radius: 24px;
        background: rgba(245, 223, 184, 1);
        box-shadow: 0px 2px 4px  rgba(0, 0, 0, 0.25);
        font-size: 18px;
        line-height: 26px;
        color: rgba(167, 145, 124, 1);
        text-align: center;
        line-height: 35px;
    }
    .desc{
        margin-top: 13px;
        font-size: 12px;
        color: rgba(166, 166, 166, 1);
        line-height: 17px;
    }
    .desc>span{
        color: rgba(167, 145, 124, 1);
    }
</style>