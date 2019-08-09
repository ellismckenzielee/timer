import time
import os
import pygame

### Get the folder path containing alarm sound
dir_path = os.path.dirname(os.path.realpath(__file__)) + '/AlarmSounds/'

class timer():
    '''Timer class creates a timer which accepts the number of hours,
    minutes and seconds, before starting the countdown process'''
    def __init__(self):
        self.hours = int(input('Hours: '))
        self.minutes = int(input('Minutes: '))
        self.seconds = int(input('Seconds: '))
        self.sound = input('Which alarm would you like?\n1: Dog\n2: Alarm Clock\n3: Bell\nPlease Enter a number!: ')
        self.soundcheck()
        self.start()
    
    def soundcheck(self):
        '''Soundcheck checks that the input number is valid, and if not,
        prompts the user to pick again'''
        while self.sound not in ['1','2','3']:
            print('\nPlease enter a number between 1 and 3!')
            self.sound = input('Which alarm would you like?\n1: Dog\n2: Alarm Clock\n3: Bell\nPlease Enter a number!: ')
        self.sound = int(self.sound)
    
    def clear(self):
        '''Clear allows the screen to be cleared to show the timer'''
        os.system('clear')

    def start(self):
        '''Start method calculates the total time in seconds and then waits
        for 0.1 seconds at a time, until the elapsed time exceeds the total time'''
        total_time = (self.hours*60*60) + (self.minutes*60) + self.seconds 
        start_time = time.time()
        elapsed_time = time.time() - start_time
        time_remaining = total_time
        while elapsed_time < total_time:
            time.sleep(0.5)
            elapsed_time = time.time() - start_time

            if time_remaining != int((total_time - elapsed_time)):
                self.clear()
                time_remaining = int((total_time - elapsed_time))
                print('Time remaining: {}s'.format(int(time_remaining)))

        sounds = {1: 'dog',
                  2: 'alarm_clock',
                  3: 'bell'
                 }

        ###Pygame library is used to play the alarm sound
        pygame.init()
        pygame.mixer.music.load(dir_path + sounds[self.sound] + '.mp3')
        pygame.mixer.music.play()

        ###Alarm plays for 10 seconds
        time.sleep(10)

          
if __name__ == "__main__":
    timer = timer()