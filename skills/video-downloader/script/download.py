import os
import sys
import subprocess
import re

def check_cookies():
    """检查是否有可用的cookies文件"""
    # 检查常见的cookies文件位置
    possible_paths = [
        os.path.join(os.getcwd(), "cookies.txt"),
        os.path.join(os.path.expanduser("~"), "cookies.txt"),
        os.path.join(os.path.expanduser("~"), ".yt-dlp", "cookies.txt"),
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return path

    return None

def get_available_formats(url, cookies_path=None):
    """获取所有可用的视频格式"""
    cmd = ["yt-dlp", "--list-formats", url]

    if cookies_path:
        cmd.extend(["--cookies", cookies_path])

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"获取格式列表失败: {result.stderr}")
        return None

    return result.stdout

def parse_formats(output):
    """解析yt-dlp输出的格式列表"""
    formats = []
    lines = output.split('\n')

    # 找到格式列表的开始（通常是包含ID的行之后）
    in_format_section = False
    for line in lines:
        # 跳过空行和标题行
        if not line.strip() or 'Available formats' in line or line.startswith('─'):
            continue

        # 解析格式行
        # 格式: ID EXT RESOLUTION FPS │ FILESIZE TBR PROTO │ VCODEC VBR ACODEC ABR
        parts = line.split('│')
        if len(parts) >= 2:
            # 提取ID和分辨率信息
            id_part = parts[0].strip().split()[0] if parts[0].strip() else ''

            # 提取分辨率
            resolution_match = re.search(r'(\d+x\d+|audio only)', line)
            resolution = resolution_match.group(1) if resolution_match else 'unknown'

            # 提取文件大小
            size_match = re.search(r'≈?\s*(\d+\.?\d*\s*(MiB|GiB|KiB))', line)
            filesize = size_match.group(1) if size_match else 'unknown'

            # 提取codec信息
            codec_match = re.search(r'(avc1|hev1|av01|mp4a)', line)
            codec = codec_match.group(1) if codec_match else ''

            if id_part and id_part not in ['ID', '─']:
                formats.append({
                    'id': id_part,
                    'resolution': resolution,
                    'filesize': filesize,
                    'codec': codec,
                    'raw_line': line.strip()
                })

    return formats

def select_format(formats):
    """让用户选择视频格式"""
    print("\n" + "="*80)
    print("可用的视频格式:")
    print("="*80)

    # 分类显示
    video_formats = []
    audio_formats = []

    for i, fmt in enumerate(formats):
        if fmt['resolution'] == 'audio only':
            audio_formats.append((i, fmt))
        else:
            video_formats.append((i, fmt))

    # 显示视频格式
    print("\n【视频格式】")
    print(f"{'序号':<6}{'ID':<10}{'分辨率':<15}{'大小':<12}{'编码':<10}")
    print("-"*60)

    for idx, fmt in video_formats:
        print(f"{idx+1:<6}{fmt['id']:<10}{fmt['resolution']:<15}{fmt['filesize']:<12}{fmt['codec']:<10}")

    # 显示音频格式
    print("\n【音频格式】")
    print(f"{'序号':<6}{'ID':<10}{'类型':<15}{'大小':<12}{'编码':<10}")
    print("-"*60)

    for idx, fmt in audio_formats:
        print(f"{idx+1:<6}{fmt['id']:<10}{'audio only':<15}{fmt['filesize']:<12}{fmt['codec']:<10}")

    # 推荐选项
    print("\n" + "="*80)
    print("推荐选项:")
    print("  [b] 最佳质量 (bestvideo+bestaudio)")
    print("  [w] 最佳1080P (通常推荐)")
    print("  [a] 仅音频")
    print("="*80)

    while True:
        choice = input("\n请选择格式 (输入序号或b/w/a): ").strip().lower()

        if choice == 'b':
            return "bestvideo+bestaudio/best"
        elif choice == 'w':
            # 尝试找到1080P
            for idx, fmt in video_formats:
                if '1080' in fmt['resolution']:
                    # 找到对应的音频格式
                    best_audio = audio_formats[-1][1]['id'] if audio_formats else 'bestaudio'
                    return f"{fmt['id']}+{best_audio}"
            return "bestvideo+bestaudio/best"
        elif choice == 'a':
            return "bestaudio"
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(formats):
                    selected = formats[idx]
                    if selected['resolution'] == 'audio only':
                        return selected['id']
                    else:
                        # 视频需要配合音频
                        best_audio = audio_formats[-1][1]['id'] if audio_formats else 'bestaudio'
                        return f"{selected['id']}+{best_audio}"
            except ValueError:
                pass

        print("无效选择，请重试")

def download_video(url, output_dir=None, format_id=None, cookies_path=None):
    """下载视频"""
    if output_dir is None:
        output_dir = os.getcwd()
    else:
        os.makedirs(output_dir, exist_ok=True)

    os.chdir(output_dir)

    cmd = [
        "yt-dlp",
        "-f", format_id if format_id else "bestvideo+bestaudio/best",
        "--merge-output-format", "mp4",
        "-o", "%(title)s.%(ext)s",
        url
    ]

    if cookies_path:
        cmd.extend(["--cookies", cookies_path])

    print(f"\n正在下载视频到: {output_dir}")
    print(f"使用格式: {format_id}")
    if cookies_path:
        print(f"使用cookies: {cookies_path}")

    subprocess.run(cmd, check=True)
    print("下载完成!")

def main():
    if len(sys.argv) < 2:
        print("Usage: python download.py <video_url> [output_dir]")
        sys.exit(1)

    video_url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    # 检查cookies
    cookies_path = check_cookies()

    if not cookies_path:
        print("\n" + "!"*80)
        print("警告: 未找到cookies文件")
        print("!"*80)
        print("\n对于Bilibili会员视频，需要cookies才能下载高清版本。")
        print("\n如何获取cookies:")
        print("1. 安装浏览器插件: Get cookies.txt LOCALLY")
        print("2. 打开B站并登录你的账号")
        print("3. 点击插件导出cookies，保存为 cookies.txt")
        print("4. 将 cookies.txt 放到当前目录")
        print("\n是否继续下载? (y/n): ", end="")

        choice = input().strip().lower()
        if choice != 'y':
            print("已取消下载")
            sys.exit(0)

        print("\n将以无cookies模式继续，可能只能下载低质量版本...\n")

    # 获取可用格式
    print("正在获取可用格式列表...")
    format_output = get_available_formats(video_url, cookies_path)

    if not format_output:
        print("无法获取格式列表，将使用默认设置下载")
        download_video(video_url, output_dir, cookies_path=cookies_path)
        return

    # 解析格式
    formats = parse_formats(format_output)

    if not formats:
        print("无法解析格式列表，将使用默认设置下载")
        download_video(video_url, output_dir, cookies_path=cookies_path)
        return

    # 让用户选择格式
    format_id = select_format(formats)

    # 下载
    download_video(video_url, output_dir, format_id, cookies_path)

if __name__ == "__main__":
    main()
