Title: 采用Pelican+Github搭建数据科学博客
Author: Joshua
Date: 2017-07-07 14:00
Category: Blog
Tags: pelican,python,blog,git
Comment: true
Jiathis: true
related_posts:true
Slug: 1490367116
Summary: 用 Python 的 Pelican 库搭建数据科学博客，并将 blog 挂在 Github Pages 上...




>### 前言
在今年的个人计划中，想要搭建一个数据挖掘的平台，主要目的是，希望通过这件事能让自己对数据挖掘、机器学习的各种算法都很熟练，同时对搭建这样的平台框架有个基础的实践与认知。因此，就想在做这件事的时候能将自己趟过的坑记录整理下来，帮助自己从技术上提高。所以，首先得搭建一个自己的博客。虽然，目前网上有很多现成的博客系统，但是自己总觉得自定义的才是最炫酷的（其实并没有什么卵用），希望能一直坚持下来吧。


## 环境

Pelican是一套开源的使用Python编写的博客静态生成, 可以添加文章和和创建页面, 可以使用`MarkDown`，` reStructuredText`和`AsiiDoc`的格式来书写, 同时使用 Disqus评论系统, 支持 RSS和Atom输出, 插件, 主题, 代码高亮等功能, 采用Jajin2模板引擎, 可以很容易的更改模板，也可以很容易的把文章部署到 GitHub Pages 让别人阅读，欢迎进入我的[Blog 站点](https://zoujoshua.github.io)进行效果预览。

* **本地环境**

windows 10 64位/ubuntu 16.04（笔记本为win10，台式机为ubuntu系统）

Python 3.5

*  **服务器环境**

Github Pages（把 Github 的仓库当成服务器）

* **安装**


> 安装Python

如果你还没有安装 Python ，建议使用 Python 3.5，可以到官网[安装](http://www.python.org/)。

> 安装Pelican

建议在 Virtualenv （Python虚拟环境）下使用，创建并激活一个[虚拟环境](http://docs.python-guide.org/en/latest/dev/virtualenvs/)。

	virtualenvs blogs 		# 创建blog的虚拟环境
	cd blogs/scripts
	pip pelican
	activate				# 激活虚拟环境
	mkdir blog 				# 创建blog目录
> 安装Markdown

	cd blogs/scripts
	pip install markdown
	
## 博客框架
通过初始化 Pelican 设置生成一个基本的博客框架，在创建的文件夹下运行 pelican-quickstart 时，会开始一个交互式博客安装过程。根据提示一步一步输入相应的配置项，对于不了解 pelican 框架或第一次安装的情况下，大多数问题直接点击`Enter`接受默认即可，后续可以在`pelicanconf.py`文件里更改配置，个人`pelicanconf.py`[详细配置](https://github.com/ZouJoshua/pelican-blog/blob/master/pelicanconf.py)。

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
	|  └──articles 			 # 目录，pelicanconf.py中ARTICLE_URL指定格式分类文件
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
	|——.gitignore        	 # 上传Git时排除指定类型文件



## 主题设置

    git clone https://github.com/getpelican/pelican-themes.git # 获取全部主题
    cd pelican-themes
    pelican-themes -i BT3-Flat  #可换成你自己的theme

因为个人喜好不同，我选择了 BT3-Flat 这个主题，但是由于原主题部分文件的问题，我自己修改了模板同时在`pelicanconf.py`文件中修改

	THEME = './pelican-themes/BT3-Flat'      # 设置的主题所在根目录下的路径


## Plugin设置

    git clone https://github.com/getpelican/pelican-plugins.git     # 将所支持的插件clone到本地，方便使用


#### Jupyter插件

Pelican默认情况下并不支持使用jupyter写博客 – 我们需要安装插件来进行支持。我们将把插件以git submodule的方式进行安装以便于管理。

- 执行`git init`将当前文件夹初始化为一个git仓库。

- 创建`plugins`文件夹
- 在plugins文件夹中执行`git submodule add https://github.com/danielfrg/pelican-ipynb.git plugins/ipynb`来添加插件

为了启动插件，我们需要修改`pelicanconf.py`并将以下内容添加到尾部：


    MARKUP = ('md', 'ipynb')
    PLUGIN_PATHS = [ './plugins' ]  # 如果像原文直接PLUGIN_PATH = `./plugins`而不使用列表会报warning
    PLUGINS = ['ipynb.markup']
后期在本地测试时发现，加上Jupyter后，部分功能未显示，所以暂时没把Jupyter功能放入进去，所以目前文档只支持Markdown。

#### JIATHIS社会化分享功能

在`pelicanconf.py`文件中配置：

	JIATHIS = True
#### Blog Search

在 [Swiftype](https://swiftype.com/users/sign_up)注册账号，得到输入自己的blog网址得到 API ，然后在 `pelicanconf.py` 中添加

	SWIFTYPE = 'swiftype_api'


#### Disqus第三方评论

开启个人博客的原因在于分享知识，分享就需要交流，评论模块当然少不了。第三方评论系统有很多，这里选用很流行的Disqus作为第三方评论系统，在Disqus上申请帐号，按照流程Disqus会分配给你站点的Shortname，记牢Shortname，如果忘了请进入admin/settings中查看。

    Site name: {your git account name}.github.io
    Admin URL: {Shortname}.disqus.com
然后同理，在`pelicanconf.py`添加：
	
	DISQUS_SITENAME = Shortname

由于DISQUS是国外的第三方应用，所以如果在国内想看到得FQ，后期争取支持国内友言之类的应用。

## BlogRoll和Social设置

设置一些Blog链接，通过设置LINKS实现,可链接到别人的blog，或者自己的社交圈。在`pelicanconf.py`文件中配置：

#### Blogroll

	LINKS = (('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

#### Social widget

	SOCIAL = (('weibo','http://www.weibo.com/233499456'),
		  ('envelope','mailto:joshua_zou@163.com'),
          ('twitter', 'https://twitter.com/joshua_zou'),
          ('facebook','https://www.facebook.com/joshua.zou.127'),
          ('linkedin', 'https://www.linkedin.com/in/%E5%B8%85-%E9%82%B9-736390135/'),
          ('github','https://github.com/ZouJoshua'))
#### Feed设置
    FEED_RSS = "feeds/all.rss.xml" 
    CATEGORY_FEED_RSS="feeds/%s.rss.xml"    #为分类添加Feed

## 撰写并发布第一篇blog
插件配置等都完成后，就可以开始书写第一篇Blog了。


- 创建一个Markdown文件，书写自己想记录的blog内容。
- 在Markdown文件开头加入文档的头信息。
- 把书写完成的Markdown文件复制到`content`目录下。
>

	Title: Pelican搭建博客        # blog的标题
	Author: Joshua				 # blog作者名字
	Date: 2017/7/7 14:02:40 	 # blog发布日期
	Category: Pelican			 # blog分类
	Tags: pelican，python，blogs # blog的标签
	Slug: pelican-blog			 # blog在服务器上的路径，是文档的唯一标识，生成html时直接用这个值做html的文件名，个人采用的是当前的时间戳 
	Summary: My first post,read it to find out.  # blog的摘要

#### 将完成的 Markdown 生成 HTML

在blog目录下运行命令。

	pelican content				# 将content目录下的markdown文件生成html文件，输出到output文件里
	cd output
	python -m http.server		# 启动本地服务器预览blog
在浏览器里访问 `localhost:8000` 来预览你的博客


## 发布博客站点
三种方法：

- **Pelican命令**

>

	pelican content -s publishconf.py

- **Fabric**

>
	
    pip install fabric
    fab build
    fab regenerate
    fab serve
    fab publish


- **Make**

>

	make html
	make regenerate
	make serve
	make devserver
	./develop_server.sh stop
make 命令不是 Windows 系统自带的dos命令，需要安装，[点此下载](http://www.equation.com/servlet/equation.cmd?fa=make)，根据自己电脑选择32位或64位。安装完成后，须将安装路径添加到系统环境变量。

个人常选用 pelican 命令及 make 命令组合将新生成的 html 文件发布到 Github Pages 。

#### GitHub Pages的创建和 Git 本地仓库配置

要将 blog 部署到 Github 上，必须在本地建立一个 Git 仓库，同时必须确保在 Github server 端有远程仓库，名字一般为 `username.github.io` 。

GitHub Pages 是 GitHub 的一项功能，允许你快速部署静态网站，让所有人都可以通过特定 URL 访问。为了完成它的配置，我们需要：

* 注册一个 GitHub 帐号，如果你还没有的话。
* 创建一个叫 username.github.io 的仓库，这里 username 是你的 GitHub 用户名。[这里](https://help.github.com/articles/create-a-repo/)有更详细的说明。


本部分 Git 本地仓库的配置，[可参考此博文](https://zoujoshua.github.io/articles/1500367116/)。

创建一个叫做 `.gitignore` 的文件，并添加入这个[文件](https://github.com/github/gitignore/blob/master/Python.gitignore)的内容。最终我们将会把文件提交到 Git ，`.gitignore`将会排除指定类型的文件。

	cd output
	git init         # 产生一个.git文件夹
	git remote add origin https://github.com/****/****.github.io.git    #将远程仓库配置到本地
	git add .
	git commit -m "commit blog"
	git push -u origin master

对于后期的更新，如果需要修改远程仓库，可以选用下面命令之一，先将远程仓库配置到本地，然后进入本地远程仓库目录进行修改，最终提交。

	git clone https://github.com/****/****.github.io.git        #将远程仓库克隆到本地
	cd xxx(clone到本地的仓库路径）
	git rm -rf xxx 						# 删除文件夹
	git commit -m "Delete some files."  # 提交修改
	git push origin xxx					# 将修改提交到远程仓库的分支或主支


#### 设置一键上传部署到 Github

打开根目录下的Makefile文件，修改以下三个地方：

	OUTPUTDIR=$(BASEDIR)/output/    #本地博客仓库路径
 	publish:    
 	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)    #可修改OUTPUTDIR,发布的blog站点的输出路径
 	github: publish    
 	cd OUTPUTDIR ; git add . ;  git commit -am 'your comments' ; git push
设置完后，以后写完文章就可以通过在blog根目录下执行`make github`进行一键部署了。

可在Makefile文件中增加如下命令，有新文章要发布时可用 `make upload`一键更新到 Github 上。
	
	upload:
		cd $(OUTPUTDIR) && git add -A && git commit -am "update blog" && git push origin master
其实，命令文章的更新上传本质还是用 Git 命令的，只不过 make 命令可以将 Git 命令整合后一键操作，自然比一个一个命令去上传更新来的快。


## 问题
在博客搭建的过程中，趟过的一些坑。

1. 因本人关注数据挖掘、数据分析、算法方面的内容，所以希望用Jupyter Notebook 及 Markdown 搭建一个数据科学博客，但是所选用的这个主题对Jupyter Notebook的插件支持并不好，同时用两种文件方式的时候，整个主题的部分功能显示不全，但不影响总体使用，对这个小瑕疵并不感冒的可以将 Jupyter 插件加入，但是本人有些轻度完美主义，所以暂时先选择Markdown来写。
2. 对于BT3-Flat原主题模板文件，出现部分错误，在此基础上进行改进，同时在主题模板文件中加入JIATHIS社会化分享功能所必须的 `css` 文件和 `js` 文件，使得主题支持社会化分享功能。
3. 对于DISQUS第三方评论插件的显示问题。由于DISQUS是国外的，在国内浏览的话会被Q的，如果可以FQ，是可以使用的。
4. 由于个人不太懂css响应式布局，所以在手机端显示会有一些问题，稍后研究完再进行修改。