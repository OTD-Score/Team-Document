<script>
import InputGroup from '../../components/inputGroup.vue'
export default{
    name:'Login-page',
    data(){
        return{
            phone:"",
            verifyCode:"",
            errors:{},
            btnTitle:"获取验证码",
            disabled:false
        };
    },
    computed:{
        isClick(){
            if(!this.phone||!this.verifyCode) return true;
            else return false;
        }
    },
    methods:{
        handleLogin(){
            // 取消错误提醒
            this.errors={};
            // 发送请求
            this.$axios.post("/api/posts/sms_back",{
                phone:this.phone,
                code:this.verifyCode
            })
            .then(res=>{
                console.log(res);
                // 检验成功 设置登录状态并跳转到/
                localStorage.setItem("MP3",true);
                this.$router.push("/");
            })
            .catch(err=>{
                // 返回错误信息
                this.errors={
                    code:err.response.data.msg
                };
            })
        },
        getVerifyCode(){
            if(this.validatePhone()){
                // 发送网络请求
                this.validateBtn();
                this.$axios.post("/api/posts/sms_send",{
                    tpl_id:"  ",
                    key: "  " ,
                    phone:this.phone
                })
                .then(res=>{
                    console.log(res);
                });
            }
        },
        validateBtn(){
            let time=60;
            let timer=setInterval(()=>{
                if(time==0){
                    clearInterval(timer)
                    this.btnTitle="获取验证码";
                    this.disabled=false;
                }else{
                    // 倒计时
                    this.btnTitle=time+"秒后重试";
                    this.disabled=true;
                    time--;
                }
            },1000)
        },
        validatePhone(){
            // 验证手机号码
            if(!this.phone){
                this.errors={
                    phone:"手机号码不能为空"
                };
                return false;
            }else if(!/^1[345678]\d{9}$/.test(this.phone)){
                this.errors={
                    phone:"请填写正确的手机号码"
                };
                return false;
            }else{
                this.errors={};
                return true;
            }
        }
    },
    components:{
        InputGroup
    }
}
</script>
<template>
    <div class="body">
    <div class="write">
        <img src="../../assets/login-character.png">
    </div>
    <div class="login">
        <div class="logo">
            <img src="../../assets/logo -b.png" alt="my login image">
        </div>
        <div class="dl">验证码登录</div>
        <div class="text">
        <!-- 手机号 -->
        <InputGroup class="text-phone" type="text" v-model="phone" placeholder="手机号"  :disabled="disabled" :error="errors.phone"  ></InputGroup>
        <!-- 验证码 -->
        <InputGroup class="text-verifyCode" type="text" v-model="verifyCode" placeholder="验证码"  :btnTitle="btnTitle" :error="errors.code" @btnClick="getVerifyCode"></InputGroup>
        <!-- 用户服务协议 -->
        <div class="login_des">
            <p>
                未注册手机验证后自动登录，注册即代表同意
                <span>《麦片谱用户使用协议》《隐私协议》</span>
            </p>
        </div>
        <!-- 登录按钮 -->
        <div class="login_btn">
            <button :disabled="isClick" @click="handleLogin">登录</button>
        </div>
        </div>
    </div>
    <div class="footer">
        <p>关于我们&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;法律声明及隐私政策&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系我们&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;关注我们</p>
        <p>长沙理工大学</p>
        <p>备案号</p>
    </div>
    </div>
      
    </template>
<style>
/* .body{
    width: 1440px;
    height: 951px;
    background-image: url('../../assets/login.png');
} */
.body {
  position: relative; /* 设置为相对定位，使子元素相对于它定位 */
  top:10%;
  left:25%;
  width: 1440px; /* 设置宽度为视口宽度 */
  height: 951px; /* 设置高度为视口高度 */
  display: flex; /* 使用flex布局 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  background-image: url('../../assets/login.png');
  background-size: contain; /* 调整背景图片大小，保持比例 */
  background-position: center; /* 设置背景图片在容器中水平和垂直居中 */
  background-repeat: no-repeat; /* 防止背景图片重复 */
}
/* .flex-grow {
  flex-grow: 1;
} */
.write {
  position: absolute;
  left: 8%; /* 相对于父元素宽度的25% */
  top: 29%; /* 相对于父元素高度的25% */
  width: 35%;
  height: 29%;
}

.login {
  position: absolute;
  left: 44.65%; 
  top: 14.19%; 
  width: 50%; 
  height: 59%; 
  opacity: 1;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.24);
  box-shadow: inset 0px 2px 4px 2px rgba(255, 255, 255, 0.15), 0px 4px 8px rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(100px);
}

.logo{
    text-align: center;
}
.logo img{
    position: absolute;
  left: 44%; 
  top: 3%; 
  width: 11%; 
  height: 14%; 
}
.dl{
    position: absolute;
    left: 41%;
top: 25%;
width: 20%;
height: 6%;
opacity: 1;
font-size: 24px;
font-weight: 400;
letter-spacing: 0px;
line-height: 34.75px;
color: rgba(56, 56, 56, 1);
text-align: left;
vertical-align: top;
font-family: 'Source Han Sans', sans-serif; /* 设置字体为思源黑体 */
}
/* 输入框组件 */
.text_group,
.login_des,
.login_btn{
    margin-top: 20px;
}
.text-phone{
    position: absolute;
    left: 15%;
top: 31%;
width: 70%;
height: 10%;
opacity: 1;
border-radius: 24px;
background: rgba(255, 255, 255, 1);
}
.text-verifyCode{
    position: absolute;
    left: 15%;
top: 47%;
width: 70%;
height: 10%;
opacity: 1;
border-radius: 24px;
background: rgba(255, 255, 255, 1);
}

/* 文字 */
.login_des{
    position: absolute;
    left: 30%;
top: 75%;
width: 40%;
height: 10%;
opacity: 1;
/** 文本1 */
font-size: 14px;
font-weight: 400;
letter-spacing: 0px;
line-height: 20.27px;
color: rgba(166, 166, 166, 1);
/** 文本2 */
font-size: 14px;
font-weight: 400;
letter-spacing: 0px;
line-height: 20.27px;
color: rgba(167, 145, 124, 1);
text-align: center;
vertical-align: top;
font-family: 'Source Han Sans', sans-serif; /* 设置字体为思源黑体 */
}

/* 登录按钮 */
.login_btn button{
    position: absolute;
    left: 15%;
top: 65%;
width: 70%;
height: 10%;
opacity: 1;
border-radius: 24px;
background: rgba(245, 223, 184, 1);
box-shadow: 0px 2px 4px  rgba(0, 0, 0, 0.25);
font-size: 18px;
font-weight: 400;
letter-spacing: 0px;
line-height: 26.06px;
color: rgba(167, 145, 124, 1);
text-align: center;
vertical-align:top;
}
.login_btn button[disabled]{
    background-color: rgba(245, 223, 184, 1);
}
.footer{
    position: absolute;
    left: 0;
    top: 80%;
width: 100%;
height: 20%;
opacity: 1;
background: rgba(67, 70, 79, 1);
opacity: 1;
/** 文本1 */
font-size: 16px;
font-weight: 400;
letter-spacing: 0px;
line-height: 40px;
color: rgba(186, 181, 181, 1);
text-align: center;
vertical-align: top;

}
</style>