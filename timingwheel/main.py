import timingwheel
import logging

def main():
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        t = timingwheel.TimingWheel()
        t.start_timer()
        t.update_timer()
        t.stop_timer()
        t.initialise(1)

if __name__ == "__main__":
        main()