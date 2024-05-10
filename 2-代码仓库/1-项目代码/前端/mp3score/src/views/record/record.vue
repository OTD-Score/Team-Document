<template>
    <div class="wrapper">
        <div class="top-area">
            <img src="@/assets/record/bg-shadow.png" class="bg-shadow">
            
            <div class="tips">
                <img src="@/assets/record/tips.png" class="tips-icon">
                <div>温馨提示：文件转换过程预计需要1~3分钟，微信小程序登录的用户转换完成后会以微信消息进行通知~</div>
            </div>

            <div class="order-list">

                <div class="order-item">
                    <img src="" alt="" class="item-type">

                    <div class="item-name-area">
                        <div class="item-name">
                            <div class="item-name-name">义勇军进行曲.mid</div>
                            <div class="item-name-type">MP3</div>
                        </div>
                        <div class="order-num">订单号：20247484555</div>
                    </div>

                    <img src="" alt="" class="result-type">

                    <div class="progress">
                        <div class="progress-bar"></div>
                        <div class="progress-num">50%</div>
                    </div>
                    


                </div>
                <div class="order-item">


                </div>
                <div class="order-item">


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

export default {
    name : 'RecordPage',
    components:{
        'bottom-nav' : BottomNavComponent ,
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
        width: 1287px;
        height: 123px;
        opacity: 1;
        border-radius: 12px;
        background: rgba(255, 255, 255, 1);
        border: 1px solid rgba(255, 255, 255, 1);
        box-shadow: 0px 8px 20px  rgba(207, 198, 182, 0.5);
    }
    .order-item:not(:first-child){
        margin-top: 30px;
    }
</style>