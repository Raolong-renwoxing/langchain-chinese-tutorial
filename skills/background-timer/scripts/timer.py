#!/usr/bin/env python3
"""
后台计时器脚本

用法: python timer.py <秒数>

功能:
1. 接收倒计时秒数参数
2. 等待指定时间
3. 生成随机字符（长度 32-64）
4. 在当前工作目录创建文件 random_text_<timestamp>.txt
"""

import sys
import time
import random
import string
from pathlib import Path
from datetime import datetime


def generate_random_text(length=None):
    """生成随机字符文本"""
    if length is None:
        length = random.randint(32, 64)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def main():
    if len(sys.argv) < 2:
        print("Usage: python timer.py <seconds>")
        sys.exit(1)

    try:
        seconds = int(sys.argv[1])
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid integer")
        sys.exit(1)

    if seconds <= 0:
        print("Error: seconds must be positive")
        sys.exit(1)

    print(f"[Timer] Started countdown: {seconds} seconds")
    time.sleep(seconds)

    random_text = generate_random_text()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"random_text_{timestamp}.txt"

    output_path = Path.cwd() / filename
    output_path.write_text(random_text, encoding='utf-8')

    print(f"[Timer] Completed! Created: {output_path}")
    print(f"[Timer] Random text length: {len(random_text)}")


if __name__ == "__main__":
    main()