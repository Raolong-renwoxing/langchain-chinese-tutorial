---
name: "video-downloader"
description: "下载 YouTube/Bilibili 视频到本地，支持会员视频和多种质量选择。当用户请求下载 YouTube 或 Bilibili 视频时调用。"
---

# 视频下载器

使用 yt-dlp 下载 YouTube 和 Bilibili 视频到本地目录。支持会员视频下载和多种视频质量选择。

## 使用方法

当用户请求下载 YouTube 或 Bilibili 视频时：

1. 询问用户视频保存位置（若未指定则使用当前目录）
2. 直接调用 skill script 脚本进行下载

### 命令格式：
```
python <skill_script_path> <video_url> [output_dir]
```

## 功能特性

### 1. 自动检测 Cookies
- 自动检查当前目录、用户目录等位置的 `cookies.txt` 文件
- 对于Bilibili会员视频，cookies可解锁高清/高码率版本

### 2. 视频质量选择
脚本会列出所有可用格式，包括：
- 视频格式：360P、480P、720P、1080P、4K等
- 音频格式：不同码率的音频
- 编码格式：AVC (H.264)、HEVC (H.265)、AV1等
- 预估文件大小

用户可选择：
- 输入序号选择特定格式
- `b` - 最佳质量
- `w` - 最佳1080P（推荐）
- `a` - 仅音频

### 3. 智能提示
- 无cookies时提醒用户如何获取
- 显示每个格式的详细信息帮助决策

## 获取 Cookies（Bilibili会员视频必需）

1. 安装浏览器插件：**Get cookies.txt LOCALLY**
2. 打开B站并登录你的账号
3. 点击插件导出cookies，保存为 `cookies.txt`
4. 将 `cookies.txt` 放到下载目录

## 示例

- 用户说："帮我下载这个 youtube 视频"
- 用户说："下载 b 站视频"
- 用户说："把这个 YouTube 视频存到本地"
- 用户说："保存到当前目录"

## 支持平台

- YouTube (youtube.com, youtu.be)
- Bilibili (bilibili.com, b23.tv)

## 注意事项

- 需要安装 yt-dlp：`pip install yt-dlp`
- 视频+音频自动合并为 mp4
- 会员视频需要cookies才能下载高清版本
- 如下载失败，请检查视频是否受地区限制或为私密视频
