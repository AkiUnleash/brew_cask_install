# coding: UTF-8
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

#     print(result_array)
#     if 'Casks' in result_array and 'alfred' in result_array:
#         print('OK')

if __name__ == "__main__":
    main()