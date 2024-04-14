<template>
    <div class="index">
        <div class="title">随车文件清单</div>

        <div class="list-container">
            <div class="list-item" v-for="(item,index) in list" :key="item.id" @click='clickEv(item.name,item.src)'>
                <img v-if="item.type ==='pdf'" src="@/assets/pdf.png" class="item-img">
                <img v-else-if="item.type==='word'" src="@/assets/word.png" class="item-img">
                <img v-else src="@/assets/exel.png" class="item-img">

                <div class="item-title">{{ index + '.' + item.name }} </div>
                <div class="item-size">{{item.size}}</div>
            </div>
        </div>
    </div>
</template>
    
<script>
    import getFileList from '@/assets/list'

    export default{
        name:'Index-page',
        data(){
            return{
                list : [
                    {type:'pdf',name:'气路原理图',size:'12.5M',src:'https://dl.djicdn.com/downloads/matrice-300/20240222RN/M300_RTK_Release_Notes_cn_20240222.pdf'},
                    {type:'pdf',name:'气路原理图',size:'12.5M',src:'https://dl.djicdn.com/downloads/matrice-300/20240222RN/M300_RTK_Release_Notes_cn_20240222.pdf'},
                    {type:'pdf',name:'气路原理图',size:'12.5M'},
                    {type:'exel',name:'气路原理图',size:'12.5M'},
                    {type:'pdf',name:'气路原理图',size:'12.5M'},
                    {type:'word',name:'气路原理图',size:'12.5M'},
                    {type:'pdf',name:'气路原理图',size:'12.5M'},
                    {type:'pdf',name:'气路原理图',size:'12.5M'},
                    {type:'pdf',name:'气路原理图',size:'12.5M'},
                    {type:'pdf',name:'气路原理图',size:'12.5M'},
                    {type:'pdf',name:'气路原理图',size:'12.5M'},
                    {type:'png',name:'气路原理图',size:'12.5M'},
                ]
            };
        },
        mounted(){
            let _this = this;
            // setTimeout(function() {
            //     let type = _this.$route.query.type; // 
            //     let id = _this.$route.query.id; // 
            //     console.log(type,id);
            //     _this.list = getFileList(type,id)
            // }, 100);
        },
        methods:{
            clickEv(name,url){
                window.open('http://www.pfile.com.cn/api/profile/onlinePreview?url='+encodeURIComponent(url));
            },
        }
    }
</script>


<style>
.index{
    display: flex;
    flex-direction: column;
    align-items: center;
}
.title{
    font-size: 24px;
    font-weight: bold;
}
.list-container{
    margin-top: 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.list-item{
    display: flex;
    align-items: center;
    justify-content: space-around;
    width: 360px;
    height: 72px;
    background-color: #ffffff;
    margin-bottom: 15px;
    border-radius: 10px;
}
.item-img{
    width: 45px;
    height: 45px;
}
.item-title{
    font-size: 15px;
    font-weight: bold;
    position: relative;
    right: 42px;
}
.item-size{
    font-size: 15px;
    font-weight: bold;
}
</style>