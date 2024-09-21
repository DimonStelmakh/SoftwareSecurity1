import tkinter as tk
from asyncio import start_server
from tkinter import filedialog, messagebox
from task2 import CaesarCipher


class CryptoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Криптографічна система")
        self.geometry("600x550")

        self.key_var = tk.IntVar()
        self.language_var = tk.StringVar(value='ua')

        self.input_text = tk.Text(self, height=10, width=50)
        self.input_text.pack(pady=10)

        self.output_text = tk.Text(self, height=10, width=50)
        self.output_text.pack(pady=10)

        tk.Label(self, text="Ключ:").pack()
        self.key_entry = tk.Entry(self, textvariable=self.key_var)
        self.key_entry.pack()

        tk.Label(self, text="Мова:").pack()
        self.language_menu = tk.OptionMenu(self, self.language_var, 'ua', 'en')
        self.language_menu.pack()

        self.encrypt_button = tk.Button(self, text="Шифрувати", command=self.encrypt_file)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(self, text="Розшифрувати", command=self.decrypt_file)
        self.decrypt_button.pack(pady=5)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        # file_menu.add_command(label="Створити", command=self.create_file)
        file_menu.add_command(label="Відкрити", command=self.open_file)
        file_menu.add_command(label="Зберегти", command=self.save_file)
        # file_menu.add_command(label="Друк", command=self.print_file)
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=self.quit_app)
        menubar.add_cascade(label="Файл", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Про розробника", command=self.about_developer)
        menubar.add_cascade(label="Допомога", menu=help_menu)

        self.config(menu=menubar)

    # def create_file(self):
        # self.input_text.delete(1.0, tk.END)
        # self.output_text.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.output_text.get(1.0, tk.END))
            messagebox.showinfo("Збереження", "Файл збережено успішно!")

    def encrypt_file(self):
        try:
            key = self.key_var.get()
            language = self.language_var.get()
            text = self.input_text.get(1.0, tk.END).strip()

            if not text:
                messagebox.showwarning("Помилка", "Текст для шифрування відсутній!")
                return

            cipher = CaesarCipher(key)
            encrypted_text = cipher.encrypt(text, language)

            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, encrypted_text)
        except Exception as e:
            messagebox.showerror("Помилка", f"Помилка шифрування: {str(e)}")

    def decrypt_file(self):
        try:
            key = self.key_var.get()
            language = self.language_var.get()
            text = self.input_text.get(1.0, tk.END).strip()

            if not text:
                messagebox.showwarning("Помилка", "Текст для розшифрування відсутній!")
                return

            cipher = CaesarCipher(key)
            decrypted_text = cipher.decrypt(text, language)

            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, decrypted_text)
        except Exception as e:
            messagebox.showerror("Помилка", f"Помилка розшифрування: {str(e)}")

    def about_developer(self):
        messagebox.showinfo("Про розробника", "Ця система розроблена Дмитром Стельмахом із групи ТВ-13")

    def quit_app(self):
        self.quit()


if __name__ == "__main__":
    app = CryptoApp()
    app.mainloop()


if __name__ == "__main__":
    app = CryptoApp()
    app.mainloop()
