import os
import wget
import pandas as pd
import datetime
import requests

im_lt = ['https://i.imgur.com/Ri5aJyp.png', 'https://i.imgur.com/YAIja1z.png',
         'https://i.imgur.com/wZfS6sA.png', 'https://i.imgur.com/OLToKCn.png',
         'https://i.imgur.com/q2V5mJY.png', 'https://i.imgur.com/UAUXZTk.png',
         'https://i.imgur.com/geI3iyA.png', 'https://i.imgur.com/UIfmn0K.png',
         'https://i.imgur.com/UF79hvY.png', 'https://i.imgur.com/Mg883zr.png',
         'https://i.imgur.com/9psMnSH.png', 'https://i.imgur.com/Dt0bUao.png',
         'https://i.imgur.com/H7zbdkx.png']


class Load_db:
    """Download jsons files and fix them to be opened as DFs

    """
    url_db = ['https://data.montpellier3m.fr/sites/default/files/ressources/'
              'MMM_EcoCompt_X2H19070220_archive.json',
              'https://data.montpellier3m.fr/sites/default/files/ressources/'
              'MMM_EcoCompt_X2H20042632_archive.json',
              'https://data.montpellier3m.fr/sites/default/files/ressources/'
              'MMM_EcoCompt_X2H20042633_archive.json',
              'https://data.montpellier3m.fr/sites/default/files/ressources/'
              'MMM_EcoCompt_X2H20042634_archive.json',
              'https://data.montpellier3m.fr/sites/default/files/ressources/'
              'MMM_EcoCompt_X2H20042635_archive.json',
              'https://data.montpellier3m.fr/sites/default/files/ressources/'
              'MMM_EcoCompt_X2H20063161_archive.json',
              'https://data.montpellier3m.fr/sites/default/files/ressources/'
              'MMM_EcoCompt_X2H20063162_archive.json',
              'https://data.montpellier3m.fr/sites/default/files/ressources/'
              'MMM_EcoCompt_XTH19101158_archive.json',
              'https://data.montpellier3m.fr/sites/default/files/ressources/'
              'MMM_EcoCompt_X2H20063163_archive.json',
              'https://data.montpellier3m.fr/sites/default/files/ressources/'
              'MMM_EcoCompt_X2H20063164_archive.json']

    C_names = ['Beracasa', 'Laverune', 'Celleneuve', 'Lattes 2', 'Lattes 1',
               'Vieille-Poste', 'Gerhardt', 'Albert 1er', 'Delmas 1',
               'Delmas 2']

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

        :param urls: url list of datasets
        :param name: list of counters's name
        """
        i = 0
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            "..", "data/")
        if not os.path.exists(path):
            os.makedirs(path)
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            "..", "data/compteurs")
        if not os.path.exists(path):
            os.makedirs(path)
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
            df_list.append(Load_db.save_as_df(stri))
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

    def bikes_list(self, df, week, day):
        """Gives the list of number of bikes passed the day for every counter.

        :param df: dataframe with all counters, mean, weekday,
                 and week (use set_df)
        :param week: int between 1 and 12 the week's number of 2021
        :param day: int, day of the week (ex: 0 means monday)

        :return: number of bikes passed the day for every counter
        :rtype: int list
        """
        temp = df[df['weekday'] == day]
        return list(temp[temp['week'] == week].iloc[0, 0:8])

    def load_images(self, path_im):
        path = path_im
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(13):
            response = requests.get(im_lt[i])
            file = open(path+str(i)+".png", "wb")
            file.write(response.content)
            file.close()
