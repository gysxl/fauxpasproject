#!/bin/bash

function get_xcodeproj_path
{
	read -p "👉  请输入项目的 .xcodeproj 文件路径：" filepath

	if [[ -d $filepath ]]; then
		if [[ ${filepath:0-10:10} = '.xcodeproj' ]]; then
			echo '【开始检测...】'
			check_project $filepath
		elif [[ ${filepath:0-11:11} = '.xcodeproj/' ]]; then
			echo '【开始检测...】'
			check_project $filepath
		else
			echo "【输入错误，或文件不存在，请重新输入！！！】"
			get_xcodeproj_path
		fi
	else
		echo "【输入错误，或文件不存在，请重新输入！！！】"
		get_xcodeproj_path
	fi
}

# 检查brew是否安装
function check_brew
{
	if hash brew 2>/dev/null; then
		echo "检查环境(1/5) - homebrew已安装" #brew已安装
	else
		/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
		echo "检查环境(1/5) - 安装homebrew"
	fi
}
# 检查fauxpas是否安装
function check_fauxpas
{
	if [ -d "/Applications/FauxPas.app" ]; then
		echo "检查环境(2/5) - FauxPas已安装"
	else
		# echo "FauxPas不存在 - 开始安装"
		brew cask reinstall fauxpas
		echo "检查环境(2/5) - 安装FauxPas"
	fi
}

# Fauxpas授权
function updatelicense
{
	Fauxpas updatelicense organization-set  ********************  1>/dev/null
	echo "检查环境(3/5) - Fauxpas已授权"
}

# 安装Fauxpas命令行
function installcli
{
	if [ -f "/usr/local/bin/fauxpas" ]; then
		echo "检查环境(4/5) - FauxPas命令行工具已安装"
	else
		/Applications/FauxPas.app/Contents/Resources/install-cli-tools
		echo "检查环境(4/5) - 安装FauxPas命令行工具"
	fi
}

# 安装往xcode中注入脚本的环境
function install_xcodeproj
{
	gem which xcodeproj 1>/dev/null 2>/dev/null
	if [ $? -eq 0 ]
	then
		echo "检查环境(5/5) - xcodeproj已安装"
	else
		gem install xcodeproj
		echo "检查环境(5/5) - 安装xcodeproj"
	fi
}

# 环境检查
function check_env
{
	echo "👉  检查运行环境..."
	check_brew
	check_fauxpas
    updatelicense
	installcli
	install_xcodeproj
	echo "【检查运行环境完毕】"
}

function check_project
{
	# todo 自定义规则等参数
	fauxpas check $1
}

check_env
get_xcodeproj_path
