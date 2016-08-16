#-*- coding:utf-8 -*-
from tkinter import Tk, filedialog


def handle_folder_dialog():
    Tk().withdraw()
    folder_name = filedialog.askdirectory(title=u"Sélectionner le dossier ou le disque à trier")
    return folder_name
