<template>
    <div class='wrapper'>
        <div class="main-area">
            <!-- 列表头 -->
            <div class="progress-area">
                <div class="left-wrap">
                    <div class="progress-lab">
                        <img src="@/assets/progress-area/progress-icon.png" class="progress-icon">
                        <p class="progress-num">29%</p>
                    </div>
                    <div class="file-size">
                        <div>任务进行中</div>
                        <div>8.3M</div>
                    </div>
                </div>
                <div class="files-btn">
                    全部记录
                </div>
            </div>
            <!-- 列表框 -->
            <div class="result-list">
                <!-- 列表项 -->
                <div class="result-item">
                    <div class="result-left-wrap">
                        <img src="@/assets/progress-area/icon-midi.png" class="file-icon">
                        <div class="file-name">夏天的风-温岚.mid</div>
                    </div>

                    <div class="result-right-wrap">
                        <img src="@/assets/progress-area/preview-btn.png" class="btn preview-btn"/>
                        <img src="@/assets/progress-area/dowload-btn.png" class="btn dowload-btn"/>
                    </div>
                </div>
                <!-- 列表项 -->
                <div class="result-item">
                    <div class="result-left-wrap">
                        <img src="@/assets/progress-area/icon-midi.png" class="file-icon">
                        <div class="file-name">菊次郎的夏天-piano.mid</div>
                    </div>

                    <div class="result-right-wrap">
                        <img src="@/assets/progress-area/preview-btn.png" class="btn preview-btn"/>
                        <img src="@/assets/progress-area/dowload-btn.png" class="btn dowload-btn"/>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
export default{
    name:'processArea',
}
</script>

<style scoped>
    .wrapper{
        display: flex;
        justify-content: center;
    }
    .main-area{
        width: 1202px;
        min-height: 252px;
        box-shadow: 0px 10px 12px  rgba(0, 0, 0, 0.25);
        border-radius: 8px;
        position: relative;
        top:-16px;
        z-index: 100;
    }
    .progress-area{
        width: 100%;
        height: 120px;
        background: rgba(79, 66, 56, 1);
        border-radius: 8px 8px 0 0 ;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .progress-lab{
        display: flex;
        width: 207.14px;
        height: 83.13px;
        border-radius: 8px;
        background: rgba(101, 94, 78, 1);
        box-shadow:inset 0px -3px 2px  rgba(0, 0, 0, 0.25);
        align-items: center;
        margin-left: 30px;
        justify-content: center;
    }
    .progress-icon{
        width: 54px;
        height: 54px;
    }
    .progress-num{
        font-size: 39px;
        margin-left: 13px;
        color: #ffffff;
    }
    .file-size{
        margin-left: 18px;
        font-size: 24px;
        color: #ffffff;
        line-height: 36px;
        text-align: center;
    }
    .left-wrap{
        display: flex;
        align-items: center;
    }
    .files-btn{
        width: 176.04px;
        height: 83.13px;
        border-radius: 8px;
        background: rgba(213, 181, 134, 1);
        box-shadow:inset 0px -3px 2px  rgba(0, 0, 0, 0.25);
        margin-right: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        color: #ffffff;
    }
    .result-list{
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 23px 0 38px;
        box-sizing: content-box;
    }
    .result-item{
        margin-bottom: 25px;
        width: 1127px;
        height: 104.64px;
        border-radius: 12px;
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 10px 20px  rgba(0, 0, 0, 0.25);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .result-left-wrap{
        display: flex;
        margin-left: 24px;
        align-items: center;
    }
    .file-icon{
        width: 54.77px;
        height: 54.77px;
    }
    .file-name{
        margin-left: 11px;
        font-size: 20px;
        color: rgba(74, 79, 56, 1);
        font-weight: 700;
    }
    .result-right-wrap{
        display: flex;
        align-items: center;
        margin-right: 47px;
    }
    .btn{
        display: block;
    }
    .preview-btn{
        width: 80px;
        height: 32px;
    }
    .dowload-btn{
        width: 75px;
        height: 32px;
        margin-left: 15px;
    }
</style>