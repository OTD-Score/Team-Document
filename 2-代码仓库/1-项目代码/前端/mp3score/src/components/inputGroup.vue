<template>
    <div class="text_group">
        <!-- 组件结构 -->
        <!-- 组件容器 -->
        <div class="input_group" :class="{'is_invalid':error}">
            <!-- 输入框 -->
            <input :type="type" :value="value" :placeholder="placeholder" :name="name" @input="$emit('input',$event.target.value)">
            <!-- 输入框后面的按钮 -->
            <button v-if="btnTitle" :disabled="disabled" @click="$emit('btnClick')">{{ btnTitle }}</button>
        </div>
            <!-- 错误提醒 -->
            <div v-if="error" class="invalid-feedback">{{ error }}</div>
        </div>
    </template>
    
<script>
export default{
    name:'inputGroup',
    props:{
        type:{
            type:String,
            default:"text"
        },
        value:String,
        placeholder:String,
        name:String,
        btnTitle:String,
        disabled:Boolean,
        error:String
    }
}
</script>
<style scoped>
.input_group{
    border: none;
}
.input_group input{
    position: relative;
    border: none;
    padding: 15px 10px;
border-radius: 24px;
width: 96%;
height: 100%;
opacity: 1;
/** 文本1 */
font-size: 18px;
font-weight: 400;
letter-spacing: 0px;
line-height: normal;
color: rgba(128, 128, 128, 1);
text-align: left;
vertical-align: center;
font-family: 'Source Han Sans', sans-serif; /* 设置字体为思源黑体 */
}
.input_group button{
    position: relative;

    left:357px;
top: -45.11px;
width: 141px;
height: 42.79px;
opacity: 1;
border-radius: 24px;
background: rgba(245, 223, 184, 0.4);
border: 1px solid rgba(245, 223, 184, 1);
font-size: 18px;
font-weight: 400;
letter-spacing: 0px;
line-height: 26.06px;
color: rgba(167, 145, 124, 1);
text-align: center;
vertical-align: top;
font-family: 'Source Han Sans', sans-serif; 


/* opacity: 1;
/** 文本1 */
/* font-size: 18px;
font-weight: 400;
letter-spacing: 0px;
line-height: 100%;
color: rgba(128, 128, 128, 1);
text-align: center;
vertical-align: middle;
    border:none;
    outline:none;
    background: #F5DFB8;  */
/* font-family: 'Source Han Sans', sans-serif;  */

}
/* .input_group button{
    background-color: #F5DFB8;
} */
.is_invalid{
    border:1px solid red;
    border-radius: 24px;

}
.invalid-feedback{
    color:red;
    padding-top: 5px;
}
</style>