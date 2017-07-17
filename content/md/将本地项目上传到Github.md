# 将本地项目上传到Github

本次操做需要用到管理工具`Git`，[点击下载](https://git-scm.com/)。



## 本地Git仓库设置

1. 创建Git配置文件。

	通过命令`git init`把即将要上传的本地项目文件夹变成Git可管理的仓库，即创建该项目的本地版本库。你会发现你的文件下生成一个`.git`文件夹，默认是隐藏文件。可通过`git status`来查看你当前的状态。Git安装好之后，打开所要上传的项目文件夹，鼠标右键点击windows系统下选择`Git Bash Here`。

		$ git init
![](http://i.imgur.com/IL1rdhx.png)
2. 通过`git add .`（.和add之间有空格）将当前所有文件添加到仓库上，仍可通过`git status`来查看你当前的状态。

		$ git add .

3. 用`git commit`把项目提交到仓库，`-m`后面引号里面是本次提交的注释内容，这个可以不写，但最好写上，不然会报错，详情自行Google。

		$ git commit -m "first commit"

	本地Git仓库这边的工作做完了，下面就到了连接远程仓库（也就是连接Github）

## 远程仓库Github设置

本地Git仓库和Github仓库之间的传输是通过SSH加密的，所以连接时需要设置一下，先在本地生成一`.ssh`。
	
1. 创建SSH KEY，先查看本地是否有.ssh文件，有的话删掉。

		$ cd ~/.ssh

2. 输入命令，生成.ssh，写你自己的邮箱

		$ ssh-keygen -t rsa -C "your email@.com"

	一直回车就可以，这样就表示成功了，会在C盘的用户目录的根目录下生成一个`.ssh`文件，如果找不到，可以搜索一下，文件下会有`id_rsa`与`id_rsa.pug`两个文件。

3. 为了避免与Github创建连接时出错，可以新建一个config文件，将以下代码复制进去

		Host github.com
    	User git
    	Hostname ssh.github.com
    	PreferredAuthentications publickey
    	IdentityFile ~/.ssh/id_rsa
    	Port 443

4. 登录Github，找到右上角的图标，打开点进里面的`Settings`，再选中里面的`SSH and GPG KEYS`，点击右上角的`New SSH key`，然后`Title`里面随便填，再把刚才`id_rsa.pub`里面的内容复制到`Title`下面的`Key`内容框里面，最后点击`Add SSH key`，这样就完成了SSH Key的加密。

5. 测试连接是否成功，下图表示访问成功

		$ ssh -t git@github.com

6. 在Github上创建一个Git仓库，此时如果你勾选了`Initialize this repository with a README`（就是创建仓库的时候自动给你创建一个README文件），那么到了第8步你将本地仓库内容推送到远程仓库的时候就会报一个*failed to push some refs to https://github.com/guyibang/TEST2.git*的错误,这是由于你新创建的那个仓库里面的README文件不在本地仓库目录中，这时我们可以通过以下命令先将内容合并以下。

7. Github上创建好Git仓库之后我们就可以和本地仓库进行关联了，注意origin后面加的是你Github上创建好的仓库的地址。根据创建好的Git仓库页面的提示，可以在本地TEST仓库的命令行输入：

		$ git remote add origin git@github.com:heshaui/pdfjsDemo.git

	解决办法：

		先输入：$ git remote rm origin
		再输入：$ git remote add origin git@github.com:heshaui/pdfjsDemo.git

8. 关联好之后就可以把本地库的所有内容推送到远程仓库（也就是Github）上了
	
		$ git push -u origin master

	由于新建的远程仓库是空的，所以要加上`-u`这个参数，等远程仓库里面有了内容之后，下次再从本地库上传内容的时候只需下面这样就可以了。