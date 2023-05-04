import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + (duration * 60)
    
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes, seconds = divmod(remaining_time, 60)
        timer = f"{minutes:02d}:{seconds:02d}"
        print(f"Remaining time: {timer}", end="\r")
        time.sleep(0.1)
    
    print("Time's up!")
