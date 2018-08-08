""" 
diango
第一步安装：
    1、pip install diango
    2、或者是，下载压缩包，解压  进入解压目录  运行 python setup.py install
第二步，新建项目
    diango-admin startproject first_django
第三步，通过cmd命令，在Test项目下新建一个应用webdev
    在first_python文件夹下运行：python manage.py startapp webdev
第四步，运行
    在first_python文件夹下运行：python manage.py runserver 127.0.0.1:8001
    浏览器下运行127.0.0.1:8001  ok!
    如果想要其他计算机也可以访问该页面，则执行如下命令：
    python manage.py runserver 0.0.0.0:8001
第五步，创建web项目
    python manage.py startapp webdev
"""