# ICleaner
Boost your computers performance.
----

This Python script automates various optimization tasks on Windows machines. It cleans up disk space, modifies registry keys, flushes DNS cache, runs system file checker, removes temporary files, and more.

## Prerequisites

- Python 3.x installed on your machine.
- Administrator privileges (required to modify registry keys and execute certain commands).

## Usage

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the downloaded repository's directory.

3. Run the following command to execute the script:

   ```shell
   python windows_optimization_pack.py
   ```
   
The script will start performing various optimization tasks automatically.

# Customization

You can customize the script by modifying the code according to your specific requirements. Here are some parts you can consider changing:
- Cleaning Tasks: If you want to exclude or include specific cleaning tasks, you can comment out or remove the corresponding lines of code.

- Registry Keys: The script modifies specific registry keys to clean up disk space. If you want to change the keys or add new ones, you can modify the code in the "Modify registry keys to clean up disk space" section.

- Software-specific Cleaning: The script includes some software-specific cleaning tasks for programs like Escape From Tarkov and Call of Duty. If you want to add or remove cleaning tasks for other software, you can modify the main() function accordingly.

- Windows Tweaks: The script includes a section for performing Windows tweaks related to services. If you want to customize or add more tweaks, you can modify the WindowsTweaks_Services() function.

  # Note

- Caution: Modifying the registry and performing system operations can have unintended consequences. Ensure you have a backup or system restore point before running the script.

- The script is provided as-is without any warranty. Use it at your own risk.
