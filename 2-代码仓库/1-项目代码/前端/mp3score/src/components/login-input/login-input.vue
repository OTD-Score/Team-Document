<template>
    <div class='inner-wrapper'>
        <div class="logo"></div>
        <div class="login-type-area">验证码登录</div>

        <div class="input-wrapper">
            <label class="input-label" for="phone-num">+86</label>
            <input class="input-input" id="phone-num" type="text" placeholder="手机号" v-model="phone_num">
        </div>

        <div class="input-wrapper">
            <label class="input-label" for="sms-code">验证码</label>
            <input class="input-input" id="sms-code" type="text" placeholder="短信验证码" v-model="valid_code">
            <div class="ValidCode-btn" :class="valid_active_class"  @click="geiValidCode">{{ valid_code_applying ?  valid_count_down_num : '获取验证码'}}</div>
        </div>

        <div class="hint-txt" v-if="hint_status != '1'">{{ hint_desc }}</div>

        <div class="submit-btn" :class="submit_active_class" @click="loginSubmit">登录</div>

        <div class="desc">未注册手机验证后自动登录，注册即代表同意<br>
            <span>《麦片谱用户使用协议》</span>
            <span>《隐私协议》</span>
        </div>

    </div>
</template>

<script>
import Req from '@/utils/request';
import Util from '@/utils/util' ;

export default{
    name:'loginInput',
    data(){
        return {
            phone_num : '',
            valid_code : '',
            hint_status : '1',//提示状态 见hint_desc
            valid_active : false,
            valid_loading : false,//获取验证码按钮请求中状态
            valid_code_applying : false, //验证码请求发至服务器了，在倒计时等响应
            valid_count_down_num : 60,
            valid_timer : null,//计时器
            login_loading : false,
        }
    },
    computed : {
        submit_active(){
            let if_phone_legal = this.if_phone_valid(this.phone_num);
            let if_valid_legal = this.if_code_valid(this.valid_code);
            return if_phone_legal && if_valid_legal ;
        },  
        valid_active_class(){
            return this.valid_active ? 'ValidCode-btn-active' : 'ValidCode-btn-inactive'
        },
        submit_active_class(){
            return this.submit_active ? 'submit-btn-active' : 'submit-btn-inactive'
        }, 
        
        hint_desc(){
            switch(this.hint_status){
                case '2' : 
                    return '手机号不能为空'
                case '3' : 
                    return '手机号码格式不正确，请重新输入'
                case '4' : 
                    return '不可频繁请求，请稍后'
                case '5' :
                    return  '验证码错误'
                case '6' :
                    return  '请求验证码失败，请稍后重试' 
             }
        }
    },
    watch : {
        phone_num(new_phone , old_phone){
            const regEx = /^[1][3-9]\d{9}$/;
            let if_legal = regEx.test(new_phone);

            if(new_phone.length == 0){
                this.valid_active = false ;
                this.hint_status = '2';
                return;
            }
            if(if_legal){
                this.valid_active = true ;
                this.hint_status = '1';
            }else{
                this.valid_active = false ;
                this.hint_status = '3';
            }
        },

    },  
    mounted() {
        let EndTime= Util.sessionGet('EndTime');
        if(EndTime){
            this.timeCountDown(EndTime);
        }
    },
    methods: {
        geiValidCode(e) {
            if(this.valid_code_applying){
                this.hint_status = '4';
                return ;
            }
           //获取验证码
           if(!this.valid_active || this.valid_loading ){
                return;
           }
  
           Req.postReq('getValidCode').then(res => {
                this.valid_loading = true ;
                if(res.code == 1){
                    this.hint_status = '1'
                    let clicktime = new Date().getTime() + 60000;   //未来60秒，这里也毫秒为单位
                    Util.sessionSet('EndTime', JSON.stringify(clicktime));  //存入sessionStorage
                    this.timeCountDown(clicktime);//倒计时60s
                }else{
                    this.hint_status = '6' ;
                }
           }).catch(err =>{

           }).finally(()=>{
                this.valid_loading = false ;
           })
        },
        timeCountDown(n_time){
            if (!this.timer) {
                this.valid_count_down_num = Math.ceil((JSON.parse(n_time) - new Date().getTime())/1000);  //取出计时
                this.valid_code_applying = true;
                this.timer = setInterval(() => {
                    if (this.valid_count_down_num > 0) {
                        this.valid_count_down_num--;
                    } else {
                        this.valid_active = true ;
                        this.valid_code_applying = false;
                        clearInterval(this.timer);  //清除计时器
                        this.timer = null;
                        Util.sessionRemove('EndTime')  //计时完后清除sessionStorage
                    }
                }, 1000)
            }
        },
        if_phone_valid(phone_num){
            const regEx = /^[1][3-9]\d{9}$/;
            return regEx.test(phone_num);
        },
        if_code_valid(code){
            const regEx = /^[A-Za-z0-9]{6}$/ ;
            return regEx.test(code);
        },
        login(e){
            let user_tel = this.phone_num ; 
            let verify_code = this.valid_code ;
            this.login_loading = true;

            Util.postReq('login',{
                user_tel,
                verify_code
            }).then(res=>{
                if(res.code == 1){
                    let token = res.dara.token || null ;
                    Util.localStorageSet('token',token);
                    this.$route.go(-1).then(navigationResult =>{//从哪里来的到哪里去，一般是个人中心
                        if(navigationResult){
                            // 导航被阻止
                            this.$route.replace('/')
                        }
                    });
                }else if(res.code == 2){//假设2代表验证码错误
                    this.hint_status = '5';
                }
            }).finally(()=>{
                this.login_loading = false ;
            })
        }

    }
}
</script>

<style scoped>
    .inner-wrapper{
        width: 520px;
        height: 400px;
        border-radius: 24px;
        background: rgba(255, 255, 255, 0.24);
        box-shadow:inset 0px 2px 4px 2px rgba(255, 255, 255, 0.15), 0px 4px 8px  rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(100px);
        display: flex;
        flex-direction: column;
        align-items: center;
        box-sizing: border-box;
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
        font-size: 14px;
        text-align: center;
        line-height: 28px;
        box-shadow: 0px 2px 4px  rgba(0, 0, 0, 0.25);
        color: rgba(167, 145, 124, 1);
        border: 1px solid rgba(245, 223, 184, 1);
    }
    .ValidCode-btn:active{
        transform: scale(1.05)
    }
    .submit-btn:active{
        transform: scale(1.05)
    }
    .ValidCode-btn-inactive{
        background: rgba(242, 232, 213, 1);
    }
    .ValidCode-btn-active{
        background: rgba(255, 245, 227, 1);
    }

    .submit-btn{
        margin-top: 25px;
        width: 365px;
        height: 35px;
        border-radius: 24px;
        box-shadow: 0px 2px 4px  rgba(0, 0, 0, 0.25);
        font-size: 18px;
        line-height: 26px;
        color: rgba(167, 145, 124, 1);
        text-align: center;
        line-height: 35px;
    }
    .submit-btn-active{
        background: rgba(255, 234, 199, 1);
    }
    .submit-btn-inactive{
        background: rgba(245, 223, 184, 1);

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
    .hint-txt{
        margin-top: 10px;
        font-size: 14px;
        color: #f15533;
        align-self: flex-start;
        position: relative;
        left: 90px;
    }
</style>