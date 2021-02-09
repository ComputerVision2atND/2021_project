# Starts data capture from camera for "object" data collection.
# The output file structure will look like this:
#       data_objects/
#       └── T1
#           ├── book
#           │   ├── 1611708112.3133156.jpg
#           │   ├── 1611708237.0503974.jpg
#           │   ├── 1611708237.4386756.jpg
#           │   ├── 1611708237.8493211.jpg
#           │   └── 1611708238.275431.jpg
#           ├── teapot
#           │   ├── 1611708100.66356.jpg
#           │   ├── 1611708250.7956946.jpg
#           │   ├── 1611708251.4162023.jpg
#           │   └── 1611708252.290155.jpg
#           └── wallet
#               ├── 1611708140.0596297.jpg
#               ├── 1611708263.2442229.jpg
#               ├── 1611708263.5862782.jpg
#               └── 1611708263.9512281.jpg
# Usage:

import os
import time
import traceback

# PARAMETERS
DRY_RUN = False             # setting it to True won't create directories or files
VIDEO_DEVICE = 0            # switch camera IDs here (0, 1, ...)
BASE_PATH = 'data_objects'  # base directory where images will be saved
N_TEAMS = 10
N_OBJECTS = 10
# ===========


# check opencv installation if needed
try:
    import cv2
except:
    print("Couldn't import OpenCV. Try installing it first with:\tconda install -c conda-forge opencv")
    exit(1)


def main():
    start_capture()


def save_frame(frame, filepath, fname):

    os.makedirs(filepath, exist_ok=True)
    fullname = str(os.path.join(filepath, fname))
    if DRY_RUN:
        print(" >>> [ DRY-RUN MODE ] Image NOT saved as {}".format(fullname))
    else:
        cv2.imwrite(fullname, frame)
        print(" >>> Image saved as {}".format(fullname))


def capture_image(cap_device, filepath):

    is_success = False
    while (True):

        ret, frame = cap_device.read()
        if ret == 0:
            print("Failed to capture image, try again")
            return is_success

        cv2.imshow('frame', frame)

        # quit capture
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        # save frame to file
        elif key == ord(' '):
            print("\tPress SPACE to save the frame, or another key to redo the capture.")
            key2 = cv2.waitKey(0)
            if key2 == ord(' '):
                try:
                    fname = str(str(time.time()) + ".jpg")
                    save_frame(frame, filepath, fname)
                    is_success = True
                except:
                    print("Error saving frame to disk:")
                    traceback.print_exc()
                    continue
            else:
                continue

    return is_success


def prompt_team_number():

    team_id = None
    while True:
        try:
            team_id = input("Enter your team number [1-{}]\t> ".format(N_TEAMS))
            team_id = int(team_id)
            if 0 < team_id <= N_TEAMS:
                break
        except KeyboardInterrupt:
            print()
            exit(1)
        except:
            pass
        print("Try again")

    team_id = "T" + str(team_id)
    return team_id


def start_capture():

    team_id = prompt_team_number()
    print(" >>> Team ID: {}".format(team_id))

    # create capture
    cap_device = cv2.VideoCapture(VIDEO_DEVICE)

    while True:

        obj_id = input("\n\n >>> Enter a name for this object (alphanum and dashes only)\n\t[Q]uit\t> ")
        if obj_id.lower() == 'q':
            break
        print(" >>> Capturing object '{}'. Press Q to quit capture mode.".format(obj_id))

        filepath = os.path.join(BASE_PATH, team_id, obj_id)
        if not capture_image(cap_device, filepath):
            break

    # release capture
    cap_device.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
