<template>
    <div class='wrapper'>
        <img src="@/assets/qa-area/bg-l.png" class="abo bg-l">
        <img src="@/assets/qa-area/bg-r.png" class="abo bg-r">
        <img src="@/assets/qa-area/bg-top.png" class="abo bg-top">


        <div class="content-box">
            <div class="r-title">常见问题</div>

            <div class="content-box-box">
                <div class="left-box">
                    <div class="left-item">常见问题</div>
                    <div class="left-item">我们的产品</div>
                    <div class="left-item">工作原理</div>
                    <div class="left-item">关于我们</div>
                </div>

                <div class="right-box">
                    <!-- Colapse下拉文字 -->
                    <div class="colapse-wrapper">
                        <a-collapse ghost v-model:activeKey="activeKey" expand-icon-position="end">
                            <a-collapse-panel key="1" header="This is panel header 1">
                                <p>{{ text }}</p>
                            </a-collapse-panel>
                            <a-collapse-panel key="2" header="This is panel header 2">
                                <p>{{ text }}</p>
                            </a-collapse-panel>
                            <a-collapse-panel key="3" header="This is panel header 2">
                                <p>{{ text }}</p>
                            </a-collapse-panel>
                            <a-collapse-panel key="4" header="This is panel header 2">
                                <p>{{ text }}</p>
                            </a-collapse-panel>
                            <a-collapse-panel key="5" header="This is panel header 2">
                                <p>{{ text }}</p>
                            </a-collapse-panel>
                        </a-collapse>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {Collapse,CollapsePanel} from 'ant-design-vue'

export default{
    name:'qa-area',
    data(){
        return {
            text : '我是祝杰伦'
        }
    }, 
    components:{
        'a-collapse' : Collapse,
        'a-collapse-panel' : CollapsePanel
    }
}
</script>

<style scoped>
    .wrapper{
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        box-sizing: border-box;
    }
    .abo{
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
    }
    .bg-l{
        width: 1920px;
        height: 544px;
    }
    .bg-r{
        width: 1920px;
        height: 595px;
    }
    .bg-top{
        width: 1920px;
        height: 135px;
        top: 35px;
    }
    .content-box{
        width: 1920px;
        /* height: 212px; */
        margin-top: 158px;
        z-index: 99;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-bottom: 30px;
        background: linear-gradient(180deg, rgba(255, 251, 240, 0.77) 0%,rgba(245, 223, 184, 1) 100% );
    }
    .r-title{
        margin-bottom:30px ;
        position: relative;
        right: 50px;
        font-size: 24px;
        color: rgba(74, 79, 56, 1);
        font-weight:700;
    }

    .content-box-box{
        display: flex;
    }
    .left-box{
        width: 400px;
    }
    .left-item{
        width: 397.7px;
        height: 40.82px;
        margin-top: 12px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.25);
        box-shadow:inset 0px 4px 4px 2px rgba(255, 255, 255, 0.15);
        color: rgba(101, 94, 78, 1);
        text-align: center;
        line-height: 40px;
    }
    .right-box{
        margin-left: 50px;
        width: 645px;
        padding-bottom: 30px;
    }
    .ant-collapse{
        font-size: 16px;
        padding: 12px 16px;
    }
    .ant-collapse-item{
        border-bottom: 1px solid #000000;
    }

</style>