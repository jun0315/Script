;translate the word from the line
#F1::
    {
    saved := clipboard
    Send ^c
    curr := clipboard

    b := saved == curr
    if not b
        run https://translate.google.cn/#view=home&op=translate&sl=auto&tl=zh-CN&text=%curr%
    else
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


>!n::Send #^{Right}
>!p::Send #^{Left}

;vim
>!j::Send {Down}
>!k::Send {Up}
>!h::Send {Left}
>!l::Send {Right}

;close the file
<!q::Send {LAlt Down}{f4}{LAlt Up}
<!w::Send {ctrl down}{w}{ctrl up}

<!e::Send {ctrl down}{tab}{ctrl up}
<!r::Send {ctrl down}{shift down}{tab}{shift up}{ctrl up}

;#IfWinActive ahk_class Chrome_WidgetWin_1

;CapsLock::return

;for the pdf change the hotkey
#IfWinActive ahk_class ATLWIN_JISUPDF_MIAN
    h::Send {Left}

#IfWinActive ahk_class ATLWIN_JISUPDF_MIAN
    l::Send {Right}
