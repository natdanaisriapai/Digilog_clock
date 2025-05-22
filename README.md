# Digilog Clock

A unique digital-analog hybrid clock application that displays time using a combination of digital numbers and analog-style hands. The clock features a modern design with a clean interface and always stays on top of other windows.

## Features

- Hybrid digital-analog display
- Real-time updates
- Always-on-top window
- Clean, modern interface
- Custom clock icon
- Hour, minute, and second hands with different colors
  - Hour hand: Black
  - Minute hand: Green
  - Second hand: Red

## Requirements

- Python 3.x
- Built-in Python libraries:
  - tkinter
  - math
  - datetime

## Installation

### Option 1: Running from Source Code
1. Clone this repository or download the source code
2. Make sure you have Python 3.x installed on your system
3. Install required packages:
```bash
pip install -r requirements.txt
```
4. Run the program using:
```bash
python clock.py
```

### Option 2: Running as Executable
1. Download the latest release from the releases section
2. Extract the downloaded zip file
3. Double-click `clock.exe` in the extracted folder to run the clock

### Option 3: Building Your Own Executable
If you want to create your own executable:

1. Make sure you have Python 3.x installed
2. Install required packages:
```bash
pip install -r requirements.txt
```
3. Open terminal/command prompt in the project directory
4. Run this single command to create the executable:
```bash
pyinstaller --onefile --icon=clock_icon.ico --noconsole clock.py
```

4. After the build process completes:
   - The executable will be created in the `dist` folder
   - You can find `clock.exe` in the `dist` directory
   - Copy `clock.exe` to any location you want to run it from

Note: 
- The executable version doesn't require Python to be installed on the system where it will run
- If you only want to run the Python code (Option 1), you don't need to install any additional packages as the program uses only built-in Python libraries

## Project Structure

- `clock.py` - Main application code
- `clock_icon.ico` - Application icon
- `requirements.txt` - Project dependencies (empty as only built-in libraries are used)
- `README.md` - This documentation file

## License

This project is open source and available for personal and educational use.

## Author

Created by natdanai_sriapai