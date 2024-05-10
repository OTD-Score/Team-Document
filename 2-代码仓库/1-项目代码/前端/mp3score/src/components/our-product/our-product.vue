<template>
    <div class='wrapper'>
        
        <!-- <div class="mp3Midi"></div> -->
        <!-- MP3转MIDI -->
        <img src="@/assets/our-products/mp3-midi.png" class="mp3Midi">
        <!-- MP3转pdf -->
        <img src="@/assets/our-products/mp3-pdf.png" class="mp3Pdf">
        <!-- 创作从此更加畅快 -->
        <img src="@/assets/our-products/b-logo-bg.png" class="b-logo">
    </div>
</template>

<script>
export default{
    name:'our-product',
}
</script>

<style scoped>
    .wrapper{
        margin-top: 120px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .title{
        width:252px;
        height:79px;
    }
    .mp3Midi{
        width: 1920px;
        height: 890px;
        /* background-image: url('@/assets/our-products/mp3Midi.png'); */
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }
    .mp3Pdf{
        width: 1330;
        height: 940px;
    }
    .b-logo{
        width: 1360px;
        height: 480px;
    }
</style>