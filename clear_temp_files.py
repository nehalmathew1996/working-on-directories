import os

def clear_temp_files():
    folders=['static_audio_extract/','variable_audio_extract/']

    for temp_folder in folders:
      
        # Getting all files in this directory
        temp=os.listdir(temp_folder)
        print(temp)
  
        # Removing the files
        for file_name in temp:
            os.remove(temp_folder+file_name)
