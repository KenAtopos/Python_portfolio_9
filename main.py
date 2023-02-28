import tkinter as tk


class DisappearingTextApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Disappearing Text Writing App')

        self.label = tk.Label(self.root, text='Type in the box below. If you stop typing, your work will disappear!')
        self.label.pack()

        self.text = tk.Text(self.root)
        self.text.pack()

        self.timer_id = None
        self.text.bind('<Key>', self.reset_timer)

    def reset_timer(self, event):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
        self.timer_id = self.root.after(3000, self.clear_text)

    def clear_text(self):
        self.text.delete('1.0', tk.END)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = DisappearingTextApp()
    app.run()
