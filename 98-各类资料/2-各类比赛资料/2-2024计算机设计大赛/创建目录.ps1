$number = Read-Host "请输入作品编号"  
$name = Read-Host "请输入作品名称"  
  
# 创建主文件夹  
New-Item -ItemType Directory -Force -Path "$number-$name"  
  
# 进入主文件夹  
Push-Location "$number-$name"  
  
# 创建子文件夹  
New-Item -ItemType Directory -Force -Path "$number-01 作品与答辩材料"  
New-Item -ItemType Directory -Force -Path "$number-02 素材与源码"  
New-Item -ItemType Directory -Force -Path "$number-03 设计与开发文档"  
New-Item -ItemType Directory -Force -Path "$number-04 作品演示视频"  
  
# 返回原目录  
Pop-Location