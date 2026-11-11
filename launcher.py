# -*- coding: utf-8 -*-
"""
小小海贼王 (Pockie Pirates) 本地一键启动器
"""
import os
import sys
import time
import subprocess
import urllib.request
import webbrowser

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def find_server_py():
    candidates = [
        os.path.join(SCRIPT_DIR, "Pockie-Pirates-Restoration-Project", "pockiepirates_project", "server_dev", "skeleton"),
        os.path.join(SCRIPT_DIR, "pockiepirates_project", "server_dev", "skeleton"),
        os.path.join(SCRIPT_DIR, "server_dev", "skeleton"),
    ]
    for c in candidates:
        py = os.path.join(c, "server.py")
        if os.path.isfile(py):
            return c, py
    return None, None

SERVER_DIR, SERVER_PY = find_server_py()

# 常用 Flash 浏览器和独立播放器候选路径
FC_BROWSER = r"G:\FlashCenter\FCBrowser.exe"
FC_PLAY = r"G:\FlashCenter\FCPlay.exe"
CENT_EXE = r"D:\CentBrowser\Application\chrome.exe"
FLASH_DLL = r"C:\Windows\System32\Macromed\Flash\pepflashplayer64_34_0_0_380.dll"

def is_server_running():
    try:
        with urllib.request.urlopen("http://127.0.0.1:8888/status", timeout=1) as resp:
            return resp.status == 200
    except Exception:
        return False

def main():
    print("=" * 65)
    print("      ⚓ 小小海贼王 (Pockie Pirates) 本地网页游戏启动器")
    print("=" * 65)
    print()

    # 1. 检查或启动服务端
    if is_server_running():
        print("[1/3] 本地游戏服务端已在运行 (Port 8888)。")
    else:
        print("[1/3] 正在启动本地游戏服务端 (Port 8888)...")
        if not SERVER_PY or not os.path.isfile(SERVER_PY):
            print(f"[错误] 找不到服务端主程序 server.py！搜索路径: {SCRIPT_DIR}")
            input("\n按回车键退出...")
            return

        subprocess.Popen(
            [sys.executable, SERVER_PY],
            cwd=SERVER_DIR,
            creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == 'nt' else 0
        )

        print("[2/3] 等待服务初始化与加载 58 个游戏数据表...")
        ready = False
        for _ in range(20):
            time.sleep(0.5)
            if is_server_running():
                ready = True
                break

        if not ready:
            print("[警告] 服务端启动超时，请检查后台黑框中的提示。")
        else:
            print("      服务端就绪 (HTTP 200 OK)!")

    # 2. 唤起浏览器
    print("[3/3] 正在唤起 Flash 浏览器进入游戏...")
    url = "http://127.0.0.1:8888/"

    if os.path.isfile(FC_BROWSER):
        print(f"      [OK] 发现 FlashCenter 专属浏览器:\n      {FC_BROWSER}")
        print("      正在以 FCBrowser 打开游戏网页...")
        subprocess.Popen([FC_BROWSER, url])
    elif os.path.isfile(CENT_EXE):
        print("      检测到 CentBrowser 百分浏览器，正在以 Flash 模式启动...")
        args = [CENT_EXE]
        if os.path.isfile(FLASH_DLL):
            args.extend([
                "--allow-outdated-plugins",
                f"--ppapi-flash-path={FLASH_DLL}",
                "--ppapi-flash-version=34.0.0.380"
            ])
        args.append(url)
        subprocess.Popen(args)
    else:
        print("      使用默认浏览器打开游戏网页...")
        webbrowser.open(url)

    print()
    print("=" * 65)
    print("  ★ 游戏已启动！")
    print("  - 游戏页面: http://127.0.0.1:8888/")
    print("  - 状态监控: http://127.0.0.1:8888/status")
    print()
    print("  [提示]")
    print("  1. 页面上方可随时切换 [▶️ 官方加载器 (GameLoader)] 或 [⚡ 直连模式 (main)]；")
    print("  2. 如果 FCBrowser 页面仍有异常，也可以直接用 FCPlay 播放器打开:")
    print("     G:\\FlashCenter\\FCPlay.exe http://127.0.0.1:8888/onepiece/main.swf")
    print("=" * 65)
    print()

if __name__ == "__main__":
    main()
