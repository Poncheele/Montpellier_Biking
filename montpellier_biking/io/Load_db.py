from montpellier_biking.io import url_db, C_names
import os
import wget
import pandas as pd


class Load_db:
    """
    Download jsons files and fix them to be opened as DFs
    """
    def __init__(self, urls=url_db, name=C_names):
        i = 0
        for url in urls:
            path_target_txt = os.path.join(os.path.dirname(
                                           os.path.realpath(__file__)),
                                           "..", "data/compteurs", name[i] +
                                           ".txt")
            if os.path.isfile(path_target_txt):
                os.remove(path_target_txt)
            wget.download(url, path_target_txt)
            path_target2 = os.path.join(os.path.dirname(os.path.realpath(
                                        __file__)), "..",
                                        "data/compteurs", name[i]+".json")
            file = open(path_target_txt, "r")
            if os.path.isfile(path_target2):
                os.remove(path_target2)
            newfile = open(path_target2, 'x')
            for line in file:
                newfile.write(line.replace('}{', '}\n{'))
            file.close()
            os.remove(path_target_txt)
            i += 1

    @staticmethod
    def save_as_df(name):
        path_target2 = os.path.join(os.path.dirname(
                                    os.path.realpath(__file__)),
                                    "..", "data/compteurs", name+".json")
        df_bikes = pd.read_json(path_target2, lines=True)
        return df_bikes
