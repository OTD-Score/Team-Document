<template>
    <div id="footer1">
      <div id="footer1d1">
        <div id="footer1p1">常见问题</div>
        <div id="footer1p2">我们的产品</div>
        <div id="footer1p3">它是如何工作的</div>
        <div id="footer1p4">关于我们</div>
      </div>
      <ul id="footer1d2">
        <li id="footer1d2p1">常见问题</li>
        <li id="footer1d2p2">什么是MIDI文件？</li>
        <li id="footer1d2p3">MIDI文件和MP3等大部分音频文件有什么区别？</li>
        <li id="footer1d2p4">如何使用MP3转MIDI功能？</li>
        <li id="footer1d2p5">支持哪些文件格式？</li>
      </ul>
    </div>
    <div id="footer2">
      <div id="footer2d1">
        <div id="footer2d1p1">功能地图</div>
        <div id="footer2d1p2">MP3转MIDI文件</div>
        <div id="footer2d1p3">MP3转PDF谱</div>
        <div id="footer2d1p4">伴奏分离</div>
        <div id="footer2d1p5">AI音乐合成</div>
        <div id="footer2d1p6">转录记录</div>
      </div>
      <div id="footer2d2">
        <div id="footer2d2p1">规则条款</div>
        <div id="footer2d2p2">服务条款</div>
        <div id="footer2d2p3">隐私政策</div>
        <div id="footer2d2p4">关于我们</div>
      </div>
      <div id="footer2d3">
        <div id="footer2d3p1">联系我们</div>
        <div id="footer2d3p2">联系方式：xxxxxxxx</div>
        <div id="footer2d3p3">邮箱：xxxxxxxx@qq.com</div>
        <div id="footer2d3p4">官网：www.xxxxxxxx</div>
        <div id="footer2d3p5">地址：湖南省长沙理工大学</div>
      </div>
      <div id="footer2d4">
        <div id="footer2d4p">关注我们</div>
      </div>
      <div id="footer2d5">
        <div id="footer2d5logo1">
          <img src="@/assets/IndexPage-guanzhuwomen.png" alt="">
        </div>
      </div>
    </div>
    <hr>
    <div id="footer3">
      <div id="footer3p">备案号</div>
    </div>
  </template>
  
  <script>
  export default {
     name:'bottom-nav'
  }
  </script>
  
  <style lang="css" scoped>
  #footer1{
      left: 4px;
      top: 0px;
      width: 100%;
      height: 600px;
      opacity: 1;
      /* background: linear-gradient(180deg, rgba(255, 251, 240, 0.77) 0%, rgba(245, 223, 184, 1) 100%); */
      position: relative;
      display: flex;
      background-image: url(@/assets/IndexPage-footer1backgroundphoto.png);
      background-size: cover;
      background-repeat: no-repeat;
      background-position: 0 0;   
  }
  #footer1d1{
      left: 15%;
      top: 35%;
      width: 396.87px;
      height: 300px;
      position:absolute;
    }
    #footer1p1{
      left: 0%;
      top: 0%;
      width: 507.7px;
      height: 50.82px;
      opacity: 1;
      border-radius: 8px;
      background: linear-gradient(180deg, rgba(240, 255, 242, 1) 66.67%, rgba(171, 196, 170, 1) 100%);
      backdrop-filter: blur(100px);
      position: absolute;
      display: flex;
      flex-direction:column;
      justify-content:center;
      font-size: 22px;
      font-weight: 400;
      letter-spacing: 0px;
      line-height: 0px;
      color: rgba(101, 94, 78, 1);
      text-align: left;
      vertical-align: top;
    }
    #footer1p2,#footer1p3,#footer1p4{
      width: 507.7px;
      height: 50.82px;
      opacity: 1;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.25);
      box-shadow:inset 0px 4px 4px 2px rgba(255, 255, 255, 0.15);
      display: flex;
      flex-direction:column;
      justify-content:center;
      font-size: 22px;
      font-weight: 400;
      letter-spacing: 0px;
      line-height: 0px;
      color: rgba(101, 94, 78, 1);
      text-align: left;
      vertical-align: top;
    }
    #footer1p2{
      left: 0;
      top: 22%;
      position: absolute;
    }
    #footer1p3{
      left: 0;
      top: 44%;
      position: absolute;
    }
    #footer1p4{
      left:0;
      top: 66%;
      position: absolute;
    }
    #footer1d2{
      left: 50%;
      top: 35%;
      width: 396.87px;
      height: 300px;
      position:absolute;
    }
    #footer1d2p1{
      left: 0;
      top: 0;
      width: 654px;
      height: 30px;
      opacity: 1;
      background: rgba(245, 245, 237, 0);
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      padding: 0px 7px 0px 7px;
      font-size: 26px;
      font-weight: 700;
      letter-spacing: 0px;
      line-height: 0px;
      color: rgba(74, 79, 56, 1);
      text-align: left;
      position: absolute;
    }
    #footer1d2p2,#footer1d2p3,#footer1d2p4,#footer1d2p5{
      width: 572px;
      height: 30px;
      opacity: 1;
      display: flex;
      justify-content: flex-start;
      align-items: center;
      font-size: 22px;
      font-weight: 400;
      letter-spacing: 0px;
      line-height: 0px;
      color: rgba(69, 64, 54, 1);
      text-align: left;
    }
    #footer1d2p2{
      left: 10%;
      top: 10%;
      position: absolute;
    }
    #footer1d2p3{
      left: 10%;
      top: 25%;
      position: absolute;
    }
    #footer1d2p4{
      left: 10%;
      top: 40%;
      position: absolute;
    }
    #footer1d2p5{
      left: 10%;
      top: 55%;
      position: absolute;
    }
    #footer2{
      left: 4px;
      top: 0px;
      width: 100%;
      height: 450px;
      opacity: 1;
      background: rgba(67, 70, 79, 1);
      position: relative;
      display: flex;
    }
    #footer2d1{
      left: 15%;
      top: 15%;
      width: 150px;
      height: 240px;
      position: absolute;    
    }
    #footer2d1p1,#footer2d2p1,#footer2d3p1,#footer2d4p{
      font-size: 23px;
      font-weight: 400;
      letter-spacing: 0px;
      line-height: 40px;
      margin-bottom: 10px;
      color: rgba(255, 255, 255, 1);    
    }
    #footer2d1p2,#footer2d1p3,#footer2d1p4,#footer2d1p5,#footer2d1p6,#footer2d2p2,#footer2d2p3,#footer2d2p4,#footer2d3p2,
    #footer2d3p3,#footer2d3p4,#footer2d3p5{
      font-size: 18px;
      font-weight: 400;
      letter-spacing: 0px;    
      line-height: 40px;
      color: rgba(181, 186, 182, 1);
      text-align: left;
      vertical-align: top; 
    }
    #footer2d2{
      left: 35%;
      top: 15%;
      width: 110px;
      height: 240px;
      position: absolute;
    }
    #footer2d3{
      left: 53%;
      top: 15%;
      width: 170px;
      height: 240px;
      position: absolute;
    }
    #footer2d4{
      left: 74%;
      top: 15%;
      width: 100px;
      height: 240px;
      position: absolute;
    }
    #footer2d5{
      left: 73%;
      top: 26%;
      width: 100px;
      height: 240px;
      position: absolute;
      display: flex;
    }
    #footer3{
      left: 4px;
      top: 0px;
      width: 100%;
      height: 100px;
      opacity: 1;
      background: rgba(67, 70, 79, 1);
      position: relative;
    }
    #footer3p{
      text-align: center;
      vertical-align: top;
      font-size: 18px;
      font-weight: 400;
      letter-spacing: 0px;
      line-height: 40px;
      color: rgba(255, 255, 255, 1);
      vertical-align: top;       
    }
    hr{
      padding: 0;
      margin: 0;
    }
  </style>