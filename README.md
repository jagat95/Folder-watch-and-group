# Folder-watch-and-group
This script can watch a folder and move the files within that into separate folders grouped by file name pattern match

Can be used to 
### Move gamebar screenshots to separate folder location

Mainly my use case was to look at game bar screenshots folder and move the files based upon game names into separate respective folders.

Example: 
- Mortal Kombat™ 11 6_18_2023 1_20_21 PM.png -> Mortal Kombat™ 11/*
- Cyberpunk 2077 (C) 2020 by CD Projekt RED 12_2_2023 12_58_01 AM.png -> Cyberpunk 2077 (C) 2020 by CD Projekt RED/*
- Overwatch 2023-04-17 00-33-48.mp4 -> Overwatch/*
- [Stray]   3_19_2023 3_36_19 PM -> [Stray]/*


## Automate

##### To add the script to Windows Task Scheduler, follow these steps:
1. **Open Task Scheduler:**
   - Press `Win + S` to open the Windows search bar.
   - Type "Task Scheduler" and press `Enter` to open it.

2. **Create a New Task:**
   - In the Task Scheduler, right-click on "Task Scheduler Library" in the left pane.
   - Choose "Create Basic Task..." from the context menu.

3. **Name and Description:**
   - Provide a name and description for your task.
   - Click "Next."

4. **Trigger:**
   - Choose the trigger for your task. You can set it to run daily, weekly, or on a specific event.
   - Click "Next."

5. **Action:**
   - Choose "Start a program" as the action.
   - Click "Next."

6. **Program/Script:**
   - Browse and select the Python executable. It might be located in a path like `C:\Python39\python.exe`. Make sure to adjust this path based on your Python installation.
   -  In the "Add arguments (optional)" field, enter the full path to your script, for example, `C:\path\to\your\script.py`.
   -  **Add the folder paths** as command-line arguments, for example, `C:\path\to\folder_to_watch C:\path\to\folder_to_write`.
   - Click "Next."

7. **Summary:**
   - Review your settings and click "Finish."

8. **Optional: Adjust Settings:**
   - You might want to adjust some settings like running the task with highest privileges or configuring conditions on the "Conditions" tab based on your requirements.

9. **Finish:**
   - Click "OK" to create the task.

Now, your script will run according to the schedule you've set. You may be prompted to enter your Windows user account password during the process.

> Make sure that Python is in your system's PATH or provide the full path to the Python executable in the "Program/Script" field.

> Please note that the Python environment used by the Task Scheduler should have all the necessary dependencies installed (e.g., `watchdog` module). You might need to adjust the Python script and the scheduled task settings accordingly.

> Make sure that Python is in your system's PATH or provide the full path to the Python executable in the "Program/Script" field.

> Please note that the Python environment used by the Task Scheduler should have all the necessary dependencies installed (e.g., watchdog module). You might need to adjust the Python script and the scheduled task settings accordingly.
