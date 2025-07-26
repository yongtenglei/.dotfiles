config.load_autoconfig()

c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
}
c.url.start_pages = ["about:blank"]
# c.url.start_pages = ["https://www.google.com"]
c.url.default_page = "about:blank"
# c.url.default_page = "https://www.google.com"

c.content.proxy = "http://127.0.0.1:7899"
c.content.blocking.enabled = True

c.auto_save.session = True

c.window.hide_decoration = True
c.window.title_format = "{current_title} - qutebrowser"

# Download the appropriate dictionary using the dictcli.py script that comes bundled with qutebrowser.
# $ ~/.local/qutebrowser/.venv/bin/python ~/.local/qutebrowser/scripts/dictcli.py install en-US
c.spellcheck.languages = ["en-US"]

config.bind(",g", "spawn --userscript quickmark_load.sh github {url}")
config.bind(",m", "spawn --userscript quickmark_load.sh github_me {url}")
config.bind(",y", "spawn --userscript quickmark_load.sh yuanbao {url}")
config.bind(",c", "spawn --userscript quickmark_load.sh chatgpt {url}")
config.bind(",o", "spawn --userscript quickmark_load.sh outlook {url}")
config.bind(",b", "spawn --userscript quickmark_load.sh bilibili {url}")
config.bind(",d", "spawn --userscript quickmark_load.sh discord {url}")

config.bind("<Ctrl-p>", "completion-item-focus --history prev", mode="command")
config.bind("<Ctrl-n>", "completion-item-focus --history next", mode="command")


# ===== Tokyo Night Color Variables =====
TOKYO_NIGHT = {
    # Base colors
    "background": "#1a1b26",
    "foreground": "#c0caf5",
    # Color palette (16-color terminal scheme)
    "black": "#15161e",
    "red": "#f7768e",
    "green": "#9ece6a",
    "yellow": "#e0af68",
    "blue": "#7aa2f7",
    "magenta": "#bb9af7",
    "cyan": "#7dcfff",
    "white": "#a9b1d6",
    # Bright variants
    "bright_black": "#414868",
    "bright_red": "#f7768e",
    "bright_green": "#9ece6a",
    "bright_yellow": "#e0af68",
    "bright_blue": "#7aa2f7",
    "bright_magenta": "#bb9af7",
    "bright_cyan": "#7dcfff",
    "bright_white": "#c0caf5",
}

# ===== Core Settings =====
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = "lightness-cielab"
c.colors.webpage.bg = TOKYO_NIGHT["background"]

# ===== Tab Bar =====
c.colors.tabs.bar.bg = TOKYO_NIGHT["black"]
c.colors.tabs.even.bg = TOKYO_NIGHT["black"]
c.colors.tabs.odd.bg = TOKYO_NIGHT["black"]
c.colors.tabs.selected.even.bg = TOKYO_NIGHT["bright_black"]
c.colors.tabs.selected.odd.bg = TOKYO_NIGHT["bright_black"]
c.colors.tabs.indicator.start = TOKYO_NIGHT["blue"]
c.colors.tabs.indicator.stop = TOKYO_NIGHT["black"]

# ===== Status Bar =====
c.colors.statusbar.normal.bg = TOKYO_NIGHT["black"]
c.colors.statusbar.command.bg = TOKYO_NIGHT["black"]
c.colors.statusbar.url.fg = TOKYO_NIGHT["white"]
c.colors.statusbar.url.hover.fg = TOKYO_NIGHT["blue"]
c.colors.statusbar.url.success.http.fg = TOKYO_NIGHT["blue"]
c.colors.statusbar.url.success.https.fg = TOKYO_NIGHT["green"]
c.colors.statusbar.url.warn.fg = TOKYO_NIGHT["yellow"]

# ===== Hints =====
c.colors.hints.fg = TOKYO_NIGHT["yellow"]
c.colors.hints.bg = TOKYO_NIGHT["black"]
c.colors.hints.match.fg = TOKYO_NIGHT["green"]

# ===== Completion Menu =====
c.colors.completion.category.bg = TOKYO_NIGHT["black"]
c.colors.completion.category.fg = TOKYO_NIGHT["blue"]
c.colors.completion.even.bg = TOKYO_NIGHT["black"]
c.colors.completion.odd.bg = TOKYO_NIGHT["bright_black"]
c.colors.completion.fg = TOKYO_NIGHT["white"]
c.colors.completion.match.fg = TOKYO_NIGHT["green"]
c.colors.completion.scrollbar.bg = TOKYO_NIGHT["black"]
c.colors.completion.scrollbar.fg = TOKYO_NIGHT["bright_black"]

# ===== Downloads =====
c.colors.downloads.bar.bg = TOKYO_NIGHT["black"]
c.colors.downloads.start.fg = TOKYO_NIGHT["blue"]
c.colors.downloads.stop.fg = TOKYO_NIGHT["green"]
c.colors.downloads.error.fg = TOKYO_NIGHT["red"]

# ===== Messages =====
c.colors.messages.error.bg = TOKYO_NIGHT["black"]
c.colors.messages.error.fg = TOKYO_NIGHT["red"]
c.colors.messages.warning.bg = TOKYO_NIGHT["black"]
c.colors.messages.warning.fg = TOKYO_NIGHT["yellow"]
c.colors.messages.info.bg = TOKYO_NIGHT["black"]
c.colors.messages.info.fg = TOKYO_NIGHT["blue"]

# ===== Font Settings =====
c.fonts.default_family = "Maple Mono NF"
c.fonts.default_size = "10pt"

# ===== Webkit Preferences =====
settings = {
    "webkit": {
        "prefers-color-scheme": "dark",
    }
}


# ===== Optional Features =====
# Uncomment to enable:
# c.scrolling.bar = "never"  # Hide scrollbar
# c.content.user_stylesheets = ["~/.config/qutebrowser/tokyo-night.css"]
