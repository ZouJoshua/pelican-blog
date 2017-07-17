title: test2
author: Joshua
date: 2017-07-09 14:00
category: Pelican
tags: pelican，numpy，blogs
comment: true
jiathis: true
slug: 1499656175
summary: My first post,read it to find out.


# 采用pelican搭建数据科学博客 


>## 前言
在今年的个人计划中，想要搭建一个数据挖掘的平台，主要目的是，希望通过这件事能让自己对数据挖掘、机器学习的各种算法都很熟练，同时对搭建这样的平台框架有个基础的实践与认知。因此，就想在做这件事的时候能将自己趟过的坑记录整理下来，帮助自己从技术上提高。所以，首先得搭建一个自己的博客。虽然，目前网上有很多现成的博客系统，但是自己总觉得自定义的才是最炫酷的（其实并没有什么卵用），希望能一直坚持下来吧。


### 环境

* 本地环境

windows 10 64位/ubuntu 16.04（笔记本为win10，台式机为ubuntu系统）

Python 3.5

*  服务器环境

ubuntu 16.04（AWS云服务）

python 3.5

## 博客框架
通过初始化Pelican设置生成一个基本的博客框架，在创建的文件夹下运行pelican-quickstart时，会开始一个交互式博客安装过程。根据提示一步一步输入相应的配置项，对于不了解pelican框架或第一次安装的情况下，大多数问题直接点击`Enter`接受默认即可，后续可以在`pelicanconf.py`文件里更改配置。

    (blogs) D:\Python\envs\blogs\blog>pelican-quickstart
	Welcome to pelican-quickstart v3.7.1.

	This script will help you create a new Pelican-based website.

	Please answer the following questions so this script can generate the files needed by Pelican.


	> Where do you want to create your new web site? [.]
	> What will be the title of this web site? Joshua's Blog
	> Who will be the author of this web site? Joshua Zou
	> What will be the default language of this web site? [Chinese (Simplified)]
	> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
	> Do you want to enable article pagination? (Y/n)
	> How many articles per page do you want? [10]
	> What is your time zone? [Europe/Paris] Asia/Shanghai
	> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) 
	> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
	> Do you want to upload your website using FTP? (y/N)
	> Do you want to upload your website using SSH? (y/N)
	> Do you want to upload your website using Dropbox? (y/N)
	> Do you want to upload your website using S3? (y/N)
	> Do you want to upload your website using Rackspace Cloud Files? (y/N)
	> Do you want to upload your website using GitHub Pages? (y/N)
	Done. Your new project is available at D:\Python\envs\blogs\blog

完成后会在相应的目录里生成如下基础框架结构及文件：


	blog/
	├── content            # 存储Blog文件的目录，这个目录及子目录下的所有md和rst文件都会被转成html
	│   └── (pages)        # Blog文件，如*.md、*.ipynb等文件
	├── output             # 将blog文件转化成相应的html及相应文件的存放目录
	├── develop_server.sh  # pelican简易web服务器操作文件
	├── Makefile           # 方便管理博客的Make命令文件
	├── fabfile.py         # 与make类似，可用fab publish，fab server命令
	├── pelicanconf.py     # 本地开发时的配置文件
	└── publishconf.py     # 发布时的配置文件，可删除


后续配置完整后，框架如下：

	blog/
	|--content 				 # 存储Blog文件的目录，这个目录及子目录下的所有md和rst文件都会被转成html
	|  └──(pages) 	 	 	 # Blog文件，如*.md、*.ipynb等文件
	|--output 				 # 将blog文件转化成相应的html及相应文件的存放目录
	   └──.git 				 # 执行git init之后，产生的远程仓库目录
	|  └──author 			 # 作者目录，存放pelicanconf.py中指定的Author文件
	|  └──category 		     # 分类目录，默认目录文件为misc，在编辑器中指定
	|  └──feeds 			 # 目录，pelicanconf.py中FEED_RSS指定的XML文件
	|  └──pages 			 # 目录，pelicanconf.py中ARTICLE_URL指定格式分类文件
	|  └──tag 				 # 目录，存放编辑器开头所指定的Tag
	|  └──theme 			 # 目录，存放博客模板文件
	|  └──archives.html,authors.html,categories.html,index.html, tags.html
	|——pelican-plugins 		 # 目录，pelican插件
	|——pelican-themes 		 # 目录，pelican主题
	|——develop_server.sh 	 # pelican简易web服务器操作文件
	|——Makefile              # make 命令文件
	|——fabfile.py 			 # 与make类似，可用fab publish, fab server命令
	|——pelicanconf.py        # 本地开发时的配置文件
	|——publishconf.py        # 发布时的配置文件，可删除



## Git远程仓库配置

要将blog部署到git上，必须在本地建立一个git仓库，同时必须确保在github server端有远程仓库，名字一般为username.github.io。本地操作命令如下：

	cd output
	git init         #产生一个.git文件夹
	git remote add origin https://github.com/username.github.io.git    #将远程仓库配置到本地


### Feed设置
    FEED_RSS = u"feeds/all.rss.xml" 
    CATEGORY_FEED_RSS=u"feeds/%s.rss.xml"    #为分类添加Feed







### 主题设置

    git clone https://github.com/getpelican/pelican-themes.git # 获取全部主题,有些主题下载下来为空需要自己重新找下该主题的链接重新下载安装下
    cd pelican-themes
	git clone https://github.com/kdeldycke/plumage.git
	pelican-themes -i plumage  #可换成你自己的theme

#### 主题头像设置

	blog/
  	└── content/
      └── images/
          └──yourheaderimage.png
在配置文件`pelicanconf.py`中添加设置：

	STATIC_PATHS = ['images']
	HEADER_IMAGE = "yourheaderimage.png"

### Disqus第三方评论

第三方评论系统有很多，这里选用很流行的Disqus作为第三方评论系统，同样需要到Disqus官网申请账号，然后填写两处：

    Site name: {your git account name}.github.io
    Admin URL: {Shortname}.disqus.com

### Plugin设置

    git clone https://github.com/getpelican/pelican-plugins.git
- 获取全部插件`git clone https://github.com/getpelican/pelican-plugins.git`

### Jupyter插件

Pelican默认情况下并不支持使用jupyter写博客 – 我们需要安装插件来进行支持。我们将把插件以git submodule的方式进行安装以便于管理。

- 执行`git init`将当前文件夹初始化为一个git仓库。

- 创建`plugins`文件夹
- 在plugins文件夹中执行`git submodule add https://github.com/danielfrg/pelican-ipynb.git plugins/ipynb`来添加插件

为了启动插件，我们需要修改pelicanconf.py并将以下内容添加到尾部：


    MARKUP = ('md', 'ipynb')
    PLUGIN_PATHS = [ './plugins' ]  # 如果像原文直接PLUGIN_PATH = `./plugins`而不使用列表会报warning
    PLUGINS = ['ipynb.markup']




### Menu Item设置
    MENUITEMS = (("ITEM1","http://github.com"),
             ("ITEM2",URL),
            ......)

### BlogRoll和Social设置
设置一些Blog链接，通过设置LINKS实现,具体如下：

    LINKS =  (("Github", "https://github.com"),
      ("Cnblogs", URL),)
	SOCIAL = (("博客园", "http://www.cnblogs.com"),
         ("Github','http://github.com"),)


### 发布博客站点
三种方法：

- pelican命令

>

	pelican content -s publishconf.py

- fabric

>
	
    pip install fabric
    fab build
    fab regenerate
    fab serve
    fab publish


- make

>

	make html
	make regenerate
	make serve
	make devserver
	./develop_server.sh stop

