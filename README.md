## 概述

這是一個簡單的英語單詞學習程序，允許用戶通過隨機測驗增加他們的英語詞彙。使用此程序，用戶可以創建新的英語單詞及其中文翻譯，查看所有當前的英語單詞，刪除不必要的單詞，並導出所有英語單詞為Excel文件以便查看。

## 特點

- 程序首先讀取英語單詞文件。如果不存在，將創建新的字典文件。
- 用戶可以將新的英語單詞及其中文翻譯添加到字典文件中。
- 用戶可以查看所有英語單詞，並選擇是否刪除單詞或將其導出為Excel文件。
- 用戶可以在單詞文件中進行隨機測驗。

## 開發環境

- Visual Studio Code
- Python

## 安裝和使用

1. 安裝Python開發環境和VS Code編輯器。（可以在Google Colab上操作）
2. 下載程序源文件並將其提取到任何文件夾中。
3. 在VS Code中打開文件夾，並打開終端運行程序。
4. 在終端中輸入命令，您可以輸入“python english”，然後按鍵盤上的TAB鍵快速輸入完整名稱。
5. 命令運行程序：`python '.\\english _word _quiz _game.py'`

## 使用的模塊和包

- `import json，random，re，pandas as pd，datetime`

## 執行流程

運行程序後，用戶將看到一個菜單，其中包含添加單詞、查詢單詞、刪除單詞、導出到Excel或進行英語單詞測驗的選項。

- 要添加單詞，用戶必須輸入英語單詞及其中文翻譯，程序將新單詞保存到項目文件夾中的“english_word.txt”文件中。
- 要查詢單詞，程序將從“english_word.txt”文件中讀取所有單詞，並使用Pandas包將其顯示在表格中。
- 要進行英語單詞測驗，程序將從“english_word.txt”文件中隨機選擇英語單詞，並要求用戶將其翻譯為中文。每個測驗都有五個問題，每個問題都有最多三次機會回答。根據嘗試次數，用戶將獲得不同的分數，第一次嘗試獲得20分，第二次嘗試獲得10分，第三次嘗試獲得5分，並附帶提示。測驗結束後，將顯示分數。
- 程序還允許用戶從“english_word.txt”文件中刪除單詞或將所有單詞導出為Excel文件。

## 函數

### `load_words（）`

- 描述：此函數負責讀取英語單詞文件。如果該文件不存在，它將創建一個新的字典文件，其中包含一些初始單詞。該函數使用`json.load（）`方法將文件內容轉換為Python字典對象並返回該字典對象。如果文件是新的或不存在，該函數使用`json.dump（）`方法創建一個新的字典對象並將其寫入項目文件夾中的“english_word.txt”文件中。

```python
def load_words():
    try:
        with open("english_word.txt", "r", encoding="utf-8") as f:
            word_dict = json.load(f)
            return word_dict
    except FileNotFoundError:
        with open("english_word.txt", "w", encoding="utf-8") as f:
            word_dict = {"apple": "蘋果", "banana": "香蕉",
                         "orange": "橘子", "watermelon": "西瓜", 
                         "kiwi": "奇異果"}
            json.dump(word_dict, f, ensure_ascii=False, indent=2)
            return word_dict
```

文件內容: english_word.txt

```python
{
  "apple": "蘋果",
  "banana": "香蕉",
  "orange": "橘子",
  "tomato": "番茄",
  "papaya": "木瓜",
  "peach": "桃子",
  "kiwi": "奇異果"
}
```

### `add_word（）`

- 描述：此函數負責添加新的英語單詞及其中文翻譯。該函數使用`str.isalpha（）`方法檢查輸入字符串是否僅包含英文字母，並使用`str.isascii（）`方法檢查輸入字符串是否僅包含ASCII字符。如果字符串滿足這兩個條件，它是一個英文字母。該函數還使用正則表達式匹配中文字符。如果字符串包含中文字符，它是一個中文單詞。然後，該函數將該字典保存到項目文件夾中的“english_word.txt”文件中，並詢問用戶是否要繼續添加單詞。
1. 使用正則表達式 (regex) 來匹配中文字符。中文字符的 Unicode 範圍是 \u4e00-\u9fff。
2. 使用 re 模組來實現正則表達式的功能。
3. 使用 re.search() 方法來檢查字串是否包含中文字符。如果是，則返回一個匹配對象 (match object)，否則返回 None。

```python
# 檢查是否為英文字母
 if not (english_word.isalpha() and english_word.isascii()):
    print("輸入的不是英文字母，請重新輸入")
    continue
```

- 使用以下方法來判斷使用者輸入的字是否為中文字：
1. 使用正則表達式 (regex) 來匹配中文字符。中文字符的 Unicode 範圍是 \u4e00-\u9fff。
2. 使用 re 模組來實現正則表達式的功能。
3. 使用 re.search() 方法來檢查字串是否包含中文字符。如果是，則返回一個匹配對象 (match object)，否則返回 None。

```python
# 檢查是否為中文字
  match = re.search(r"[\u4e00-\u9fff]", chinese_word)
  if not match:
     print("輸入的不是中文字，回到上一層請重新輸入英文單字\n")
     continue
```

### `query_word（）`

