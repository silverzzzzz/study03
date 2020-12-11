import pandas as pd
import eel

# デスクトップアプリ作成課題


def kimetsu_search(word, csvname):
    # 検索対象取得
    df = pd.read_csv("./source.csv")
    source = list(df["name"])
    # 検索
    if word in source:
        # CSV書き込み
        writecsv(source, csvname)
        return("『{}』はあります".format(word))
    else:
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        # if add_flg=="1":
        source.append(word)
        # CSV書き込み
        writecsv(source, csvname)
        sourcestr = ",".join(source)
        return("『"+word+"』はありません\n『"+word+"』を追加しました。\n"+sourcestr)


def writecsv(source, csvname):
    # CSV書き込み
    # print(csvname)
    df = pd.DataFrame(source, columns=["name"])
    df.to_csv("./"+csvname+".csv", encoding="utf_8-sig")
    print(source)
