import os
import subprocess
import re


def get_terminal():
    def get_ppid(pid):
        try:
            with open(f"/proc/{pid}/status") as f:
                for line in f:
                    if line.startswith("PPid:"):
                        return int(line.split()[1].strip())
        except FileNotFoundError:
            return None
        return None

    def get_name(pid):
        try:
            with open(f"/proc/{pid}/comm") as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    current_pid = os.getpid()
    ignore_list = [
        "bash",
        "zsh",
        "fish",
        "sh",
        "dash",
        "tmux",
        "tmux: server",
        "screen",
        "su",
        "sudo",
    ]

    while current_pid:
        ppid = get_ppid(current_pid)
        if not ppid or ppid <= 1:
            break
        name = get_name(ppid)
        if name and name not in ignore_list:
            if "gnome-terminal" in name:
                return "GNOME Terminal"
            if name == "urxvtd":
                return "urxvt"
            return name
        current_pid = ppid

    env = os.environ
    if "KONSOLE_VERSION" in env:
        return "Konsole"
    if "ALACRITTY_WINDOW_ID" in env:
        return "Alacritty"
    if "KITTY_WINDOW_ID" in env:
        return "Kitty"
    if "TERM_PROGRAM" in env:
        return env["TERM_PROGRAM"]
    return "Unknown Terminal"


def get_shell():
    python_pid = os.getpid()
    shell_pid = None

    with open(f"/proc/{python_pid}/status") as f:
        content = f.read()

    for line in content.split("\n"):
        if line.startswith("PPid:"):
            shell_pid = line.split()[1]

    with open(f"/proc/{shell_pid}/comm") as f:
        return f.read().strip()


def get_cpu():
    with open("/proc/cpuinfo") as f:
        content = f.read().splitlines()
    cpu_name = "Unknown"
    for line in content:
        if line.startswith("model name"):
            cpu_name = line.split(":")[1].strip()
            break
    cpu_name = re.sub(r"\(R\)|\(TM\)|Core|Processor|(\d+th Gen)", "", cpu_name)
    cpu_name = " ".join(cpu_name.split())
    return cpu_name


def get_gpu():
    result = subprocess.run(
        'lspci | grep -E "VGA|3D|Display"', capture_output=True, text=True, shell=True
    ).stdout.strip()
    gpus = []
    for line in result.split("\n"):
        match = re.search(r"\[(.*?)\]", line)
        if match:
            gpus.append(match.group(1))
    if not gpus:
        return ["Unknown GPU"]
    return gpus


def get_memory():
    memory_gb = None

    with open("/proc/meminfo") as f:
        content = f.read().splitlines()

    for line in content:
        if line.startswith("MemTotal"):
            memory_kb = line.split(":")[1].replace("kB", "").strip()
            memory_gb = round(int(memory_kb) / (1024 * 1024))
    return f"{memory_gb}GB"


def collect():
    shell = get_shell()
    kernel = os.uname().release
    desktop_environment = os.environ.get("XDG_CURRENT_DESKTOP")
    session_type = os.environ.get("XDG_SESSION_TYPE")
    terminal = get_terminal()
    cpu = get_cpu()
    gpu = get_gpu()
    memory = get_memory()
    return {
        "Shell": shell,
        "Kernel": kernel,
        "Desktop Environment": desktop_environment,
        "Session Type": session_type,
        "Terminal": terminal,
        "CPU": cpu,
        "GPU": gpu,
        "Memory": memory,
    }
