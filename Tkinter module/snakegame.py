import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game 🐍")
        self.root.resizable(False, False)

        # Game constants
        self.GRID_SIZE = 20
        self.CANVAS_SIZE = 500
        self.SPEED = 120
        self.direction = "Right"
        self.game_running = True

        # Score
        self.score = 0

        # UI Setup
        self.canvas = tk.Canvas(root, width=self.CANVAS_SIZE, height=self.CANVAS_SIZE,
                                bg="#1E1E1E", highlightthickness=0)
        self.canvas.pack()

        self.score_label = tk.Label(root, text="Score: 0", font=("Segoe UI", 16, "bold"))
        self.score_label.pack(pady=10)

        self.restart_btn = tk.Button(root, text="Restart", font=("Segoe UI", 14, "bold"),
                                     bg="#4F46E5", fg="white", command=self.restart,
                                     relief="flat", padx=10, pady=5)
        self.restart_btn.pack(pady=5)

        # Initial snake and food
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = None

        # Key binding
        self.root.bind("<Key>", self.change_direction)

        self.spawn_food()
        self.update()

    # ---------- Spawn Food ----------
    def spawn_food(self):
        while True:
            x = random.randint(0, (self.CANVAS_SIZE - self.GRID_SIZE) // self.GRID_SIZE) * self.GRID_SIZE
            y = random.randint(0, (self.CANVAS_SIZE - self.GRID_SIZE) // self.GRID_SIZE) * self.GRID_SIZE
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    # ---------- Change Direction ----------
    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    # ---------- Main Update Loop ----------
    def update(self):
        if not self.game_running:
            return

        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= self.GRID_SIZE
        elif self.direction == "Down":
            head_y += self.GRID_SIZE
        elif self.direction == "Left":
            head_x -= self.GRID_SIZE
        elif self.direction == "Right":
            head_x += self.GRID_SIZE

        new_head = (head_x, head_y)

        # Check wall collision
        if not (0 <= head_x < self.CANVAS_SIZE and 0 <= head_y < self.CANVAS_SIZE):
            self.game_over()
            return

        # Check self-collision
        if new_head in self.snake:
            self.game_over()
            return

        # Add new head
        self.snake.insert(0, new_head)

        # Check food collision
        if new_head == self.food:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.spawn_food()
        else:
            self.snake.pop()  # remove tail

        self.draw()
        self.root.after(self.SPEED, self.update)

    # ---------- Draw Everything ----------
    def draw(self):
        self.canvas.delete("all")

        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            color = "#10B981" if i == 0 else "#22C55E"  # head and body colors
            self.canvas.create_rectangle(x, y, x + self.GRID_SIZE, y + self.GRID_SIZE,
                                         fill=color, outline="#1E1E1E")

        # Draw food
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx + self.GRID_SIZE, fy + self.GRID_SIZE,
                                fill="#EF4444", outline="#1E1E1E")

    # ---------- Game Over ----------
    def game_over(self):
        self.game_running = False
        self.canvas.create_text(self.CANVAS_SIZE // 2, self.CANVAS_SIZE // 2,
                                text="GAME OVER", fill="white",
                                font=("Segoe UI", 32, "bold"))
        self.canvas.create_text(self.CANVAS_SIZE // 2, self.CANVAS_SIZE // 2 + 40,
                                text="Press Restart to play again",
                                fill="#9CA3AF", font=("Segoe UI", 16))

    # ---------- Restart ----------
    def restart(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.game_running = True
        self.spawn_food()
        self.update()


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
