import pytube
import flet as ft


def main(page: ft.Page):
    # some design changes
    page.title = "YouTube video downloader"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#c6f5fd"
    page.scroll = True

    # function that checks if video is selected and then add dropdown to select quality
    def menu(idk):
        if dropdown1.value == "Video":
            cont4.content = dropdown2
            page.update()


    # dropdown menu to choose audio or video
    dropdown1 = ft.Dropdown(width=200, options=[
        ft.dropdown.Option("Audio"),
        ft.dropdown.Option("Video")
    ], on_change=menu)

    # quality dropdown
    dropdown2 = ft.Dropdown(width=200, options=[
        ft.dropdown.Option("144p"),
        ft.dropdown.Option("240p"),
        ft.dropdown.Option("360p"),
        ft.dropdown.Option("480p"),
        ft.dropdown.Option("720p"),
        ft.dropdown.Option("240p"),
        ft.dropdown.Option("1080p"),
        ft.dropdown.Option("1440p"),
        ft.dropdown.Option("Nejvyšší"),
    ])

    # alert box to alert on downloading and finishing download / function to trigger alerts
    dlg1 = ft.AlertDialog(
        title=ft.Text("Video nebylo nalezeno"), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    dlg2 = ft.AlertDialog(
        title=ft.Text("Stahuji"), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    dlg3 = ft.AlertDialog(
        title=ft.Text("Staženo"), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    dlg4 = ft.AlertDialog(
        title=ft.Text("Kvalita není dostupná"), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    def alert1():
        page.dialog = dlg1
        dlg1.open = True
        page.update()

    def alert2():
        page.dialog = dlg2
        dlg2.open = True
        page.update()

    def alert3():
        page.dialog = dlg3
        dlg3.open = True
        page.update()

    def alert4():
        page.dialog = dlg4
        dlg4.open = True
        page.update()

    # declaration of text, that shows if the submitted value is video
    text = ft.Text()

    # function to test if folder was selected
    def tester(test):
        if test:
            return test

    # function to download on click
    def download(z):
        try:
            if (dropdown1.value == "Video"):
                alert2()
                if (dropdown2.value == "Nejvyšší"):
                    pytube.YouTube(txt_number.value).streams.get_highest_resolution().download(tester(selected_directory))
                    alert1()
                else:
                    pytube.YouTube(txt_number.value).streams.get_by_resolution(dropdown2.value).download(tester(selected_directory))
                    alert1()
            else:
                alert2()
                pytube.YouTube(txt_number.value).streams.get_audio_only().download(tester(selected_directory))
                alert3()
        except AttributeError:
                alert4()
        except:
                alert1()

    # file picking block
    directory_path = ft.Text()

    def get_directory_result(e):
        global selected_directory
        directory_path.value = selected_directory = e.path if e.path else "Cancelled!"
        page.update()

    picker = ft.FilePicker(on_result=get_directory_result)
    btn_file = ft.ElevatedButton("Vyber složku", on_click=picker.get_directory_path, icon=ft.icons.SUBDIRECTORY_ARROW_LEFT)

    # idk what does this do, but it is important
    page.overlay.extend([picker])

    txt_number = ft.TextField(label="Zadejte URl videa", width=300)
    btn = ft.ElevatedButton("Stáhnout", on_click=download, icon=ft.icons.DOWNLOADING_OUTLINED)
    cont1 = ft.Container(margin=50, content=txt_number, )
    cont2 = ft.Container(margin=35, content=dropdown1)
    cont3 = ft.Container(margin=35, content=btn)
    cont4 = ft.Container(margin=35, )
    text_header = ft.Text(size=40, value="YouTube video downloader")

    page.add(text_header, cont1, cont2,cont4, btn_file, directory_path, cont3, text)


ft.app(target=main)