- 描述：此函數負責顯示所有英語單詞、刪除單詞和將其導出為Excel文件。該函數使用Pandas包的`DataFrame（）`函數將字典對象轉換為DataFrame對象，類似於Excel表格。然後，該函數使用`ljust（）`函數將每個英語和中文單詞左對齊，使它們的寬度一致。最後，該函數使用`print（）`函數在屏幕上顯示DataFrame對象。

```python
with open("english_word.txt", "r", encoding="utf-8") as f:
        word_dict = json.load(f)
    # 創建 DataFrame
    eng_col = "%-10s" % "英文單字"
    chi_col = "%-10s" % "中文單字"
    df = pd.DataFrame(list(word_dict.items()), columns = [eng_col, 
                      chi_col])
    max_word_length = max(df[eng_col].apply(len))
    df[eng_col] = df[eng_col].apply(lambda x: x.ljust(max_word_length))

    max_word_length = max(df[chi_col].apply(len))
    df[chi_col] = df[chi_col].apply(lambda x: x.ljust(max_word_length))
    print(df)
```

### `delete_word（）`

- 描述：此函數負責從“english_word.txt”文件中刪除英語單詞。該函數使用while循環允許用戶輸入要刪除的單詞。如果該單詞不存在於字典對象中，程序將顯示一條消息，說明單詞不存在，用戶可以輸入另一個單詞。如果該單詞存在於字典對象中，該函數將該單詞從字典對象中刪除，並顯示一條消息，說明該單詞已被刪除。然後，該函數將更新後的字典對象保存到“english_word.txt”文件中。

```python
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
```

### `export_to_excel（）`

- 描述：此函數負責將所有英語單詞導出為Excel文件。該函數使用`pd.json_normalize（）`函數將字典對象轉換為DataFrame對象，並使用`df.T.reset_index（）`函數將DataFrame對象垂直重新排列。然後，該函數使用`df_vertical.columns = [‘English’, ‘Chinese’]`函數設置新的字段名，並將DataFrame對象導出為帶有當前日期和時間的Excel文件名。

```python
filename = "english_word_" +  
       datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx"
   
# 將 Json 轉為 DataFrame
   df = pd.json_normalize(word_dict)
   # 將 DataFrame 垂直排列
   df_vertical = df.T.reset_index()
   # 設定新的欄位名稱
   df_vertical.columns = ['英文單字', '中文單字']
   # 將 DataFrame 儲存為 Excel 檔案
   df_vertical.to_excel(filename, index= False)
    print("將資料匯出成 Excel 檔案!!")
```
### `english_word_quiz()`

程式區塊說明

- 負責進行英文單字測驗遊戲，每回測驗共有五題，每題最多有三次機會回答。
- 程式開始時會先呼叫 load_words() 函式載入單字字典，接著進入主要的遊戲迴圈 english_word_quiz()。
- 在遊戲迴圈中，從字典中隨機選擇一個尚未使用過的單字，並將出現過的單字從字典中刪除，避免重複出現。
- set(words.keys())：取得英文單字字典的所有鍵值 (英文單字)並轉換成集合形式。
- set(used_words)：已經使用過的單字集合。
- set(words.keys()) - set(used_words)：將兩個集合相減，得到還未使用過的單字集合。
- list(set(words.keys()) - set(used_words)))：將集合轉換為列表形式。
- 玩家會被要求回答正確的英文單字，每題最多可回答三次，若第一次就回答正確可獲得20分，第二次為10分並給兩個字母提示，第三次為5分並給三個字母提示，若三次都回答錯誤，則顯示正確答案。

```python
# 猜英文單字遊戲
def english_word_quiz():
    print("英文單字測驗，每回測驗共有五題,每題最多有三次機會回答")
    words = load_words()
    score = 0
    used_words = [] # 儲存已使用過的單字
    # 每回測驗共有五題
    for i in range(5):
        # 從字典中隨機選擇一個尚未使用過的單字
        # 將出現過的單字從字典中刪除，避免重複出現
        word = random.choice(list(set(words.keys()) - set(used_words)))                                  
        used_words.append(word)
        print(f"\n第{i+1}題,請回答正確單字的英文單字")
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
```
### main()

程式區塊說明

- 負責主程式的運行，功能包括新增單字、查詢單字、刪除單字、匯出成 Excel 和單字測驗。
- 程式一開始會讀取已經存在的英文單字檔案，如果檔案不存在則會創建一個新的字典檔案。
- 當使用者輸入選擇後，程式會根據使用者的選擇執行相應的功能，如果輸入了不正確的選擇，程式會輸出現錯誤訊息，並要求使用者重新輸入選擇。

```python
def main():
    # 程式一開始會先讀取英文單字檔案，沒有就建立新字典檔案
    load_words()
    print("<<< 歡迎來到英文單字測驗遊戲，請選擇要執行的項目： >>>")
    print("1. 新增單字")
    print("2. 查看所有單字/刪除單字/匯出成 Excel")
    print("3. 英文單字測驗遊戲")
    print("4. 退出結束")
 while True:
        print("\n請輸入您的選擇:")
        choice = input("1.新增單字 2.查看所有單字/刪除單字/匯出成 Excel
                        3.英文單字測驗遊戲 4.退出結束 : ")
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
```
