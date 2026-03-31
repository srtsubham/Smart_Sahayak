import gateway as g
import interaction as i


def s():
    print("System Initialized. Monitoring for presence...")
    while True:
        if g.m():
            print("User verification complete. Starting interactive mode...")
            i.i()
            print("Session ended. Returning to Idle State.")


if __name__ == "__main__":
    s()
