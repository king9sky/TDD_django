配置网站
=============

##需要的包
* Nginx
* python3.6
* virtualenv + pip
* git

##Nginx虚拟主机
* 参考list_site.conf
* 把SITENAME替换为所需域名

##开机启动
* 参考lists-site.sh
* 把SITENAME替换为所需域名

##文件夹结构


/home/username
  └── sites
         │──SITENAME           
             ├── database
             ├── source
             ├── static
             └── virtualenv