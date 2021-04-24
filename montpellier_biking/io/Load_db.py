from montpellier_biking.io import url_db, C_names
import os
import wget
import pandas as pd
import datetime


class Load_db:
    """Download jsons files and fix them to be opened as DFs

    """
    count_str_list = ["Albert 1er",
                      "Beracasa",
                      "Celleneuve",
                      "Delmas 1",
                      "Delmas 2",
                      "Gerhardt",
                      "Lattes 1",
                      "Lattes 2",
                      "Laverune",
                      "Vieille-Poste"]

    def __init__(self, urls=url_db, name=C_names):
        """Download jsons files and fix them to be opened as DFs

        :param urls: 
        :param name: list of counters's name
        """
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

    def save_as_df(name):
        """Open json as a dataframe
        
        :param name: name of the counter
        :type name: string
        :return: dataframe
        
        """
        path_target2 = os.path.join(os.path.dirname(
                                    os.path.realpath(__file__)),
                                    "..", "data/compteurs", name+".json")
        df_bikes = pd.read_json(path_target2, lines=True)
        df = pd.DataFrame()
        df[name] = df_bikes['intensity']
        df = df.iloc[18:, :]
        df.index = pd.date_range(datetime.date(2021, 1, 4),
                                 periods=len(df))
        return df

    def set_df(self):
        """Give a dataframe with all counters, mean, weekday, and week
        """
        # Concat every counter's dataframe
        df_list = []
        for stri in self.count_str_list:
            df_list.append(self.save_as_df(stri))
        data_total = pd.DataFrame()
        for i in range(len(df_list)):
            if i == 3 or i == 6:
                df_list[i][self.count_str_list[i]] += df_list[i+1][
                                                 self.count_str_list[i+1]]
            if i != 7 and i != 4:
                data_total[self.count_str_list[i]] = df_list[i][
                                                     self.count_str_list[i]]
        data_total = data_total.dropna()
        # add mean, weekday, and week to the df
        data_total['mean'] = data_total.mean(axis=1)
        data_total['weekday'] = data_total.index.weekday
        data_total['week'] = data_total.index.week
        return data_total

    # @staticmethod
    # def df_hist_plot_total(df):
        
