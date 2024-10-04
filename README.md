# Biblical-Resting-Eyes

A mindful screen break application that encourages regular breaks with Bible verse memorization.

## 📖 About

Bible Break is a Python-based desktop application that helps users maintain healthy screen time habits while strengthening their faith. The application runs in the background and periodically displays a full-screen break reminder with a Bible verse. To resume work, users must correctly type out the displayed verse, promoting both screen breaks and scripture memorization.

### 🌟 Key Features

- **Automatic Break Reminders**: Defaults to 20-minute intervals (customizable)
- **Full-Screen Break Mode**: Ensures users take a proper break
- **Bible Verse Memorization**: Contains 10 carefully selected verses
- **Minimal Resource Usage**: Runs quietly in the background
- **Windows Support**: Built for Windows operating systems

## 🚀 Getting Started

### Prerequisites

- Windows Operating System
- No additional installations required for the executable version

### Installation

#### Option 1: Direct Download (Recommended for Most Users)
1. Go to the [Releases](../../releases) section
2. Download the latest `BibleBreak.exe`
3. Double-click to run the application

#### Option 2: Building from Source
If you want to customize the application or build it yourself, you'll need:
- Python 3.8 or higher
- Required packages: `tkinter` (usually comes with Python)
- PyInstaller (for building the executable)

```bash
# Clone the repository
git clone https://github.com/yourusername/bible-break.git
cd bible-break

# Install PyInstaller
pip install pyinstaller

# Build the executable
python build_script.py
```

### Auto-start Setup

To make Bible Break start automatically with Windows:

1. Press `Win + R`
2. Type `shell:startup`
3. Create a shortcut to `BibleBreak.exe` in this folder

## 🛠️ Configuration

Currently, the following aspects can be modified in the source code:

- Break interval (default: 20 minutes)
- Bible verses collection
- Screen appearance

Future versions may include a configuration file for easier customization.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/bible-break.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install development dependencies
pip install pyinstaller
```

## 🙏 Acknowledgments

- Thanks to [eyes-thanks](https://github.com/yalov/eyes-thanks) for inspiration
- Bible verses from the New International Version (NIV)

## 📝 Version History

- 1.0.0
  - Initial Release
  - Basic break reminder functionality
  - 10 core Bible verses

## 🔮 Future Plans

- [ ] Customizable break intervals
- [ ] User-configurable verse collection
- [ ] Statistics tracking
- [ ] Multiple Bible translations
- [ ] Cross-platform support

---
*"All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness" - 2 Timothy 3:16*
