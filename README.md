# 英文單字測驗遊戲
## 摘要

這是一款簡單的英文單字學習程式，透過隨機測驗單字，可以讓使用者增加英文單字記憶。可以透過此程式來建立新的英文單字及其中文翻譯，查看目前所有英文單字、刪除不需要的單字，也可將所有英文單字匯出成Excel檔案出來方便查看。

## 功能說明

- 程式開始會先讀取英文單字文件，沒有就會建立新的字典文件。
- 將新的英文單字和中文翻譯添加到字典文件中。
- 查看所有英文單字並選擇是否需要刪除單字或是匯出成Excel文件。
- 對文件中的英文單字進行隨機測驗。


## 開發環境

- Visual Studio Code
- Python

## 安裝和使用

1. 安裝Python開發環境和VS Code編輯器。（可以在Google Colab上操作）
2. 下載程式原始檔，解壓縮至任意資料夾中。
3. 在 VS Code 中開啟資料夾，並開啟終端機，執行程式。
4. 在終端機執行輸入指令時，可輸入到 python english 接著按鍵盤上的TAB鍵，可快速打出完整名稱。
5. 命令運行程序：`python '.\english _word _quiz _game.py'`

## 使用的模組套件

- `import json，random，re，pandas as pd，datetime`

## 執行流程

1. 執行程式後，可以看到選單選項，可以選擇要新增單字、查詢單字、刪除、匯出excel或進行英文單字測驗。
2. 新增單字功能會要求使用者輸入英文單字和中文翻譯，並且會將新增的單字儲存到本地的專案資料夾中的 english_word.txt 檔案中。
3. 查詢單字功能會讀取 english_word.txt 檔案中所有的單字並且使用Pandas 將它們顯示在一個表格中。
4. 英文單字測驗遊戲，會從english_word.txt 中隨機選取英文單字進行測驗。
5. 每回測驗共有五題，每題最多有三次機會回答，依答題次數給予不同分數，一次答對20分，後面兩次分別為10分、5分並給與提示，測驗結束後會顯示分數。

## 函數

### `load_words（）`

程式區塊說明
- 負責讀取英文單字檔案，如果檔案不存在就建立新字典檔案並加入一些初始的單字。
- 使用json.load() 方法將檔案內容轉換成Python字典物件，並回傳該字典物件。
- 初始使用或是檔案不存在，就使用json.dump()方法建立一個新的字典物件，並將該字典物件寫入“english_word.txt” 檔案中。
- json.dump()方法將 ensure_ascii 參數設為 False，就會將特殊字元直接寫入檔案，而非轉換成預設的 Unicode escape 字元。
- indent參數，指定要在JSON檔案中使用的縮排空格數，會讓輸出的JSON檔案更容易閱讀，每個層級的資料都會縮排兩個空格。


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

程式區塊說明
- 負責新增英文單字和中文翻譯。
- 使用以下方法來判斷使用者輸入的字是否為英文字母：
  1. 使用 str.isalpha() 方法來檢查字串是否只包含字母
  2. 使用 str.isascii() 方法來檢查字串是否只包含 ASCII 字元。
  3. 結合以上兩個方法，如果一個字串同時滿足 isalpha() 和 isascii()的條件，那麼它就是英文字母。

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
```python
# 將字典寫入檔案
  word_dict = load_words()
  word_dict[english_word] = chinese_word
  with open("english_word.txt", "w", encoding="utf8") as f:
      json.dump(word_dict, f, ensure_ascii=False, indent=2)
```
```pyrhon
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
```

### `query_word（）`

程式區塊說明
- 負責顯示所有英文單字、刪除單字和匯出成 Excel 檔案。
- 使用 pandas 套件的 DataFrame() 函式，將字典物件轉換成 DataFrame 物件，類似於 Excel 表格，可以方便地處理表格資料。
- 程式碼中使用了 ljust() 函式將每個英文單字和中文單字向左靠齊，使其寬度一致。
- 使用 print() 函式將 DataFrame 物件顯示在螢幕(終端機)上。

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

### 判斷要刪除的英文單字

程式區塊說明
- 這段程式碼是一個 while 迴圈，用來讓使用者輸入要刪除的英文單字。當使用者輸入“q”時，迴圈會結束。
- 如果使用者輸入的英文單字不存在於 word_dict 字典物件中，程式碼會顯示 “查無此單字，請重新輸入”的訊息。
- 如果使用者輸入的英文單字存在於 word_dict 字典物件中，程式碼會將該單字從字典物件中刪除，並顯示【英文單字】單字已刪除的訊息。
- 程式碼會使用 with 關鍵字開啟 english_word.txt 檔案，並使用 json.dump() 方法將更新後的 word_dict 字典物件寫入檔案中。

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

### 匯出成 Excel 檔案

程式區塊說明
- 匯出成 Excel 檔案，檔名會自動加上日期時間，可以區分不同版本的檔案。
- 使用 pd.json_normalize() 函式將 word_dict 字典物件轉換成一個 DataFrame 物件。
- 使用 df.T.reset_index() 函式將 DataFrame 物件垂直排列。
- 使用 df_vertical.columns = [‘英文單字’, ‘中文單字’] 設定新的欄位名稱。
- 使用 to_excel() 方法將 DataFrame 物件儲存為一個 Excel 檔案。

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
