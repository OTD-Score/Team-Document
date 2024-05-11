<template>
    <div class="wrapper">
        <div class="top-area">
            <img src="@/assets/record/bg-shadow.png" class="bg-shadow">
            
            <div class="tips">
                <img src="@/assets/record/tips.png" class="tips-icon">
                <div>温馨提示：文件转换过程预计需要1~3分钟，微信小程序登录的用户转换完成后会以微信消息进行通知~</div>
            </div>

            <div class="order-list">
                <!-- 进行中订单 -->
                <div class="order-item">
                    <img src="@/assets/record/icon-mp3.png" class="icon-mp3">

                    <div class="item-name-area">
                        <div class="item-name">
                            <div class="item-name-name">义勇军进行曲.mid</div>
                            <div class="item-name-type">MP3</div>
                        </div>
                        <div class="order-num">订单号：20247484555</div>
                    </div>

                    <img src="@/assets/record/icon-mp3.png" alt="" class="result-type-icon">

                    <div class="result-type-txt">MIDI</div>

                    <div class="progress">
                        <a-progress :percent="50" status="active"></a-progress>
                    </div>

                    <img src="@/assets/progress-area/preview-btn.png" class="btn preview-btn"/>
                    <img src="@/assets/progress-area/dowload-btn.png" class="btn dowload-btn"/>

                    <div class="date">2024-01-30</div>
                </div>
                <!-- 完成订单 -->

                <div class="order-item">
                    <img src="@/assets/record/icon-mp3.png" class="icon-mp3">

                    <div class="item-name-area">
                        <div class="item-name">
                            <div class="item-name-name">义勇军进行曲.mid</div>
                            <div class="item-name-type">MP3</div>
                        </div>
                        <div class="order-num">订单号：20247484555</div>
                    </div>

                    <img src="@/assets/record/icon-mp3.png" alt="" class="result-type-icon">

                    <div class="result-type-txt">PDF</div>

                    <div class="progress">
                        <a-progress :percent="100"></a-progress>
                    </div>

                    <img src="@/assets/progress-area/preview-btn.png" class="btn preview-btn"/>
                    <img src="@/assets/progress-area/dowload-btn.png" class="btn dowload-btn"/>

                    <div class="date">2024-01-30</div>

                </div>
                <!-- 失败订单 -->
                <div class="order-item order-item-fail">
                    <img src="@/assets/record/icon-mp3.png" class="icon-mp3">

                    <div class="item-name-area">
                        <div class="item-name">
                            <div class="item-name-name">义勇军进行曲.mid</div>
                            <div class="item-name-type">MP3</div>
                        </div>
                        <div class="order-num">订单号：20247484555</div>
                    </div>

                    <img src="@/assets/record/icon-mp3.png" alt="" class="result-type-icon">

                    <div class="result-type-txt">PDF</div>

                    <div class="progress">
                        <a-progress :percent="100"  status="exception"></a-progress>
                    </div>

                    <img src="@/assets/progress-area/preview-btn.png" class="btn preview-btn"/>
                    <img src="@/assets/progress-area/dowload-btn.png" class="btn dowload-btn"/>

                    <div class="date">2024-01-30</div>

                </div>

            </div>
        </div>

        <div class="bottom-area">
            <bottom-nav></bottom-nav>
        </div>

    </div>
</template>

<script>
import BottomNavComponent from '@/components/bottom-nav/bottom-nav.vue';
import { Progress } from 'ant-design-vue';

export default {
    name : 'RecordPage',
    components:{
        'bottom-nav' : BottomNavComponent ,
        'a-progress' : Progress
      },
}

</script>

<style scoped>
    .wrapper{
        width: 100%;
    }
    .top-area{
        min-height: 700px;
        padding-left: 360px;
    }
    .bg-shadow{
        position: absolute;
        right: -200px;
        top: -200px;
        width: 1645px;
        height: 716px;
    }
    .tips{
        margin-top: 147px;
        display: flex;
        align-items: center;
        font-size: 14px;
        color: rgba(92, 85, 73, 1);
    }
    .tips-icon{
        width: 18px;
        height: 18px;
        margin-right: 6px;
    }
    .order-list{
        margin-top: 23px;
        position: relative;
        z-index: 99;
    }
    .order-item{
        position: relative;
        width: 1287px;
        height: 123px;
        opacity: 1;
        border-radius: 12px;
        background: rgba(255, 255, 255, 1);
        border: 1px solid rgba(255, 255, 255, 1);
        box-shadow: 0px 8px 20px  rgba(207, 198, 182, 0.5);
        display: flex;
        align-items: center;
    }
    .order-item-fail{
        background: rgba(240, 240, 240, 1);
    }
    .order-item:not(:first-child){
        margin-top: 30px;
    }
    .icon-mp3{
        margin-left: 30px;
        width: 48px;
        height: 48px;
    }
    .item-name-area{
        margin-left: 13px;
    }
    .item-name{
        display: flex;
        align-items: center;
    }
    .item-name-name{
        font-size: 18px;
        font-weight: 700;
        color: rgba(74, 79, 56, 1);
    }
    .item-name-type{
        margin-left: 20px;
        width: 47px;
        height: 22px;
        border-radius: 8px;
        background: rgba(245, 223, 184, 1);
        font-size: 14px;
        font-weight: 700;
        line-height: 22px;
        text-align: center;
        color: #ffffff;
    }
    .order-num{
        margin-top: 8px;
        font-size: 14px;
        font-weight: 700;
        color: rgba(133, 128, 101, 1);
    }
    .result-type-icon{
        margin-left: 406px;
        width: 47px;
        height: 47px;
    }
    .result-type-txt{
        margin-left: 5px;
        font-size: 18px;
        color: rgba(133, 128, 101, 1);
    }
    .progress{
        margin-left: 19px;
        width: 234px;
    }

    .btn{
        display: block;
    }
    .preview-btn{
        margin-left: 22px;
        width: 68px;
        height: 27px;
    }
    .dowload-btn{
        width: 65px;
        height: 27px;
        margin-left: 29px;
    }
    .date{
        position: absolute;
        font-size: 12px;
        font-weight: 700;
        color: #000000;
        right: 46px;
        bottom: 19px;
    }
</style>