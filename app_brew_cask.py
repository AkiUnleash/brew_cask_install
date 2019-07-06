# coding: UTF-8
import os
import glob
import subprocess
import re

# コマンド出力結果を返す関数
def res_cmd(cmd):

    # コマンド結果の出力
    return subprocess.Popen(
        cmd, stdout=subprocess.PIPE,
        shell=True).communicate()[0]

# brew serch コマンドテキスト発行する
def brew_search(appName):

    # コマンドの内容
    cmd = ("brew search " + appName)

    # 結果の判断
    return 1  if appName in res_cmd(cmd) else 0

# 検索したファイル名を配列にする(result_arr)
def globFileInfo(directry):

    # 配列宣言
    result_arr = []

    # ApplicationsフォルダのApp名を取得→配列化
    files = glob.glob(directry)
    for file in files:
        fname = os.path.basename(file)
        fname = fname[0:len(fname)-4:].lower().replace(' ','-')
        print(fname)
        flg = brew_search(fname)
        print(flg)
        result_arr.append([fname, file])

    return result_arr

if __name__ == "__main__":

    # シェルファイル作成
    with open('./cask.sh', 'w'):pass

    # シェルファイルの追記
    f = open('./cask.sh', 'a')

    # appファイルを検索して配列化
    result_arr = globFileInfo("/Applications/*.app")
    result_arr = result_arr + globFileInfo("/Applications/**/*.app")

    # f.write('brew cask install ' + fname + '\n')

    #シェルファイルの追記クローズ
    f.close

    print(result_arr)