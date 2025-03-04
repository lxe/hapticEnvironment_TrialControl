# HapticEnvironment TrialControl

A Python-based trial management interface for haptic environment experiments. This application provides a graphical interface for controlling and monitoring haptic experiments, including data collection, trial management, and real-time feedback.

## Features

- Graphical user interface for experiment control
- Real-time haptic data streaming and visualization
- Trial management and configuration
- Data logging capabilities (EMG, motion capture)
- MongoDB integration for data storage
- Support for multiple haptic devices
- Configurable experiment states and transitions

## System Requirements

- Windows 10 or later
- Python 3.11
- Haptic device(s) (compatible with the system)
- MongoDB server (for data storage)

## Installation Instructions

1. Install uv:
```powershell
# Install uv using PowerShell
iwr https://astral.sh/uv/install.ps1 -useb | iex

# Add uv to PATH
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
```

2. Create and activate environment:
```powershell
# Create new venv with Python 3.11
uv venv --python 3.11

# Activate venv
.\.venv\Scripts\activate.ps1

# Install dependencies
uv pip install -r requirements.txt
```

## Usage

1. Start the RPC server first (required for communication)
2. Run the application:
```powershell
python taskControl.py
```

3. Configure the experiment:
   - Set subject name
   - Choose save directory
   - Select configuration file
   - Configure recording options (EMG, motion capture)

4. Control the experiment:
   - Start/Stop trials
   - Pause/Resume as needed
   - Monitor real-time data
   - View trial records

## Configuration

The application uses several configuration files:
- `Globals.py`: Network and system settings
- `messageDefinitions.py`: Message protocols
- Trial configuration files in `trialConfig/` directory

## Data Collection

The system supports:
- Haptic data streaming
- EMG data recording
- Motion capture data
- Trial metadata
- MongoDB storage integration

## Troubleshooting

1. Connection Issues:
   - Ensure RPC server is running
   - Check network settings in `Globals.py`
   - Verify firewall settings

2. Virtual Environment Issues:
   - If activation fails, try running PowerShell as administrator
   - Ensure Python is in PATH
   - Try recreating the virtual environment

3. Data Collection Issues:
   - Verify device connections
   - Check MongoDB connection
   - Review log files

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]

## Building Executable

To create a standalone executable (.exe) file:

1. Ensure all dependencies are installed:
```powershell
pip install -r requirements.txt
```

2. Build the executable:
```powershell
pyinstaller taskControl.spec
```

The executable will be created in the `dist` directory as `HapticEnvironment.exe`. This executable includes all necessary dependencies and can be run on any Windows system without requiring Python installation.

Note: The first build might take several minutes as it packages all dependencies.
