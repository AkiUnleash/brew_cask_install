# coding: UTF-8
import os
import glob
import subprocess
import re

def res_cmd(cmd):

    # コマンド結果の出力
    return subprocess.Popen(
        cmd, stdout=subprocess.PIPE,
        shell=True).communicate()[0]

def brew_search(appName):

    # コマンドの内容
    cmd = ("brew search " + appName)

    # コマンド結果の配列化（空白と改行）
    result_array = re.split(" |\n", res_cmd(cmd))

    # 結果の判断
    return result_array


if __name__ == "__main__":

    # シェルファイル作成
    with open('./cask.sh', 'w'):pass

    # シェルファイルの追記
    f = open('./cask.sh', 'a')

    # ApplicationsフォルダのApp名を取得→シェルに追記
    files = glob.glob("/Applications/*.app")
    for file in files:
        fname = os.path.basename(file)
        fname = fname[0:len(fname)-4:].lower().replace(' ','-')
        f.write('brew cask install ' + fname + '\n')

    # ApplicationsサブフォルダのApp名を取得→シェルに追記
    files = glob.glob("/Applications/**/*.app")
    for file in files:
        fname = os.path.basename(file)
        fname = fname[0:len(fname)-4:].lower().replace(' ','-')
        f.write('brew cask install ' + fname + '\n')

    #シェルファイルの追記クローズ
    f.close



# p_tmp = pathlib.Path('/Applications')
# files = p_tmp.glob("**/*.app")


# files = os.listdir(path)
# files_app = [f for f in files if f[-4:] == '.app']
# print(files_app)

# for f in files_app:
#     f_name = f[0:len(f)-4].lower().replace(' ','-')
#     print('brew cask install ' + f_name)
#     # print('brew search ' + f_name)

# for fd_path, sb_folder, sb_file in os.walk(path):
#     for files in sb_file:
#         if files[-4:] == '.app':
#             print(files)

