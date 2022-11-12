;https://www.autohotkey.com
;https://www.macrocreator.com

F1::
    ;F1 lenyomására fog kettőt kattintani
    Loop, 2
    {
        MouseClick, left
    }

F2::
    ;F3 lenyomására fog folyamatosan kattintani
    Loop
    {
        MouseClick, left
    }

;Ez macera és ha tokenes a beléptetés, nem is működik
F3::
    ;Fiddler használatával először meg kell nézni, hogy a belépéskor milyen formában kerül küldésre a post data
    URL := "https://www.autohotkey.com/boards/ucp.php?mode=login"
    PostData := "username=AzEnUserem&password=JeLszo123&redirect=.%2Fucp.php%3Fmode%3Dlogin&sid=c89f5d5aac01c57078991f7c15577764&redirect=index.php&login=Login"

    ;Post requestet elküldi, headert beállítja, stb... webstuff
    oHTTP := ComObjCreate("WinHttp.WinHttpRequest.5.1")
    ;Post request
    oHTTP.Open("POST", URL , False)
    ;Add User-Agent header
    oHTTP.SetRequestHeader("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)")
    ;Add Referer header
    oHTTP.SetRequestHeader("Referer", URL)
    ;Add Content-Type
    oHTTP.SetRequestHeader("Content-Type", "application/x-www-form-urlencoded")
    ;Send POST request
    oHTTP.Send(PostData)

    ;Kiírja a html kódot anélkül, hogy böngészőt egyszer is megnyitna
    Gui, Add, Edit, w800 r30, % oHTTP.ResponseText
    Gui, Show
    return

;Ez tokenes oldalaknál is működik
;Ez 10 másodpercenként be- és kilép az oldalról, de kezdetleges kód
;pl ha több ideig tölt az oldal, akkor könnyen szétcsúszhat
;Ezt a módszert lehet ötvözni a ComObjecttel...
F4::
    Run, iexplore.exe https://www.autohotkey.com/boards/ucp.php?mode=login,
	Sleep, 5000
    Send AzEnUserem
    Loop
    {
            Sleep, 100
            Send {TAB}
        Send JeLszo123
            Sleep, 100
            Send {ENTER}
            Sleep, 5000
        Loop, 15
        {
            Send {TAB}
        }
        Send {ENTER}
        Send {ENTER}
    }


F8::Reload
F12::ExitApp
;F8, F12 <- ezeket nyomd meg, ha ki akarsz lépni