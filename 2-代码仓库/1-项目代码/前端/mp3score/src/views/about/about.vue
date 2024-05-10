
<template>
    <div class="wrapper">

        <div class="top-area">
            <img src="@/assets/about-us/yuan-1.png" alt="" class="abo yuan-1">
            <img src="@/assets/about-us/yuan-2.png" alt="" class="abo yuan-2">

            <div class="top-content-area">
                <img src="@/assets/about-us/whoRwe.png" class="whoRwe">

                <div class="describe-word">
                    欢迎来到我们的公司，我们是一家专注于音乐技术创新的团队。以激情和创意为驱动，我们致力于打造出色的音乐工具，让用户在创作和欣赏音乐时享受无与伦比的体验。
                    <br>
                    <br>
                    “为全球音乐爱好者提供前所未有的音乐之旅”
                </div>

                <div class="num-aea">
                    <div class="num-item-area" style="left:15px">
                        <div class="num-item-top">
                            <div class="num-item-num">500</div>
                            <div class="num-item-danwei">万</div>
                        </div>
                        <div class="num-item-name">目标客户</div>                            
                    </div>
                    <div class="shuxian"></div>
                    <div class="num-item-area">
                        <div class="num-item-top">
                            <div class="num-item-num">95%</div>
                        </div>
                        <div class="num-item-name">客户满意度</div>                            
                    </div>
                    <div class="shuxian"></div>
                    <div class="num-item-area" style="right:15px">
                        <div class="num-item-top">
                            <div class="num-item-num">10+</div>
                        </div>
                        <div class="num-item-name">解决痛点</div>                            
                    </div>
                </div>

            </div>
        </div>

        <div class="middle-area">
            <img src="@/assets/about-us/team-title.png" class="team-title">

            <div class="team-word">
                "我们是一支充满创意与激情的团队，致力于通过技术创新，<br>为用户提供音乐创作与享受的全新体验。"
            </div>

            <div class="team-people-title">团队成员</div>

            <div class="teams-wrap">
                <div class="team-item" v-for="item in people_list">
                    <div class="team-item-name">{{ item.position }}</div>
                    <img :src="item.avat_url" class="team-item-avg">
                    <div class="team-item-people-name">{{ item.name }}</div>
                    <div class="team-item-people-tag">{{ item.title }}</div>
                    <div class="team-item-people-desc">{{ item.desc }}</div>
                </div>
            </div>

            <div class="school-aea">
                <div class="school-area-title">研发支持</div>
                <div class="school-logo-area">
                    <img src="@/assets/about-us/logo-school-1.png" alt="" class="school-logo">
                    <img src="@/assets/about-us/logo-school-2.png" alt="" class="school-logo">
                </div>
                <div class="school-area-tag">长沙理工大学AI应用实验室</div>
            </div>
        </div>

        <div class="contact-us">
            <img src="@/assets/about-us/contact-title.png" class="contact-title">

            <div class="contact-map-area">
                <img src="@/assets/about-us/contact-map.png" class="map-pic">

                <div class="address-area">
                    <div>联系方式：15575936492</div>
                    <div>邮箱：569513303@qq.com</div>
                    <div>官网：</div>
                    <div>地址：湖南省长沙市长沙理工大学</div>
                </div>
            </div>

        </div>

        <div class="bottom-nav">
            <bottom-nav></bottom-nav>
        </div>



    </div>
