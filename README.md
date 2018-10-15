# taopiaopiao
淘票票


###下载项目后 设置好自己的数据库

### 在项目目录下运行
~~~
python manager.py db init

python manager.py db migrate

python manager.py db upgrade
~~~
###生成迁移脚本并迁移到数据库

在项目目录下运行
~~~
python manager.py runserver -r -d
~~~
启动服务器

访问http://127.0.0.1:5000

看到下面代码即是成功
~~~
{
    "msg": "ok",
    "status": 200
}
~~~
