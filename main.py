from tkinter import Tk, Label, Button, Listbox, END, MULTIPLE, filedialog, messagebox
from PIL import Image


def images_to_pdf(image_paths, pdf_path):
    if not image_paths:
        print("Нет изображений для конвертации.")
        return

    images = []

    for image_path in image_paths:
        try:
            img = Image.open(image_path)
            img = img.convert('RGB')  # Конвертируем изображение в RGB режим
            images.append(img)
        except Exception as e:
            print(f"Не удалось открыть изображение {image_path}: {e}")
            continue

    if images:
        first_image = images[0]
        first_image.save(pdf_path,
                         save_all=True,
                         append_images=images[1:])
        messagebox.showinfo("Успех", f"PDF файл '{pdf_path}' успешно сохранён.")
        print(f"PDF файл '{pdf_path}' успешно создан.")
    else:
        print("Не удалось создать PDF, так как нет валидных изображений.")


def select_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    for file_path in file_paths:
        image_listbox.insert(END, file_path)


def save_pdf():
    if not image_listbox.size():
        print("Сначала добавьте изображения.")
        return

    pdf_path = filedialog.asksaveasfilename(initialfile="result.pdf",
                                            defaultextension=".pdf",
                                            filetypes=[("PDF Files", "*.pdf")])
    if pdf_path:
        image_paths = list(image_listbox.get(0, END))
        images_to_pdf(image_paths, pdf_path)


def delete_selected_images():
    selected_indices = image_listbox.curselection()
    for index in reversed(selected_indices):  # Удаление элементов в обратном порядке
        image_listbox.delete(index)


# Создаем основной интерфейс
root = Tk()
root.title("Конвертирование изображений в PDF")
root.iconbitmap("icon.ico")

# Метки и элементы управления
label = Label(root, text="Выберите изображения:")
label.pack()

image_listbox = Listbox(root,
                        selectmode=MULTIPLE,
                        width=50,
                        height=10)
image_listbox.pack()

select_button = Button(root,
                       text="Добавить изображения",
                       command=select_images)
select_button.pack()

delete_button = Button(root,
                       text="Удалить выделенные изображения",
                       command=delete_selected_images)
delete_button.pack()

save_button = Button(root,
                     text="Сохранить в PDF",
                     command=save_pdf)
save_button.pack()

# Запуск приложения
root.mainloop()
