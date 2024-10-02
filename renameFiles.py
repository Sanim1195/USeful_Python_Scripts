import mutagen
import os

path_to_song1 = r"C:\Test Music"

for dirpath, dirnames,filenames in os.walk(path_to_song1):
        # print(f"The dirnames is {filenames}")
        # Exclude desktop.ini
        filenames = [f for f in filenames if f.lower() != 'desktop.ini']
        for filename in filenames:
            print(f"The filename is {filename}")
            path_to_music = os.path.join(dirpath,filename)
            print(f"The path for the above music is {path_to_music}")
            # storing the audio info as an object to a variable
            audio_info = mutagen.File(path_to_music)
            # getting the length of the audio file
            audio_duration= audio_info.info.length
            # The colon (:) after audio_duration allows you to specify formatting options for the value that follows it
            print(f"Duration: {audio_duration:.0f} seconds")
            # .mime gives the information about audio file and [0] is for teh type of audio file.
            print(f"The audio type is: {audio_info.mime[0]}", "\n")

            # @TO DO: def check_and_insert():
            # Check if song is less than or equal to 10 seconds
            # check the audio format -> If format is .flac convert to mp3/mp4
            # Store the path of music to list when above is true
            # check_and_insert(audio_duration, path )
            if audio_duration <= 10:
                if " 1" in filename:
                    print("Found a 1")
                    fixing_file_name = filename.replace(" 1","")
                    new_audio_path =os.path.join(dirpath,fixing_file_name)
                    os.rename(path_to_music,new_audio_path )
                # add name to list
                # remove file os.remove(path)
                # copy that file from anoter music folder and save it to a specific location

# audio_info = mutagen.File(path_to_song1)
# b = a.replace("1", "")
# b = b.replace(" ", "")
# print(b.strip())