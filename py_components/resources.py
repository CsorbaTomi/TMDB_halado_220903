from PySide2.QtCore import QObject, Slot, QUrl
import os, requests

RESOURCES_PATH = os.path.dirname(__file__).replace("py_components", "resources")

class Resources(QObject):
    @Slot(str, result=QUrl)
    def get(self, resource_name):
        resource_path = os.path.join(RESOURCES_PATH, resource_name)
        assert os.path.exists(resource_path), f"Resource does not exist: {resource_path}"
        return QUrl().fromLocalFile(resource_path)

def download_poster(url, cache_folder):
    # creat cache_folder if not exists
    if not os.path.exists(cache_folder):
        os.makedirs(cache_folder)
    poster_file_name = url[1:]
    poster_path = os.path.join(cache_folder, poster_file_name)

    if os.path.exists(poster_path):
        return poster_path

    server_url = f"https://image.tmdb.org/t/p/w300{url}"
    #test url response
    assert requests.get(server_url).status_code == 200, f"Bad url {server_url}"

    img_data = requests.get(server_url).content
    with open(poster_path, "wb") as f:
        f.write(img_data)
    return poster_path

if __name__ == "__main__":
    download_poster("/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg", r"/home/csorba/Python_enviroments/pythonsuli/TMDB_halado_220903/resources/tmp")