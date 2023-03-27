import json
import random
import re
import pandas as pd
import datetime

# 讀取英文單字檔案，沒有就建立新字典檔案
def load_words():
    try:
        with open("english_word.txt", "r", encoding="utf-8") as f:
            word_dict = json.load(f)
            return word_dict
    except FileNotFoundError:
        with open("english_word.txt", "w", encoding="utf-8") as f:
            word_dict = {"apple": "蘋果", "banana": "香蕉",
                         "orange": "橘子", "watermelon": "西瓜", "kiwi": "奇異果"}
            # 將 ensure_ascii 參數設為 False，就會將特殊字元直接寫入檔案，而非轉換成預設的 Unicode escape 字元。
            # indent 參數，指定要在 JSON 檔案中使用的縮排空格數，
            # indent 設為 2，會讓輸出的 JSON 檔案更容易閱讀，每個層級的資料都會縮排兩個空格。
            json.dump(word_dict, f, ensure_ascii=False, indent=2)
            return word_dict

# 新增單字
def add_word():
    # 檢查輸入的字是否為英文字母或中文字
    while True:
        # 輸入英文單字
        english_word = input("請輸入要新增的英文單字 (取消輸入按 【q 】結束):\n")
        # 檢查是否為 q
        if english_word == "q":
            print("取消新增英文單字。")
            return
        # 檢查是否為英文字母
        if not (english_word.isalpha() and english_word.isascii()):
            print("輸入的不是英文字母，請重新輸入")
            continue

        # 輸入中文單字
        chinese_word = input("請輸入要新增的中文單字 (取消輸入按【q 】結束):\n")
        # 檢查是否為 q
        if chinese_word == "q":
            print("取消新增中文單字。")
            return
        # 檢查是否為中文字
        match = re.search(r"[\u4e00-\u9fff]", chinese_word)
        if not match:
            print("輸入的不是中文字，回到上一層請重新輸入英文單字\n")
            continue

        # 新增成功
        print("新增英文單字成功!")
        eng = english_word
        print(eng)

        print("新增中文翻譯成功!")
        chi = chinese_word
        print(chi)

        # 將字典寫入檔案
        word_dict = load_words()
        word_dict[english_word] = chinese_word
        with open("english_word.txt", "w", encoding="utf8") as f:
            json.dump(word_dict, f, ensure_ascii=False, indent=2)
        print("單字已成功儲存到檔案裡!")

        # 是否繼續新增單字
        while True:
            choice = input("\n是否要繼續新增單字? (y/n): ")
            try:
                if choice.lower() == "y":
                    break  # 回到迴圈開始處
                elif choice.lower() == "n":
                    return  # 結束函式
                else:
                    print("無效的選擇，只能選擇 y 或 n")
            except:
                print("無效的選擇，只能選擇 y 或 n")

# 查看目前所有英文單字
def query_word():
    with open("english_word.txt", "r", encoding="utf-8") as f:
        word_dict = json.load(f)
    # 創建 DataFrame
    eng_col = "%-10s" % "英文單字"
    chi_col = "%-10s" % "中文單字"
    df = pd.DataFrame(list(word_dict.items()), columns=[eng_col, chi_col])
    # 要讓顯示資料都可以對齊
    # 使用 ljust 函數將每個英文單字向左靠齊，使其寬度一致。max_word_length 變數則儲存最長英文單字的長度
    max_word_length = max(df[eng_col].apply(len))
    df[eng_col] = df[eng_col].apply(lambda x: x.ljust(max_word_length))

    max_word_length = max(df[chi_col].apply(len))
    df[chi_col] = df[chi_col].apply(lambda x: x.ljust(max_word_length))
    print(df)

    choice = input("\n 請選擇: 1.刪除英文單字 2.匯出成 Excel 3.離開回到選單:  ")
    if choice == "1":
        while True:
            del_word_key = input("請輸入要刪除的英文單字(按q取消): ")
            if del_word_key.lower() == "q":
                return
            elif del_word_key not in word_dict:
                print("查無此單字，請重新輸入")
            else:
                del word_dict[del_word_key]
                print(f"【{del_word_key}】單字已刪除!!")
                # 將資料重新寫入
                with open("english_word.txt", "w", encoding="utf-8")as f:
                    json.dump(word_dict, f, ensure_ascii=False, indent=2)
                return
    elif choice == "2":
        filename = "english_word_" + \
            datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx"
        # 將 Json 轉為 DataFrame
        df = pd.json_normalize(word_dict)
        # 將 DataFrame 垂直排列
        df_vertical = df.T.reset_index()
        # 設定新的欄位名稱
        df_vertical.columns = ['英文單字', '中文單字']
        # 將 DataFrame 儲存為 Excel 檔案
        df_vertical.to_excel(filename, index=False)
        print("將資料匯出成 Excel 檔案!!")
    elif choice == "3":
        return  # 結束返回主選單
    else:
        return query_word()

