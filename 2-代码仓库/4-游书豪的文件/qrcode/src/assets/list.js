/* eslint-disable */

function getFileList(type = '21M',id){
    //type = '21M' "51M" "65M" "CYC" "ZJC" "LYC" "SYC" "ZZXC"
    if(type==='21M'){
        return M21
    }
    if(type==='51M'){
        return M51
    }
    if(type==='65M'){
        return M65
    }
    if(type==='CYC'){
        return CYC
    }
    if(type==='ZJC'){
        return ZJC
    }
    if(type==='LYC'){
        return LYC
    }
    if(type==='SYC'){
        return SYC
    }
    if(type==='ZZXC'){
        return ZZXC
    }
}

let base_url = 'https://yingji.irootech.com/upload';

let M21 = [
    {
        name:'4桥21米消防车液压系统原理图（外发版）.pdf',
        type:'pdf',
        size: '197KB',
        url: base_url + '/1-三桶油21米/'
    },
    {
        name:'20T消防车电气原理图.pdf',
        type:'pdf',
        size: '903KB',
        url: base_url + '/1-三桶油21米/'
    },
    {
        name:'JP21气路原理图-Model.pdf',
        type:'pdf',
        size: '63KB',
        url: base_url + '/1-三桶油21米/'
    },
    {
        name:'JP21水路原理图(借用JP26).pdf',
        type:'pdf',
        size: '179KB',
        url: base_url + '/1-三桶油21米/'
    },
    {
        name:'升级款21米举高喷射消防车车型基本信息.docx',
        type:'word',
        size: '903KB',
        url: base_url + '/1-三桶油21米/'
    }
]

let M51 = [
    {
        name:'JP51电气原理图.pdf',
        type:'pdf',
        size: '2.6M',
        url: base_url + '/2-三桶油51米/'
    },
    {
        name:'JP51水路原理图.pdf',
        type:'pdf',
        size: '76KB',
        url: base_url + '/2-三桶油51米/'
    },
    {
        name:'JP51液压原理图.pdf',
        type:'pdf',
        size: '240KB',
        url: base_url + '/2-三桶油51米/'
    },
    {
        name:'JP51气路原理图.pdf',
        type:'pdf',
        size: '198KB',
        url: base_url + '/2-三桶油51米/'
    },
    {
        name:'三一重工51米举高喷射消防车技术规格书-202404（JP51+沃尔沃FM540+万升泵+5t载液).docx',
        type:'word',
        size: '544KB',
        url: base_url + '/2-三桶油51米/'
    },
]

let M65 = [
    {
        name:'65米液压原理图-Model.pdf',
        type:'pdf',
        size: '419KB',
        url: base_url + '/3-三桶油65米/'
    },
    {
        name:'XJPV65电气原理图new-Model.pdf',
        type:'pdf',
        size: '517KB',
        url: base_url + '/3-三桶油65米/'
    },
    {
        name:'气路原理图.pdf',
        type:'pdf',
        size: '198KB',
        url: base_url + '/3-三桶油65米/'
    },
    {
        name:'升级款65米举高喷射消防车车型基本信息.doc',
        type:'word',
        size: '1.3M',
        url: base_url + '/3-三桶油65米/'
    },
    {
        name:'水路原理图-Model.pdf',
        type:'pdf',
        size: '118KB',
        url: base_url + '/3-三桶油65米/'
    },
]

let CYC = [
    {
        name:'应急保障餐车.docx',
        type:'word',
        size: '15.9M',
        url: base_url + '/4-三桶油餐饮车/'
    },
    {
        name:'餐车基本信息（SYM5181XCC）三一重工饮食保障车技术规格书CV5.docx',
        type:'word',
        size: '462KB',
        url: base_url + '/4-三桶油餐饮车/'
    },
    {
        name:'餐车原理图.doc',
        type:'word',
        size: '203KB',
        url: base_url + '/4-三桶油餐饮车/'
    },
]

let ZJC = [
    {
        name:'多功能化学侦检消防车—电气原理图.pdf',
        type:'pdf',
        size: '616KB',
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能化学侦检消防车技术规格书.docx',
        type:'word',
        size: '946KB',
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能化学侦检消防车—气路原理图.pdf',
        type:'pdf',
        size: '81KB',
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能化学侦检消防车—水路原理图.pdf',
        type:'pdf',
        size: '75KB',
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能化学侦检消防车—应急呼吸系统原理图.pdf',
        type:'pdf',
        size: '51KB',
        url: base_url + '/5-三桶油侦检车/'
    },
]

let LYC = [
    {
        name:'淋浴车基本信息（SYM5180XLY）三一重工淋浴车技术规格书.docx',
        type:'word',
        size: '197KB',
        url: base_url + '/6-三桶油淋浴车/'
    },
    {
        name:'淋浴车使用说明书.docx',
        type:'word',
        size: '2.6M',
        url: base_url + '/6-三桶油淋浴车/'
    },{
        name:'淋浴车原理图.doc',
        type:'word',
        size: '288KB',
        url: base_url + '/6-三桶油淋浴车/'
    },
]

let SYC = [
    {
        name:'宿营车基本参数（SYM5181TSY）三一重工-24人宿营车技术规格书CV5.docx',
        type:'word',
        size: '936KB',
        url: base_url + '/7-三桶油宿营车/'
    },
    {
        name:'应急保障宿营车说明书.docx',
        type:'word',
        size: '2.2M',
        url: base_url + '/7-三桶油宿营车/'
    },
    {
        name:'宿营车原理图.doc',
        type:'word',
        size: '264KB',
        url: base_url + '/7-三桶油宿营车/'
    },
]

let ZZXC = [
    {
        name:'三一重工国六汕德卡自装卸式消防车技术规格书-SYM5210TXFZX80.docx',
        type:'word',
        size: '153KB',
        url: base_url + '/8-三桶油自装卸车/'
    },
    {
        name:'SYM5200TXFZX70ZS自装卸式消防车操作保养手册.pdf',
        type:'pdf',
        size: '2.1M',
        url: base_url + '/8-三桶油自装卸车/'
    },
    {
        name:'汕德卡国六自装卸消防车电气原理图.pdf',
        type:'pdf',
        size: '122KB',
        url: base_url + '/8-三桶油自装卸车/'
    },
    {
        name:'汕德卡国六自装卸消防车液压原理图.pdf',
        type:'pdf',
        size: '175KB',
        url: base_url + '/8-三桶油自装卸车/'
    },
]

export default getFileList

