import time
import os
from pynput import keyboard, mouse

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

delay = 0.1  # Delay between moving to different positions
delay_before_click = 0.1  # Delay before clicking at each position
pause_duration = 180  # Time between runs
check_interval = 0.1  # Interval for checking stop_execution flag

positions = []
stop_execution = False
total_clicks = 0
clicks_per_position = []

def on_press(key):
    global recording, stop_execution
    if key == keyboard.Key.enter:
        recording = False
        return False
    elif key == keyboard.KeyCode.from_char('x'):
        current_pos = mouse_controller.position
        positions.append(current_pos)
        clicks_per_position.append(0)  # Initialize clicks count for this position
        print(f"Recorded position: {current_pos}")
    elif key == keyboard.Key.esc:
        stop_execution = True
        return False

mouse_controller = mouse.Controller()

recording = True
print("Press X to record positions.\nPress 'Enter' to finish recording.")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

with keyboard.Listener(on_press=on_press) as listener:
    while not stop_execution:
        for idx, pos in enumerate(positions):
            if stop_execution:
                break
            mouse_controller.position = pos
            
            for _ in range(int(delay_before_click / check_interval)):
                if stop_execution:
                    break
                time.sleep(check_interval)
            if stop_execution:
                break
            mouse_controller.click(mouse.Button.left, 1)
            
            total_clicks += 1
            clicks_per_position[idx] += 1
            clear_console()
            print(f"Total Clicks: {total_clicks}")
            print(f"Clicks Per Account: {clicks_per_position}")
            
            for _ in range(int(delay / check_interval)):
                if stop_execution:
                    break
                time.sleep(check_interval)
        
        if not stop_execution:
            for _ in range(int(pause_duration / check_interval)):
                if stop_execution:
                    break
                time.sleep(check_interval)

print("Execution finished.")