# 猜英文單字遊戲
def english_word_quiz():
    print("英文單字測驗，每回測驗共有五題,每題最多有三次機會回答")
    words = load_words()
    score = 0
    used_words = []  # 儲存已使用過的單字
    # 每回測驗共有五題
    for i in range(5):
        # 從字典中隨機選擇一個尚未使用過的單字
        # 將出現過的單字從字典中刪除，避免重複出現
        word = random.choice(list(set(words.keys()) - set(used_words)))
        used_words.append(word)
        print(f"\n第{i+1}題,請回答正確的英文單字")
        quiz = word
        # 每題最多可回答三次
        # 初始提示字母數量為0
        hint = 1
        for j in range(1, 4):
            answer = input(f"請輸入【{words[word]}】的英文單字: ")
            if answer == quiz:
                if j == 1:
                    print("太棒了! 一次就答對了! 可獲得20分!")
                    score += 20
                    break  # 跳出內層迴圈，進行下一題
                else:
                    if j == 2:
                        print("不錯哦，第二次就答對了! 可獲得10分")
                        score += 10
                        break  # 跳出內層迴圈，進行下一題
                    elif j == 3:
                        print("還可以，第三次才答對了! 可獲得5分")
                        score += 5
                        break  # 跳出內層迴圈，進行下一題
            else:
                if j < 3:
                    hint += 1  # 增加提示字母數量
                    print(f"不對哦!請再試試看! 提示: {quiz[0:hint]}\n")
                else:
                    print("要加油哦!答題失敗。正確答案是：", quiz)

    # 五題答完後會跳出，顯示目前得分，是否要繼續英文單字測驗
    print(f"\n您的分數為: {score} 分")
    while True:
        choice = input("是否要繼續英文單字測驗？(y/n): ")
        try:
            if choice.lower() == "y":
                english_word_quiz()  # 繼續執行
            elif choice.lower() == "n":
                return   # 結束返回主選單
        except:
            print("無效的選擇，只能選擇 y 或 n")

# 主程式:選擇項目
def main():
    # 程式一開始會先讀取英文單字檔案，沒有就建立新字典檔案
    load_words()

    print("\n<<< 歡迎來到英文單字測驗遊戲,請選擇要執行的項目： >>>")
    print("1. 新增單字")
    print("2. 查看所有單字/刪除單字/匯出成 Excel")
    print("3. 英文單字測驗遊戲")
    print("4. 退出結束")

    while True:
        print("\n請輸入您的選擇:")
        choice = input("1.新增單字 2.查看所有單字/刪除單字/匯出成 Excel 3.英文單字測驗遊戲 4.退出結束 : ")
        if choice == "1":
            add_word()  # 新增單字
        elif choice == "2":
            query_word()  # 查詢單字/刪除單字/匯出成 Excel
        elif choice == "3":
            english_word_quiz()  # 單字測驗
        elif choice == "4":
            print("退出")
            break
        else:
            print("輸入錯誤,請重新選擇要執行的項目")


if __name__ == '__main__':
    main()