</template>
<script>
    import BottomNavComponent from '@/components/bottom-nav/bottom-nav.vue';

    export default{
        name:'aboutPage',
        data(){
            return {
                people_list : [
                    { name : '豪妹' , position :'产品经理' , title : '三一集团项目经理' , avat_url : require('@/assets/about-us/avatar-1.jpg') , desc : '互联网产品创业经历、前端开发<br>掌握乐器：吉他、钢琴' },
                    { name : '毅哥' , position :'运营经理' , title : '中国电信高级运营总监' ,avat_url : require('@/assets/about-us/avatar-2.png') , desc : '大型项目负责人、10余年开发经验乐器：酒后，贼能吼，醉后，能主唱' },
                    { name : '老杨' , position :'市场经理' , title : '吉他世界网销量前10制谱师' ,avat_url : require('@/assets/about-us/avatar-3.jpg') , desc : '琴行老板、制谱师掌握乐器：吉他、贝斯' },
                    { name : '狒狒' , position :'音乐质量' , title : '哔哩哔哩游戏音乐制作' ,avat_url : require('@/assets/about-us/avatar-4.jpg') , desc : '武汉音乐学院毕业掌握乐器：吉他、贝斯、鼓' },
                    { name : '波波' , position :'算法开发' , title : '百度算法工程师' ,avat_url : require('@/assets/about-us/avatar-5.jpg') , desc : '百度APP客户端设计' },
                    { name : '嘎子' , position :'后端开发' , title : '三一集团后端工程师' ,avat_url : require('@/assets/about-us/avatar-6.jpg') , desc : '大型交付产品后端主管' },
                ]

            }
        },
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
        width: 1920px;
        height: 700px;
        background-image: url('@/assets/about-us/top-bg.png');
        background-size: 100% 100%;
        background-repeat: no-repeat;
        position: relative;
    }
    .abo{
        position: absolute;
    }
    .yuan-1{
        width: 71px;
        height: 71px;
        top: 431px;
        left: 290px;
    }
    .yuan-2{
        width: 101px;
        height: 101px;
        bottom: -64px;
        left: 948px;
    }
    .middle-area{
        width: 1920px;
        margin-top: 96px;
        background-image: url('@/assets/about-us/flash-bg.png');
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }
    .top-content-area{
       position: relative;
       top: 239px;
       left: 405px;
        
    }
    .whoRwe{
        width: 515px;
        height: 82px;
        display: block;
    }
    .describe-word{
        width: 390px;
        margin-top: 25px;
        font-size: 18px;
        font-weight: 400;
        line-height: 23.76px;
        color: rgba(194, 180, 159, 1);
    }
    .num-aea{
        margin-top: 84px;
        width: 626px;
        height: 105px;
        background-color: rgba(243, 214, 160, 0.9);
        box-shadow:inset 0px 0px 4px 2px rgba(255, 255, 255, 0.15), 0px 6px 15px  rgba(0, 0, 0, 0.25);
        display: flex;
        align-items: center;
        justify-content: space-around;
    }
    .num-item-area{
        color : rgba(255, 255, 255, 1);
        text-align: center;
        position: relative;
    }
    .num-item-num{
        font-size: 36px;
        font-weight: 700;
        display: inline;
    }
    .num-item-danwei{
        font-size: 14px;
        display: inline;
        font-weight: 300;

    }
    .num-item-name{
        font-size: 14px;
        font-weight: 300;
    }
    .shuxian{
        width: 2px;
        height: 37px;
        background-color: rgba(255, 241, 217, 1);
    }
    .middle-area{
        margin-top: 96px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .team-title{
        width: 224px;
        height: 79px;
    }
    .team-word{
        margin-top: 34px;
        width: 719px;
        font-size: 18px;
        line-height: 40px;
        color: rgba(133, 128, 101, 1);
        text-align: center;
    }
    .team-people-title{
        margin-top: 141px;
        font-size: 30px;
        font-weight: 700;
        line-height: 35.16px;
        color: rgba(74, 79, 56, 1);
    }
    .teams-wrap{
        margin-top: 39px;
        display: flex;
    }
    .team-item{
        width: 207px;
        height: 421px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 3px 5px  rgba(133, 117, 90, 0.1), 0px 10px 20px  rgba(204, 180, 139, 0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .team-item-name{
        margin-top: 29px;
        font-size: 20px;
        font-weight: 700;
        color: rgba(101, 94, 78, 1);
    }
    .team-item-avg{
        margin-top: 48px;
        width: 105px;
        height: 105px;
        border-radius: 50%;
    }
    .team-item-people-tag{
        margin-top: 12px;
        font-size: 18px;
        font-weight: 400;
        width: 180px;
        text-align: center;
    }
    .team-item-people-name{
        margin-top: 20px;
        font-size: 24px;
        font-weight: 400;;
        color: rgba(92, 85, 73, 1);
    }
    .team-item-people-desc{
        margin-top: 12px;
        width: 164px;
        font-size: 16px;
        font-weight: 300;
        color: rgba(101, 94, 78, 1);
    }
    .team-item:not(:first-child){
        margin-left: 20px;
    }
    .school-aea{
        margin-top: 120px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .school-area-title{
        font-size: 30px;
        font-weight: 700;
        color: rgba(74, 79, 56, 1);
    }
    .school-logo-area{
        margin-top: 28px;
    }
    .school-logo{
        width: 157px;
        height: 157px;
        margin-right: 70px;
    }
    .school-area-tag{
        margin-top: 40px;
        font-size: 18px;
        color: rgba(101, 94, 78, 1);
    }
    .contact-us{
        margin-top: 180px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .contact-title{
        width: 335px;
        height: 105px;
    }
    .contact-map-area{
        margin-top: 2px;
        width: 1920px;
        height: 575px;
        background-color: rgba(251, 249, 242, 1);
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .map-pic{
        width: 1440px;
        height: 575px;
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        z-index: 98;
    }
    .address-area{
        position: relative;
        display: block;
        margin-top: 287px;
        font-size: 18px;
        color: rgba(101, 94, 78, 1);
        z-index: 99;
        line-height: 40px;
        text-align: left;
    }
</style>