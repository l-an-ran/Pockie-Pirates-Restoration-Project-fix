# -*- coding: utf-8 -*-
import subprocess

def stop():
    print("正在查找并停止运行在 8888 端口的游戏服务...")
    try:
        out = subprocess.check_output('netstat -ano | findstr ":8888 " | findstr "LISTENING"', shell=True).decode()
        pids = set()
        for line in out.strip().splitlines():
            parts = line.strip().split()
            if len(parts) >= 5:
                pids.add(parts[-1])
        for pid in pids:
            print(f"正在结束服务端进程 (PID: {pid})...")
            subprocess.call(f"taskkill /F /PID {pid}", shell=True)
        print("服务已成功停止！")
    except Exception:
        print("未发现正在运行的 8080 端口服务。")

if __name__ == '__main__':
    stop()
