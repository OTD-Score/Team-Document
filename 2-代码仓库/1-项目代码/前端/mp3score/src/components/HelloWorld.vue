<template>
  <div @click='test'>点击测试</div>
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

      Utils.postReq('login',data).then((res)=>{
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
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
