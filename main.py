import pytube
import flet as ft


def main(page: ft.Page):
    # some design changes
    page.title = "YouTube video downloader"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#c6f5fd"

    # dropdown menu to choose audio or video
    dropdown = ft.Dropdown(width=200, options=[
        ft.dropdown.Option("Audio"),
        ft.dropdown.Option("Video")
    ])

    # alert box to alert on downloading and finishing download
    dlg1 = ft.AlertDialog(
        title=ft.Text("Tohle nelze stáhnout"), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    dlg2 = ft.AlertDialog(
        title=ft.Text("Stahuji"), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    dlg3 = ft.AlertDialog(
        title=ft.Text("Staženo"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    # declaration of text, that shows if the submitted value is video
    text = ft.Text()

    # function to test if folder was selected
    def tester(test):
        if test:
            return test

    # function to download on click
    def download(z):
        try:
            page.dialog = dlg2
            dlg2.open = True
            page.update()
            if (dropdown.value == "Video"):
                pytube.YouTube(txt_number.value).streams.get_highest_resolution().download(tester(selected_directory))
            else:
                pytube.YouTube(txt_number.value).streams.get_audio_only().download(tester(selected_directory))
                page.dialog = dlg3
                dlg3.open = True
                page.update()
        except:
            page.dialog = dlg1
            dlg1.open = True
            page.update()

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
    cont2 = ft.Container(margin=35, content=dropdown)
    cont3 = ft.Container(margin=35, content=btn)
    text_header = ft.Text(size=40, value="YouTube video downloader")

    page.add(text_header, cont1, cont2, btn_file, directory_path, cont3, text)


ft.app(target=main)
