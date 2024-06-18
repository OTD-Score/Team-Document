/* eslint-disable */

function getFileList(type = '21M',id){
    //type = '21M' "51M" "65M" "CYC" "ZJC" "LYC" "SYC" "ZZXC" "PM180" "BP450" "DF20"
    switch(type){
        case '21M':
            return M21;
        case '51M':
            return M51;
        case '65M':
            return M65;
        case 'CYC':
            return CYC;
        case 'ZJC':
            return ZJC;
        case 'LYC':
            return LYC;
        case 'SYC':
            return SYC;
        case 'ZZXC':
            return ZZXC;
        case 'PM180':
            return PM180;
        case 'BP450':
            return BP450;
        case 'DF20':
            return DF20;
        case 'DG55':
            return DG55;
    }
}

let base_url = 'https://yingji.irootech.com/upload';

let M21 = [
    {
        name:'JP21润滑图.pdf',
        type:'pdf',
        size: '201KB',
        url: base_url + '/1-三桶油21米/'
    },
    {
        name:'4桥21米消防车液压系统原理图（外发版）.pdf',
        type:'pdf',
        size: '197KB',
        url: base_url + '/1-三桶油21米/'
    },
    {
        name:'JP21维保记录表.pdf',
        type:'pdf',
        size: '304KB',
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
        name:'JP21水路原理图.pdf',
        type:'pdf',
        size: '179KB',
        url: base_url + '/1-三桶油21米/'
    },
    {
        name:'SYM5435JXFJP21举高喷射消防车操作保养手册1.pdf',
        type:'pdf',
        size: '50.6M',
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
        name:'JP51润滑图.pdf',
        type:'pdf',
        size: '145KB',
        url: base_url + '/2-三桶油51米/'
    },
    {
        name:'JP51维保记录表.pdf',
        type:'pdf',
        size: '328KB',
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
        name:'JP51操作保养手册.pdf',
        type:'pdf',
        size: '59.7M',
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
        name:'65米润滑图.pdf',
        type:'pdf',
        size: '146KB',
        url: base_url + '/3-三桶油65米/'
    },
    {
        name:'65米维保记录表1.pdf',
        type:'pdf',
        size: '340KB',
        url: base_url + '/3-三桶油65米/'
    },
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
        name:'SYM5520JXFJP65举高喷射消防车操作保养手册.pdf',
        type:'pdf',
        size: '68.2M',
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
    {
        name:'保障餐车维保记录表.pdf',
        type:'pdf',
        size: '363KB',
        url: base_url + '/4-三桶油餐饮车/'
    },
]

