# 🍚📸 rice-snap

Generate a postcard-style card of your Linux rice and share it with the community! 🐧

<img width="1280" height="720" alt="rice-card" src="https://github.com/user-attachments/assets/d9ac1d77-182a-42d2-99bb-2e41a3dcd016" />

---

## ✨ Features

- Detects system info automatically: shell, kernel, DE, session type, terminal, CPU, GPU, and RAM
- Generates a 1280x720 postcard-style PNG card
- Custom seal and stamp support
- Works on any Linux distro (Arch, CachyOS, Fedora, Ubuntu, Debian and more)

---

## 📦 Requirements

Before installing, make sure you have:

- `python3`
- `python3-pip`
- `python3-venv`

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/rice-snap.git
cd rice-snap
bash install.sh
```

---

## 🖼️ Usage

Take a screenshot of your desktop first, then run:

```bash
rice-snap ~/Pictures/desktop.png
```

The card will be saved to `~/Downloads/rice-card.png`.

### Options

```
rice-snap <image> [options]

positional arguments:
  image                 Path to your desktop screenshot

optional arguments:
  --bg-color HEX        Background color (default: #FFFCED)
  --bg-image PATH       Use image as background instead of solid color
  --text-color HEX      Font color (default: #263A43)
  --decoration-color HEX Accent lines color (default: #C93F2B)
  --seal PATH           Custom seal image (default: built-in white seal)
  --stamp PATH          Custom stamp image (default: built-in stamp)
  --output PATH         Output path (default: ~/Downloads/rice-card.png)
  -h, --help            Show help message
```

### Examples

```bash
# Basic usage
rice-snap ~/Pictures/desktop.png

# Dark theme card
rice-snap ~/Pictures/desktop.png \
  --bg-color "#1a1a2e" \
  --text-color "#eee" \
  --decoration-color "#e94560"

# Custom background image
rice-snap ~/Pictures/desktop.png --bg-image ~/Pictures/wallpaper.jpg

# Custom seal
rice-snap ~/Pictures/desktop.png --seal ~/Pictures/myseal.png

# Custom output path
rice-snap ~/Pictures/desktop.png --output ~/Pictures/rice-card.png
```

---

## 🎨 Customization

### Colors
Use any valid hex color code:

    Cream (default): #FFFCED
    Dark: #1a1a2e with text #eee
    Nord theme: #2e3440 bg, #d8dee9 text, #88c0d0 accent

### Background Image
For best results, use images with 16:9 aspect ratio (1280x720) or similar. The image will be resized to fit.

### Custom seal
The seal is the stamp image in the top-right corner of the card. You can use any PNG with a transparent background. Recommended size: 200x300px

```bash
rice-snap ~/desktop.png --seal ~/my-avatar.png
```

---

## 🗂️ Project Structure

```
rice-snap/
├── assets/
│   ├── seal.png          # default seal
│   └── stamp.png         # default stamp
├── cli.py                # CLI entry point
├── collector.py          # system info collector
├── composer.py           # card generator
├── install.sh            # installer
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Some ideas:

- Add more themes/color schemes for the card
- Improve terminal detection for edge cases
- Add more system info fields

---

## 📜 License

MIT License

---

Made with ☕ and 🐧 by RafaFonPessoa
