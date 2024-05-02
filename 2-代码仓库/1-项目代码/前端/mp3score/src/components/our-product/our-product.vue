<template>
    <div class='wrapper'>
        <img src="@/assets/our-products/title.png" class="title">
        <div class="mp3Midi"></div>
        <img src="" class="mp3Midi">
        <img src="@/assets/our-products/mp3Pdf.png" class="mp3Pdf">
    </div>
</template>

<script>
export default{
    name:'our-product',
}
</script>

<style scoped>
    .wrapper{
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
        background-image: url('@/assets/our-products/mp3Midi.png');
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }
    .mp3Pdf{
        width: 1330;
        height: 940px;
    }
</style>