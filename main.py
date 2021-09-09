# playing yt selected video
from selenium import webdriver
import time
import random

# list of video to be played
# paste the url of the videos
video_list =[
    "https://www.youtube.com/watch?v=ci_driJKHD0",
    "https://www.youtube.com/watch?v=S52MgFVHAa0",
    "https://www.youtube.com/watch?v=imTEj1AT3vI",
    "https://www.youtube.com/watch?v=_jQlqbsikbc",
    "https://www.youtube.com/watch?v=zUamPtdFcK4",
    "https://www.youtube.com/watch?v=kvTeWKT620k",
    "https://www.youtube.com/watch?v=aeQXdjnBVg4"
]


def plays(count):
    # change the driver PATH
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    # change the second index of the below variable accroding ur array length
    random_video_index = random.randint(0, 7)
    video_url = video_list[random_video_index]
    driver.get(video_url)
    try:
        with open("video_played.txt","a") as f:
            f.write(f"Video No: {count+1}, Title: {driver.title}, URL: {video_url} \n")
    except Exception as e:
        print("Error: ", e)
    video_id = driver.find_element_by_id("ytd-player")
    video_id.click()
    sleep_time = time.sleep(random.randint(40,120))
    driver.quit()

    
if __name__=="__main__":
    # change the variable for looping the process
    play_for = 2
    for i in range(play_for):
        plays(i)
        sleep_time=random.randint(5, 20)
        time.sleep(sleep_time)









