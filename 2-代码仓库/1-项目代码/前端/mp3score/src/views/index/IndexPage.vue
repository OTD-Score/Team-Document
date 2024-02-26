<template>
  <TopColumn/>
<div id="bigback1">
  <div id="functionPage">
    <div class="funcbackimage" id="backimage1"></div>
    <div id="func1">
      <div id="func1p1">将你的MP3、WMN音乐文件，转录为MIDI文件</div>
      <br>
      <div id="func1p2">
        <div id="func1p2d"><p id="func1p2text">试试吧</p></div>
        <div id="func1logo">
          <img id="jiantou" src="../../assets/IndexPage-jiantou.png" alt="">
        </div>
      </div>
    </div>
    <div id="func2">
      <div id="func2d1">
        <div id="func2d1p1">MP3转MIDI</div>
        <div id="func2d1p2">MP3转PDF谱</div>
        <div id="func2d1p3">伴奏分离</div>
        <div id="func2d1p4">AI音乐生成</div>
      </div>
      <div id="func2d2">
        <div id="func2d2logo"></div>
        <div id="func2d2p">请将您的音乐文件放在这里</div>
      </div>
      <div id="func2d3">
        <div id="func2d3p1">
          <div id="func2d3p1logo"></div>
          <div id="func2d3p1text">纯钢琴</div>
        </div>
        <div id="func2d3p2">
          <div id="func2d3p2logo"></div>
          <div id="func2d3p2text">多轨道</div>
        </div>
      </div>
    </div>
  </div>
  <div id="body1">
    <div id="body1d2">Our Product</div>
    <div id="body1d1">我们的产品</div>
    <div id="body1d3">
      <div id="body1d3p1">MP3转MIDI</div>
      <div id="body1d3p2">创作如临仙境，将任何旋律化为数字语言，用AI的魔法将你的灵感编织成无限可能！ </div>
    </div>
    <div id="body1d4logo1">
      <img src="../../assets/IndexPage-MusicLogo1.png" alt="">
    </div>
    <div id="body1d4logo2">
      <img src="../../assets/IndexPage-MusicLogo2.png" alt="">
    </div>
    <div id="body1d4logo3">
      <img src="../../assets/IndexPage-MusicLogo3.png" alt="">
    </div>
    <div id="body1d4logo4">
      <img src="../../assets/IndexPage-MusicLogo4.png" alt="">
    </div>
    <div id="body1d4logo5">
      <img src="../../assets/IndexPage-MusicLogo5.png" alt="">
    </div>
    <div id="body1d4logo6">
      <img src="../../assets/IndexPage-MusicLogo6.png" alt="">
    </div>
    <div id="body1d4logo7">
      <img src="../../assets/IndexPage-MusicLogo7.png" alt="">
    </div>
    <div id="body1d5logo2">
      <img src="../../assets/IndexPage-Body1BackImage.png" alt="">
    </div>
    <div id="body1d5logo1">
      <img src="../../assets/IndexPage-Body1BackImage.png" alt="">
    </div>
  </div>
</div>
  <div id="body2" class="body2back">
    <div id="body2p">
      <div id="body2p1">MP3转PDF谱</div>
      <div id="body2p2">音符跃然纸上，创意在五线谱中蔓延。将你最喜欢的歌曲转换为乐谱，
        为你的音乐创作增添更多可能性。只需几步简单操作，即可将MP3的音轨精准地转录成乐谱，
        让你在创作过程中更加游刃有余。
      </div>
    </div>
    <div id="body2photo1">
        <img class="body2image1" src="../../assets/IndexPage-yinpin.png" alt="">
    </div>
    <div id="body2photo2">
      <img class="body2image1" src="../../assets/IndexPage-yinpin.png" alt="">
    </div>
    <div id="body2photo3">
      <img class="body2image1" src="../../assets/IndexPage-yinpin.png" alt="">
    </div>
    <div id="body2photo4">
      <img src="../../assets/IndexPage-jiantou2.png" alt="">
    </div>
    <div id="body2photo5">
      <img src="../../assets/IndexPage-jiantou2.png" alt="">
    </div>
    <div id="body2photo6">
      <img src="../../assets/IndexPage-jiantou2.png" alt="">
    </div>
    <div id="body2photo7">
      <img src="../../assets/IndexPage-Body2Image2.png" alt="">
    </div>
    <div id="body2photo8">
      <img src="../../assets/IndexPage-Body2Image3.jpg" alt="">
    </div>
    <div id="body2photo9">
      <img src="../../assets/IndexPage-Body2Image4.png" alt="">
    </div>
    <div id="body2footer">
      <div id="body2footerp">
        <div id="body2footerp1"> 与麦片谱一起，开启音乐创作的新纪元。</div>
        <div id="body2footerp2"> 创作，从此更加畅快淋漓！</div>
      </div>
    </div>
    <div id="body2footerback" class="body2footerback"></div>
  </div>
  <br>
  <br>
  <br>
  <BottomColumn/>
