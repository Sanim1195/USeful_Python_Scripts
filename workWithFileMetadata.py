import os
import mutagen

#from a specific os path :
# i) Loop through all the folders and sub folders
# ii) if length is less than 1 minute insert it's path to a list
    # dirpath: The current directory path.
    # dirnames: A list of subdirectories in the current directory.
    # filenames: A list of file names in the current directory.
    # # instatiating a list to store the path of songs that is less than 10 sec or less.
music_list = []
def find_shortened_music(music_folder):
    """ This function helps to find music that is compressed and shortened by i-Tunes 
        It traverses a folder using os.walk and returns all the music that is less than 
        10 sec in that main music folder and stores it in a list
    """
    counter = 0
    for dirpath, dirnames,filenames in os.walk(music_folder):
        # print(f"The dirnames is {filenames}")
        # Exclude desktop.ini
        filenames = [f for f in filenames if f.lower() != 'desktop.ini']
        for filename in filenames:
            print(f"The filenames is {filename}")
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
                    fixed_file_name = filename.replace(" 1","")
                    # new_audio_path =os.path.join(dirpath,fixing_file_name)
                music_list.append(fixed_file_name)

                    # add name to list
                    # remove file os.remove(path)
                    # copy that file from anoter music folder and save it to a specific location
            counter += 1


    # print("The number of songs in the music directory is: ",  counter)
    # print("The length of music to be moved is:", len(music_list))
    # print("Music List ", music_list)
    # rename(music_list)



def rename(music_to_rename_list):
    for songs in music_to_rename_list:

        # os.rename()
        print(songs)


# path_to_music_folder = r"C:\Users\pokhr\Music\iTunes\iTunes Media\Music"
path_to_music_folder = r"C:\Users\pokhr\Music\iTunes\iTunes Media\Music\1974 A.D\1974"

find_shortened_music(path_to_music_folder)


# def traverse_dir(music_folder):
#     for dirpath, dirnames,filenames in os.walk(music_folder):
#         # print(f"The dirnames is {filenames}")
#         # Exclude desktop.ini
#         filenames = [f for f in filenames if f.lower() != 'desktop.ini']
#         for filename in filenames:
#             print(f"The filenames is {filename}")
#             path_to_music = os.path.join(dirpath,filename)
#             print(f"The path for the above music is {path_to_music}")
#             # storing the audio info as an object to a variable
#             audio_info = mutagen.File(path_to_music)
#             # getting the length of the audio file
#             audio_duration= audio_info.info.length
#             # The colon (:) after audio_duration allows you to specify formatting options for the value that follows it
#             print(f"Duration: {audio_duration:.0f} seconds")
#             # .mime gives the information about audio file and [0] is for teh type of audio file.
#             print(f"The audio type is: {audio_info.mime[0]}", "\n")
#     return 



