import webbrowser

SITES = {
    "1": ("知网", "https://www.cnki.net/"),
    "2": ("百度", "https://www.baidu.com/"),
    "3": ("GitHub", "https://github.com/"),
}

choice = input("请选择网站：")

if choice in SITES:
    name, url = SITES[choice]
    print(f"正在打开{name}...")
    webbrowser.open(url)
else:
    print("无效选择")