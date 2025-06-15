import time
import os
from io import StringIO
import sys

TARGET_FILE = "/app/uploads/light.txt"
cmd_buffer = ""
in_cmd_mode = False
cmd_shell_opened = False
last_executed_command = ""

def execute_command_buffer():
    global cmd_buffer, last_executed_command, cmd_shell_opened
    cmd = cmd_buffer.strip()
    last_executed_command = cmd

    if cmd == "cmd":
        cmd_shell_opened = True
        print("[EXEC] cmd")
    elif cmd == "echo MISSION SUCCESSFUL > C:\\target\\light.txt" and cmd_shell_opened:
        print("[EXEC] 조건 충족: 공격 성공 명령 실행됨")
        with open(TARGET_FILE, 'w') as f:
            f.write("MISSION SUCCESSFUL")
    else:
        print(f"[REJECTED] 허용되지 않은 명령어: {cmd}")
        with open(TARGET_FILE, 'w') as f:
            f.write("")
    cmd_buffer = ""

def parse_ducky_script(file_path):
    global cmd_buffer, in_cmd_mode
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    for line in lines:
        print(f"[PARSE] {line}")
        if line.startswith("DELAY"):
            delay = int(line.split()[1]) / 1000
            time.sleep(delay)
        elif line.startswith("GUI"):
            key = line.split()[1].lower()
            if key == "r":
                print("[GUI] Windows + R → 실행창 열림 (시뮬레이션)")
                in_cmd_mode = True
        elif line.startswith("STRING"):
            input_str = line[len("STRING "):]
            if in_cmd_mode:
                cmd_buffer += input_str + " "
                print(f"[TYPE] '{input_str}' 입력됨 (버퍼 누적)")
            else:
                print(f"[TYPE] '{input_str}' 입력됨 (명령 모드 아님)")
        elif line == "ENTER":
            if in_cmd_mode:
                print("[ENTER] → 명령 실행")
                execute_command_buffer()
            else:
                print("[ENTER] → 무시됨 (명령 모드 아님)")

def run_emulator(file_path):
    global last_executed_command
    buffer = StringIO()
    original_stdout = sys.stdout
    sys.stdout = buffer
    try:
        parse_ducky_script(file_path)
        success = (last_executed_command == "echo MISSION SUCCESSFUL > C:\\target\\light.txt")
    finally:
        sys.stdout = original_stdout
    return success, buffer.getvalue()