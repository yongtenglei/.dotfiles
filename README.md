# Rey's dotfiles

## Zsh Config

```bash
stow zsh
```

And then copy zshrc and zimrc to ~/.zshrc ~/.zimrc manually.

## Desktops and Scripts

```bash
stow scripts
stow desktops
```

Scripts locate at `~/.scripts/`, and desktop files at `~/.local/share/applications/`. And you need specify your `username` in desktop scripts.

```desktop
[Desktop Entry]
Name=youtube
Exec=/home/<username>/.scripts/youtube
Type=Application
Terminal=false
Icon=utilities-terminal
```

And then, update your desktop database by

```bash
update-desktop-database ~/.local/share/applications/
```

Now, your wofi/rofi will recognize your desktop files successfully.
