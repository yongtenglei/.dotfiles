# Maple-Mono-Font(+ss07;+ss08;+zero;+cv61;+ss11;+calt;)

Built from [maple-font](https://github.com/subframe7536/maple-font).

## config.json

```json
{
  "family_name": "Maple Mono",
  "use_hinted": false,
  "pool_size": 4,
  "enable_ligature": true,
  "ttfautohint_param": {},
  "feature_freeze": {
    "cv01": "ignore",
    "cv02": "ignore",
    "cv03": "ignore",
    "cv04": "ignore",
    "cv05": "ignore",
    "cv06": "ignore",
    "cv07": "ignore",
    "cv08": "ignore",
    "cv31": "ignore",
    "cv32": "ignore",
    "cv33": "ignore",
    "cv34": "ignore",
    "cv35": "ignore",
    "cv36": "ignore",
    "cv37": "ignore",
    "cv38": "ignore",
    "cv39": "ignore",
    "cv40": "ignore",
    "cv41": "ignore",
    "cv61": "enable",
    "cv62": "ignore",
    "cv63": "ignore",
    "cv64": "ignore",
    "cv65": "ignore",
    "cv96": "ignore",
    "cv97": "ignore",
    "cv98": "ignore",
    "cv99": "ignore",
    "ss01": "ignore",
    "ss02": "ignore",
    "ss03": "ignore",
    "ss04": "ignore",
    "ss05": "ignore",
    "ss06": "ignore",
    "ss07": "enable",
    "ss08": "enable",
    "ss09": "ignore",
    "ss10": "ignore",
    "ss11": "enable",
    "zero": "enable"
  },
  "nerd_font": {
    "enable": true,
    "version": "3.4.0",
    "mono": false,
    "use_font_patcher": false,
    "glyphs": [
      "--complete"
    ],
    "extra_args": []
  },
  "cn": {
    "enable": true,
    "with_nerd_font": true,
    "fix_meta_table": true,
    "clean_cache": false,
    "narrow": false,
    "use_hinted": false,
    "use_static_base_font": true,
    "scale_factor": 1.0
  }
}
```

## building args

```bash
--cn --no-hinted --feat ss07,ss08,ss11,zero,cv61
```

## Usage

```bash
cd ~/.dotfiles/fonts
stow -t ~/.local maple
fc-cache -fv
```
