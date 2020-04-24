# This is a tutorial of using github

## TODO
- [x] 安裝github
- [ ] github 指令
- [ ] Markdown

---
## github指令
- config (設定git bash)
    - git config --global user.name myusername   
    - git config --global user.email myemail  
    - git config --global github.user myusername  
- clone from others (使用別人的作品的時候)
    - git clone {url}
- update repo (當你的repo被別人更新的時候)
    - git pull
- **upload to yours**
    1. git status (檢查狀態)
    2. git add * （把檔案加到repo中，*代表全部）
    3. git commit -m 'message' (確定變更)
    4. git push (更改至原本repo)
    5. checkout your github

---
## Markdown語法
連結
>this is a [link](https://www.google.com/) to *google*.  
>this is [covid19](covid19.csv) file.

可愛的狗狗
>![dog](pic/corgi.jpeg)  
> [影片](https://youtu.be/yw-s6OSd51I)  

可愛的貓貓
> ![cat](pic/cat.jpeg)  
> [here](https://youtu.be/n2OEHlkCXio)  

表格
>|A|B|C|
>|---|---|---|
>|aa|bb|cc|
>|zz|qq|bb|

<!-- 這是一行註解-->