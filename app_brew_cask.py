# coding: UTF-8
import os
import glob
import subprocess
import re
from tqdm import tqdm

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
    return 1 if appName in str(res_cmd(cmd)) else 2

# 検索したファイル名を配列にする(result_arr)
def globFileInfo(directry):

    # 配列宣言
    result_arr = []

    # ApplicationsフォルダのApp名を取得→配列化
    files = glob.glob(directry)
    for file in tqdm(files):
        # ファイル名を取得→全小文字／スペースはハイフンに置換
        fname = os.path.basename(file)
        fname = fname[0:len(fname)-4:].lower().replace(' ', '-')

        # brew search でインストール可能化の確認(可=1/不可=2)
        flg = brew_search(fname)

        # 配列に取り込む
        result_arr.append([fname, file, flg])

    return result_arr


if __name__ == "__main__":


    # appファイルを検索して配列化
    result_arr = globFileInfo("/Applications/*.app")
    result_arr = result_arr + globFileInfo("/Applications/**/*.app")

    # result_arrのflgでソートする
    result_arr = sorted(result_arr, key=lambda x: x[2])

    # シェルファイル作成
    with open('./brew_cask_install.sh', 'w'):pass

    # シェルファイルの追記
    f = open('./cask.sh', 'a')

    # shファイルを出力する
    for r in tqdm(result_arr):
        status = 'installable' if r[2] == 1 else 'not installable'
        f.write('#[' + status + ']' + r[1] + '\n')
        if r[2] == 1:
            f.write('brew cask install ' + r[0] + '\n\n')
        else:
            f.write('# brew cask install ' + r[0] + '\n\n')

    # シェルファイルの追記クローズ
    f.close
