/*const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave:false
})*/
/*上述为初始配置，下面为PC端页面自动适应不同分辨率配置*/
const { defineConfig } = require('@vue/cli-service')


// 引入等比适配插件
const px2rem = require("postcss-px2rem");

// 配置基本大小
const postcss = px2rem({
  // 基准大小 baseSize，需要和rem.js中相同
  remUnit: 32,
});
// module.exports = defineConfig({
//   transpileDependencies: true,
//   lintOnSave:false,
// })

// 使用等比适配插件
module.exports = {
  lintOnSave: false,
  // 此三行代码是为项目打包运行所写----
  publicPath: "./", 
  outputDir: "dist",
  assetsDir: "static",
  //---------------------------
  css: {
    loaderOptions: {
      postcss: {
        postcssOptions: {
          plugins: [postcss],
          },
      },
    },
  },
  devServer: {
    proxy: {
      '/api': {
        target: 'https://api.klang.io/', // 目标后端服务器地址
        changeOrigin: true, // 改变Origin来解决跨域问题
        pathRewrite: {
          '^/api': '' // 重写路径
        }
      }
    }
  }
};
