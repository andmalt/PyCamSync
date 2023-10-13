from datetime import datetime
import os
import zipfile



def zip_video(config,video_path,video_filename):
    folder = str(config["FOLDERS"]["DIR"])
    directory_path = os.path.join(folder, "Compressed")
    date = datetime.now()
    formatted_data = date.strftime("%Y-%m-%d_%H-%M-%S-%f")
    zip_filename  =  f"video_{formatted_data}.zip"
    zip_path = os.path.join(directory_path,zip_filename)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Aggiungi il file AVI al file zip
        zipf.write(video_path, arcname=video_filename)
        os.remove(video_path)
        print("The file has been successfully compressed\n")