from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Spotify:
    def start_playing(self):
        print(f"Музыка играет")
    def stop_playing(self):
        print(f"Музыка остановилась")

class StartPlaying(Command):
    def __init__(self, par):
        self.par = par

    def execute(self):
        self.par.start_playing()

class StopPlaying(Command):
    def __init__(self, par):
        self.par = par

    def execute(self):
        self.par.stop_playing()

class AppPlayer():
    def __init__(self):
        self.current_command = None
    def assign_command(self, command):
        self.current_command = command
    def press_button(self):
        if self.current_command:
            self.current_command.execute()

def main():
    s = Spotify()
    app = AppPlayer()
    play_on = StartPlaying(s)
    play_off = StopPlaying(s)
    app.assign_command(play_on)
    app.press_button()
    app.assign_command(play_off) 
    app.press_button()

if __name__ == "__main__":
    main()
