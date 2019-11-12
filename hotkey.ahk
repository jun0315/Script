;translate the word from the line
#F1::
    {
    
    Send ^c
    curr := clipboard
    run https://translate.google.cn/#view=home&op=translate&sl=auto&tl=zh-CN&text=%curr%
    return
    }

#F2::
    {
    Send ^c
    curr := clipboard
    run https://cn.bing.com/search?q=%curr%
    }

;reload
>!<+r::Reload


<!n::Send #^{Right}
<!p::Send #^{Left}

;vim
<!j::Send {Down}
<!k::Send {Up}
<!h::Send {Left}
<!l::Send {Right}
<!g::Send {Home}
<!;::Send {End}

;xkill
^!k::run H:\Python\xkill.exe

;close the file
<!q::Send {LAlt Down}{f4}{LAlt Up}
<!w::Send {ctrl down}{w}{ctrl up}
<!a::Send {ctrl down}{a}{ctrl up}


<!e::Send {ctrl down}{tab}{ctrl up}
<!r::Send {ctrl down}{shift down}{tab}{shift up}{ctrl up}

;+WheelUp::Send {WheelLeft}
;+WheelDown::Send {WheelRight}

;#IfWinActive ahk_class Chrome_WidgetWin_1

;CapsLock::return

;for the pdf change the hotkey
;#IfWinActive ahk_class ATLWIN_JISUPDF_MIAN
;    h::Send {Left}

;#IfWinActive ahk_class ATLWIN_JISUPDF_MIAN
;    l::Send {Right}