</template>

<script>
import BottomColumn from '@/components/BottomColumn.vue';
import TopColumn from '@/components/TopColumn.vue';
export default {
    name:'Index-Page',
    components:{
      BottomColumn,TopColumn
    }
}
</script>

<style lang="css" scoped>
  #bigback1{
    background-image: url(../../assets/IndexPage-juxing1.png);
    background-size: 80% 80%;
    background-repeat: no-repeat;
    background-position: 0% 100%; 
    bottom: 0;
    left:0;
  }
  #functionPage{
    left: 4px;
    top: 0px;
    width: 100%;
    height: 1220px;
    opacity: 1;
     /* background: linear-gradient(180deg, rgb(255, 255, 255) 16%, rgba(255, 251, 240, 0.59) 30.23%, rgba(255, 251, 240, 1) 100%);  */
    /* background-color: rgba(255, 251, 240, 1); */
    position: relative;
    overflow: hidden;
  }
  .funcbackimage{
    width:100%;
    height: 1220px;
    overflow: hidden;
    /* display: flex; */
  }
  #backimage1{
    background-image: url(../../assets/IndexPage-FunctionPageBackImage.png);
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: 0 0; 
    max-height: 100%;
    max-width: 100%;
  }
  #func1{
  opacity: 1;
  left: 10%;
  top: 30%;
  width: 444px;
  height: 305px;
  opacity: 1;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  position:absolute;
  display: flex;
  }
  #func1p1{
    font-size: 55px;
    font-weight: 700;
    letter-spacing: 0px;
    line-height: 64.46px;
    color: rgba(101, 94, 78, 1);
    text-align: left;
    vertical-align: middle;    
  }
  #func1p2{
    left: 5px;
    top: 14.5px;
    width: 285px;
    height: 81px;
    display: flex;
    flex-direction: row;
    
  }
  #func1p2d{
    left: 5px;
    top: 14.5px;
    width: 204px;
    height: 81px;
    opacity: 1;
    background: rgba(243, 214, 160, 1);
    display: flex;
    flex-direction:column;
    justify-content:center;
  }
  #func1p2text{
    font-size: 40px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 46.88px;
    color: rgba(255, 255, 255, 1);
    text-align: center;
  }
  #func1logo{
    left: 209px;
    top: 14.5px;
    width: 81px;
    height: 81px;
    opacity: 1;
    background: rgba(255, 241, 217, 1);
    overflow: hidden;
    text-align: center;
    
  }
  #jiantou{
    vertical-align:middle;
    padding-top: 15px;
  }
  #func2{
    left: 45%;
    top: 28%;
    width: 805px;
    height: 479px;
    opacity: 1;
    position:absolute;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.35);
    box-shadow:inset 0px 0px 4px 2px rgba(255, 255, 255, 0.15), 0px 6px 15px  rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(10px)    
  }
  #func2d1{
    left: 0px;
    top: 0px;
    width: 805px;
    height: 94px;
    opacity: 1;    
  }
  #func2d1p1{
    left: 4%;
    top: 18px;
    width: 150px;
    height: 24px;
    opacity: 1;
    position: absolute;
    border-radius: 4px;
    background: rgba(245, 223, 184, 1);
    box-shadow:inset 0px -2px 1px  rgba(0, 0, 0, 0.25);
    font-size: 23px;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 9px 9px 9px 29px;
  }
  #func2d1p2{
    left: 33%;
    top: 25px;
    width: 150px;
    height: 24px;
    opacity: 1;
    font-size: 23px;
    position: absolute;
  }
  #func2d1p3{
    left: 60%;
    top: 25px;
    width: 150px;
    height: 24px;
    opacity: 1;
    font-size: 23px;
    position: absolute;
  }
  #func2d1p4{
    left: 81%;
    top: 25px;
    width: 150px;
    height: 24px;
    opacity: 1;
    font-size: 23px;
    position: absolute;
  }
  #func2d2{
    left: 4%;
    top: 18%;
    width: 741px;
    height: 325px;
    opacity: 1;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0);
    border: 1px dashed rgba(176, 164, 141, 1);
    position: absolute;
  }
  #func2d2logo{
    left: 45%;
    top: 15%;
    width: 104.22px;
    height: 95.06px;
    opacity: 1;
    background-image: url(../../assets/IndexPage-funcMusicLogo.png);
    background-size: contain;
    background-repeat: no-repeat;
    background-position: 0 0; 
    position: relative;
  }
  #func2d2p{
    left: 18%;
    top: 60%;
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    letter-spacing: 0px;
    line-height: 39.59px;
    color: rgba(133, 128, 101, 1);
    vertical-align: middle; 
    position: absolute;
  }
  #func2d3{
    left: 5%;
    top: 90%;
    width: 605px;
    height: 54px;
    opacity: 1; 
    position: absolute;
    display: flex;
    flex-direction: row;
  }
  #func2d3p1logo{
    left: 0;
    height: 20px;
    width: 20px;
    background-image: url(../../assets/IndexPage-funcbutton1.png);
    background-size: contain;
    background-repeat: no-repeat;
    background-position: 0 0; 
    position: absolute;
  }
  #func2d3p1text{
    left: 25px;
    height: 20px;
    width: 70px;
    font-size: 18px;
    position: absolute;
  }
  #func2d3p2logo{
    left: 100px;
    height: 20px;
    width: 20px;
    background-image: url(../../assets/IndexPage-funcbutton2.png);
    background-size: contain;
    background-repeat: no-repeat;
    background-position: 0 0; 
    position: absolute;
  }
  #func2d3p2text{
    left: 125px;
    height: 20px;
    width: 70px;
    font-size: 18px;
    position: absolute;
  }
  #body1{
    left: 4px;
    top: 0px;
    width: 100%;
    height: 792.09px;
    opacity: 1;
    position: relative;
    overflow: hidden
  }
  #body1d1{
    top:0%;
    left: 38%;
    font-size: 75px;
    font-weight: 700;
    letter-spacing: 0px;
    line-height: 64.46px;
    color: rgba(101, 94, 78, 1);
    text-align: center;
    vertical-align: middle;
    position: absolute;
  }
  #body1d2{
    top:4%;
    left:37%;
    font-size: 90px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 90px;
    color: rgba(243, 214, 160, 0.34);
    text-align: center;
    vertical-align: middle;
    position: absolute;
  }
  #body1d3{
    left: 10%;
    top: 25%;
    width: 346px;
    height: 232px;
    opacity: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    position: absolute;
  }
  #body1d3p1{
    left: 0px;
    top: 0px;
    width: 346px;
    height: 90px;
    opacity: 1;
    display: flex;
    font-size: 58px;
    font-weight: 700;
    letter-spacing: 0px;
    line-height: 56.26px;
    color: rgba(74, 79, 56, 1);
    text-align: left;
    vertical-align: middle;
  }
  #body1d3p2{
    left: 0px;
    top: 112px;
    width: 544px;
    height: 140px;
    opacity: 1;
    display: flex;
    font-size: 35px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 40px;
    color: rgba(133, 128, 101, 1);
    text-align: left;
    vertical-align: middle;
  }
  #body1d4logo1{
    left: 10%;
    top: 54%;
    width: 77px;
    height: 77px;
    opacity: 1;
    position:absolute;
    display: flex;
  }
  #body1d4logo2{
    left: 16%;
    top: 54%;
    width: 77px;
    height: 77px;
    opacity: 1;
    position:absolute;
    display: flex;
  }
  #body1d4logo3{
    left: 22%;
    top: 54%;
    width: 77px;
    height: 77px;
    opacity: 1;
    position:absolute;
    display: flex;
  }
  #body1d4logo4{
    left: 10%;
    top: 66%;
    width: 77px;
    height: 77px;
    opacity: 1;
    position:absolute;
    display: flex;
  }
  #body1d4logo5{
    left: 16%;
    top: 66%;
    width: 77px;
    height: 77px;
    opacity: 1;
    position:absolute;
    display: flex;
  }
  #body1d4logo6{
    left: 22%;
    top: 66%;
    width: 77px;
    height: 77px;
    opacity: 1;
    position:absolute;
    display: flex;
  }
  #body1d4logo7{
    left: 28%;
    top: 66%;
    width: 77px;
    height: 77px;
    opacity: 1;
    position:absolute;
    display: flex;
  }
  #body1d5logo1{
    left: 45%;
    top: 15%;
    width: 823.95px;
    height: 419.12px;
    opacity: 1;
    position: absolute;
    transform:skewx(10deg) scale(0.95);
  }
  #body1d5logo2{
    left: 43%;
    top: 18%;
    width: 823.95px;
    height: 419.12px;
    opacity: 1;
    position: absolute;
    background: linear-gradient(250.44deg, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0) 100%);
    filter: blur(5px);
    transform:skewx(10deg) scale(0.95);
  }
  #body2{
    left: 4px;
    top: 0px;
    width: 100%;
    height: 1728px;
    opacity: 1;
    /* background: rgba(255, 251, 240, 1); */
    position: relative;
    background-image: url(../../assets/IndexPage-Body2BackImage1.png);
    background-size: 56%;
    background-repeat: no-repeat;
    background-position: 0 0;
    display: flex;
  }
  #body2p{
    left: 4px;
    top: 0px;
    width: 100%;
    height: 150px;
    opacity: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 0px 0px 10px 0px;
  }
  #body2p1{
    text-align: center;
    width: 350px;
    height: 70px;
    opacity: 1;
    display: flex;
    font-size: 48px;
    font-weight: 700;
    letter-spacing: 0px;
    line-height: 56.26px;
    color: rgba(74, 79, 56, 1);
  }
  #body2p2{
    text-align: center;
    width: 1070px;
    height: 85px;
    opacity: 1;
    display: flex;
    font-size: 24px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 40px;
    color: rgba(133, 128, 101, 1);
  }
  #body2photo{
    display: flex;
    justify-content: center;
    align-items: center; 
  }
  #body2photo1{
    left: 12%;
    top: 14%;
    width: 400.33px;
    height: 216.32px;
    opacity: 1;
    border-radius: 8px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 3px 5px  rgba(133, 117, 90, 0.1), 0px 10px 20px  rgba(204, 180, 139, 0.1);
    position: absolute;
    text-align: center;
    display: flex;
    flex-direction:column;
    justify-content:center;
  }
  .body2image1{
    transform: scale(0.8);
  }
  #body2photo2{
    left: 39%;
    top: 14%;
    width: 400.33px;
    height: 216.32px;
    opacity: 1;
    border-radius: 8px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 3px 5px  rgba(133, 117, 90, 0.1), 0px 10px 20px  rgba(204, 180, 139, 0.1);
    position: absolute;
    text-align: center;
    display: flex;
    flex-direction:column;
    justify-content:center;
  }
  #body2photo3{
    left: 67%;
    top: 14%;
    width: 400.33px;
    height: 216.32px;
    opacity: 1;
    border-radius: 8px;
    background: rgba(255, 255, 255, 1);
    box-shadow: 0px 3px 5px  rgba(133, 117, 90, 0.1), 0px 10px 20px  rgba(204, 180, 139, 0.1);
    position: absolute;
    text-align: center;
    display: flex;
    flex-direction:column;
    justify-content:center;
  }
  #body2photo4{
    left: 21%;
    top: 31%;
    width: 56.33px;
    height: 76.32px;
    opacity: 1;
    border-radius: 8px;
    box-shadow: 0px 3px 5px  rgba(133, 117, 90, 0.1), 0px 10px 20px  rgba(204, 180, 139, 0.1);
    position: absolute;
    text-align: center;
    display: flex;
    flex-direction:column;
    justify-content:center;
  }
  #body2photo5{
    left: 48%;
    top: 31%;
    width: 56.33px;
    height: 76.32px;
    opacity: 1;
    border-radius: 8px;
    box-shadow: 0px 3px 5px  rgba(133, 117, 90, 0.1), 0px 10px 20px  rgba(204, 180, 139, 0.1);
    position: absolute;
    text-align: center;
    display: flex;
    flex-direction:column;
    justify-content:center;
  }
  #body2photo6{
    left: 76%;
    top: 31%;
    width: 56.33px;
    height: 76.32px;
    opacity: 1;
    border-radius: 8px;
    box-shadow: 0px 3px 5px  rgba(133, 117, 90, 0.1), 0px 10px 20px  rgba(204, 180, 139, 0.1);
    position: absolute;
    text-align: center;
    display: flex;
    flex-direction:column;
    justify-content:center;
  }
  #body2photo7{
    left: 11%;
    top: 40%;
    width: 430px;
    height: 600px;
    opacity: 1;
    border-radius: 8px;
    background-color: aqua;
    box-shadow: 0px 3px 5px  rgba(133, 117, 90, 0.1), 0px 10px 20px  rgba(204, 180, 139, 0.1);
    position: absolute;
    text-align: center;
    display: flex;
    flex-direction:column;
    justify-content:center;
    overflow: hidden;
  }
  #body2photo8{
    left: 39%;
    top: 40%;
    width: 430px;
    height: 600px;
    opacity: 1;
    border-radius: 8px;
    box-shadow: 0px 3px 5px  rgba(133, 117, 90, 0.1), 0px 10px 20px  rgba(204, 180, 139, 0.1);
    position: absolute;
    text-align: center;
    display: flex;
    flex-direction:column;
    justify-content:center;
    overflow: hidden;
  }
  #body2photo9{
    left: 67%;
    top: 40%;
    width: 430px;
    height: 600px;
    opacity: 1;
    border-radius: 8px;
    box-shadow: 0px 3px 5px  rgba(133, 117, 90, 0.1), 0px 10px 20px  rgba(204, 180, 139, 0.1);
    position: absolute;
    text-align: center;
    display: flex;
    flex-direction:column;
    justify-content:center;
    overflow: hidden;
  }
  #body2footer{
    left:8%;
    top: 82%;
    width: 1620px;
    height: 328px;
    opacity: 1;
    border-radius: 12px;
    position: absolute;
    background: linear-gradient(243.67deg, rgba(222, 242, 250, 1) 0%, rgba(255, 248, 236, 1) 100%);
    box-shadow: 0px 100px 80px  rgba(255, 162, 0, 0.02), 0px 60px 40px  rgba(0, 0, 0, 0.02), 0px 40px 20px  rgba(0, 0, 0, 0.01), 0px 26px 17px  rgba(0, 0, 0, 0.01), 0px 10px 8px  rgba(0, 0, 0, 0.01), 0px 2px 4px  rgba(0, 0, 0, 0);
  }
  #body2footerp{
    left: 93px;
    top: 76px;
    width: 822.23px;
    height: 146.09px;
    opacity: 1;
    position: relative;  
  }
  #body2footerp1{
    font-size: 30px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 50px;
    color: rgba(101, 94, 78, 1);
  }
  #body2footerp2{
    font-size: 60px;
    font-weight: 700;
    letter-spacing: 0px;
    line-height: NaNpx;
    color: rgba(101, 94, 78, 1);
    text-align: left;
    vertical-align: middle;
  }
  #body2footerback{
    position: absolute;
    overflow: hidden;
    width: 70%;
    height: 70%;
    display: flex;
  }
  .body2footerback{
    background-image: url(../../assets/IndexPage-Body2BackImage2.png);
    background-size: contain;
    background-repeat: no-repeat;
    background-position: 85% 100%; 
    bottom:0;
    right:0;
  }
  </style>


  