let ZJC = [
    {
        name:'多功能危险化学品监测车操保手册.pdf',
        type:'pdf',
        size: '3.4M',   
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能危险化学品监测车—电气原理图.pdf',
        type:'pdf',
        size: '616KB',
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能危险化学品监测车技术规格书.pdf',
        type:'pdf',
        size: '1.4M',
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能危险化学品监测车—气路原理图.pdf',
        type:'pdf',
        size: '81KB',
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能危险化学品监测车—润滑图.pdf',
        type:'pdf',
        size: '214KB',
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能危险化学品监测车—水路原理图.pdf',
        type:'pdf',
        size: '75KB',
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能危险化学品监测车维保记录表.pdf',
        type:'pdf',
        size: '238KB',
        url: base_url + '/5-三桶油侦检车/'
    },
    {
        name:'多功能危险化学品监测车—应急呼吸系统原理图.pdf',
        type:'pdf',
        size: '51KB',
        url: base_url + '/5-三桶油侦检车/'
    }
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
    },
    {
        name:'淋浴车原理图.doc',
        type:'word',
        size: '288KB',
        url: base_url + '/6-三桶油淋浴车/'
    },
    {
        name:'淋浴车维保记录表.pdf',
        type:'pdf',
        size: '376KB',
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
    {
        name:'宿营车维保记录表.pdf',
        type:'pdf',
        size: '388KB',
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
    {
        name:'自装卸车维保记录表.pdf',
        type:'pdf',
        size: '400KB',
        url: base_url + '/8-三桶油自装卸车/'
    },
]

let PM180 = [
    {
        name:'PM180泡沫消防车车型基本信息.pdf',
        type:'pdf',
        size: '368KB',
        url: base_url + '/9-三桶油PM180/'
    },
    {
        name:'PM180维保记录表.pdf',
        type:'pdf',
        size: '412KB',
        url: base_url + '/9-三桶油PM180/'
    },
    {
        name:'PM180泡沫消防车电气原理图V0_20230413.pdf',
        type:'pdf',
        size: '147KB',
        url: base_url + '/9-三桶油PM180/'
    },
    {
        name:'PM180泡沫消防车气路原理图V0.pdf',
        type:'pdf',
        size: '107KB',
        url: base_url + '/9-三桶油PM180/'
    },
    {
        name:'PM180水路原理图V0.pdf',
        type:'pdf',
        size: '209KB',
        url: base_url + '/9-三桶油PM180/'
    },
    {
        name:'PM180操保手册PS00037664V0.pdf',
        type:'pdf',
        size: '66.9M',
        url: base_url + '/9-三桶油PM180/'
    },
]

let BP450 = [
    {
        name:'BP450泵浦车技术规格书V1.docx',
        type:'word',
        size: '1.53M',
        url: base_url + '/10-三桶油泵浦消防车/'
    },
    {
        name:'泵浦消防车电气原理图.pdf',
        type:'pdf',
        size: '293KB',
        url: base_url + '/10-三桶油泵浦消防车/'
    },
    {
        name:'泵浦消防车水路原理图.pdf',
        type:'pdf',
        size: '23KB',
        url: base_url + '/10-三桶油泵浦消防车/'
    },
    {
        name:'泵浦消防车液压原理图.pdf',
        type:'pdf',
        size: '80KB',
        url: base_url + '/10-三桶油泵浦消防车/'
    },
    {
        name:'泵浦消防车操保手册.pdf',
        type:'pdf',
        size: '5.0M',
        url: base_url + '/10-三桶油泵浦消防车/'
    },
    {
        name:'泵浦消防车润滑图.pdf',
        type:'pdf',
        size: '85KB',
        url: base_url + '/10-三桶油泵浦消防车/'
    },
    {
        name:'泵浦消防车维保记录表.pdf',
        type:'pdf',
        size: '232KB',
        url: base_url + '/10-三桶油泵浦消防车/'
    },
]
let DF20 = [
    {
        name:'DF20水带敷设车技术规格V1.docx',
        type:'word',
        size: '443KB',
        url: base_url + '/11-三桶油水带敷设车/'
    },
    {
        name:'DF20水带车水路气路原理图.pdf',
        type:'pdf',
        size: '40KB',
        url: base_url + '/11-三桶油水带敷设车/'
    },
    {
        name:'DF20水带车液压原理图.pdf',
        type:'pdf',
        size: '118KB',
        url: base_url + '/11-三桶油水带敷设车/'
    },
    {
        name:'水带敷设车电气原理图.pdf',
        type:'pdf',
        size: '901KB',
        url: base_url + '/11-三桶油水带敷设车/'
    },
    {
        name:'水带敷设消防车操作保养手册.pdf',
        type:'pdf',
        size: '18.8M',
        url: base_url + '/11-三桶油水带敷设车/'
    },
    {
        name:'DF20水带敷设车润滑图.pdf',
        type:'pdf',
        size: '176KB',
        url: base_url + '/11-三桶油水带敷设车/'
    },
    {
        name:'DF20水带敷设车维保记录表.pdf',
        type:'pdf',
        size: '218KB',
        url: base_url + '/11-三桶油水带敷设车/'
    },
]
let DG55 = [
    {
        name:'三一重工55米登高平台消防车技术规格书V4-202405（SYM5430JXFDG55+沃尔沃FM500+100泵).docx',
        type:'word',
        size: '2.1M',
        url: base_url + '/12-三桶油登高55/'
    },
    {
        name:'四桥登高平台消防车产品介绍.docx',
        type:'word',
        size: '976KB',
        url: base_url + '/12-三桶油登高55/'
    },
    {
        name:'整车检测报告.pdf',
        type:'pdf',
        size: '1.2M',
        url: base_url + '/12-三桶油登高55/'
    },
    
]
export default getFileList

