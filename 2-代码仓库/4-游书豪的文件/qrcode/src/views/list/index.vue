<template>
    <div class="index">
        <div class="title">车辆信息详情</div>

        <div class="list-container">
            <div class="list-item" v-for="(item,index) in list" :key="item.id" @click='clickEv(item.name,item.url)'>
                <img v-if="item.type ==='pdf'" src="@/assets/pdf.png" class="item-img">
                <img v-else-if="item.type==='word'" src="@/assets/word.png" class="item-img">
                <img v-else src="@/assets/exel.png" class="item-img">

                <div class="item-title">{{ (index+1) + '.' + item.name }} </div>
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
                    {type:'pdf',name:'气路原理图',size:'12.5M',url:''},
                ]
            };
        },
        mounted(){
            let _this = this;
            //type = '21M' "51M" "65M" "CYC" "ZJC" "LYC" "SYC" "ZZXC"
            setTimeout(function() {
                let type = _this.$route.query.type; // 
                let id = _this.$route.query.id; // 
                // console.log(type,id);
                _this.list = getFileList(type,id)
            }, 100);
        },
        methods:{
            clickEv(name,url){
                console.log(url + name);
                window.open('http://www.pfile.com.cn/api/profile/onlinePreview?url='+encodeURIComponent(url + name));
            },
        }
    }
</script>


<style>
.index{
    display: flex;
    flex-direction: column;
    align-items: center;
    box-sizing: border-box;
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
    position: relative;
    display: flex;
    align-items: center;
    width: 360px;
    height: 72px;
    background-color: #ffffff;
    margin-bottom: 15px;
    border-radius: 10px;
}
.item-img{
    display: block;
    width: 40px;
    height: 40px;
    position: relative;
    left: 10px;
}
.item-title{
    font-size: 15px;
    font-weight: bold;
    width: 220px;
    white-space: nowrap;
    overflow-x: scroll;
    position: relative;
    left: 25px;
    text-align: left;
    display: flex;
}
.item-size{
    font-size: 15px;
    font-weight: bold;
    position: absolute;
    right: 5px;
}
</style>