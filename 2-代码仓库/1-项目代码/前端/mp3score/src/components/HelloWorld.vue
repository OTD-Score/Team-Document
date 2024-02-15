<template>
  <div id="test" @click='test'>点击测试</div>
</template>

<script>
import Utils from '@/utils/request';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods:{
    test(){
      let data = {
        name : '张三',
        tel : 13574141111
      }

      Utils.getReq('hello',data).then((res)=>{
        console.log('成功',res)
      }).catch(err =>{
        console.log('失败',err)
      }).finally(()=>{
        console.log('完成')
      })
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #test{
    margin: 30px 0;
    
  }

  
</style>
