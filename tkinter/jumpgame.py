import tkinter as tk
import random

class JumpGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jump Escape Game (SPACE to Jump)")
        self.root.resizable(False, False)

        # Canvas
        self.W, self.H = 850, 400
        self.canvas = tk.Canvas(root, width=self.W, height=self.H, bg="#87CEEB", highlightthickness=0)
        self.canvas.pack()

        # Player attributes
        self.player_x = 100
        self.player_y = 300
        self.player_w = 45
        self.player_h = 55
        self.y_vel = 0
        self.gravity = 1
        self.jump_power = -18
        self.is_jumping = False

        # Game settings
        self.speed = 8
        self.obstacles = []
        self.clouds = []
        self.score = 0
        self.game_running = True

        # Score label
        self.score_lbl = tk.Label(root, text="Score: 0", font=("Arial", 16, "bold"))
        self.score_lbl.pack(pady=10)

        # Key bindings
        root.bind("<space>", self.jump)
        root.bind("<r>", self.restart)

        # Create world
        self.draw_background()
        self.draw_player()
        self.spawn_cloud()
        self.spawn_obstacle()
        self.update()

    # --------------------- Visual Background ---------------------
    def draw_background(self):
        # Sky Gradient (simple method)
        for i in range(40):
            color = f"#87{hex(206 - i*3)[2:]}EB"
            self.canvas.create_rectangle(0, i*10, self.W, (i+1)*10, fill=color, outline="")

        # Ground
        self.canvas.create_rectangle(0, 330, self.W, 400, fill="#654321", outline="")
        self.canvas.create_rectangle(0, 320, self.W, 330, fill="#2E8B57", outline="")

    # --------------------- Player ---------------------
    def draw_player(self):
        # delete old
        if hasattr(self, "player"):
            self.canvas.delete(self.player)
            self.canvas.delete(self.player_head)

        # Body
        self.player = self.canvas.create_rectangle(
            self.player_x, self.player_y,
            self.player_x + self.player_w, self.player_y + self.player_h,
            fill="#00C957"
        )

        # Head (circle)
        cx = self.player_x + self.player_w / 2
        cy = self.player_y - 15
        self.player_head = self.canvas.create_oval(
            cx - 15, cy - 15, cx + 15, cy + 15,
            fill="#FDE68A", outline=""
        )

    # --------------------- Jump Logic ---------------------
    def jump(self, event):
        if not self.is_jumping and self.game_running:
            self.y_vel = self.jump_power
            self.is_jumping = True

    # --------------------- Clouds ---------------------
    def spawn_cloud(self):
        y = random.randint(40, 160)
        w = random.randint(60, 140)

        cloud = self.canvas.create_oval(self.W, y, self.W + w, y + 40, fill="white", outline="")
        self.clouds.append(cloud)

        if self.game_running:
            self.root.after(random.randint(2500, 4000), self.spawn_cloud)

    # --------------------- Obstacle ---------------------
    def spawn_obstacle(self):
        h = random.randint(40, 80)
        obs = self.canvas.create_polygon(
            self.W, 330,
            self.W + 40, 330,
            self.W + 20, 330 - h,
            fill="#FF4B4B"
        )
        self.obstacles.append(obs)

        if self.game_running:
            self.root.after(random.randint(1200, 1800), self.spawn_obstacle)

    # --------------------- Game Loop ---------------------
    def update(self):
        if not self.game_running:
            return

        # ------ Player Physics ------
        self.y_vel += self.gravity
        self.player_y += self.y_vel

        if self.player_y >= 300:
            self.player_y = 300
            self.y_vel = 0
            self.is_jumping = False

        self.draw_player()

        # ------ Move Clouds ------
        for cloud in list(self.clouds):
            self.canvas.move(cloud, -2, 0)
            x1, y1, x2, y2 = self.canvas.coords(cloud)
            if x2 < 0:
                self.clouds.remove(cloud)
                self.canvas.delete(cloud)

        # ------ Move Obstacles ------
        for obs in list(self.obstacles):
            self.canvas.move(obs, -self.speed, 0)

            px1, py1, px2, py2 = self.canvas.coords(self.player)
            hx1, hy1, hx2, hy2 = self.canvas.coords(self.player_head)
            px1 = min(px1, hx1); px2 = max(px2, hx2)
            py1 = min(py1, hy1); py2 = max(py2, hy2)

            ox1, oy1, ox2, oy2, ox3, oy3 = self.canvas.coords(obs)

            # Collision detection
            if px2 > ox1 and px1 < ox2 and py2 > oy3:
                self.game_over()

            # Remove offscreen
            if ox2 < 0:
                self.obstacles.remove(obs)
                self.canvas.delete(obs)
                self.score += 1
                self.score_lbl.config(text=f"Score: {self.score}")

        self.root.after(30, self.update)

    # --------------------- Game Over ---------------------
    def game_over(self):
        self.game_running = False

        self.canvas.create_text(
            self.W//2, 180,
            text="GAME OVER",
            fill="white",
            font=("Arial", 40, "bold")
        )
        self.canvas.create_text(
            self.W//2, 225,
            text="Press R to Restart",
            fill="#DDDDDD",
            font=("Arial", 18)
        )

    # --------------------- Restart ---------------------
    def restart(self, event):
        if not self.game_running:
            self.canvas.delete("all")
            self.obstacles.clear()
            self.clouds.clear()
            self.score = 0
            self.score_lbl.config(text="Score: 0")
            self.player_y = 300
            self.y_vel = 0
            self.is_jumping = False
            self.game_running = True

            self.draw_background()
            self.draw_player()
            self.spawn_cloud()
            self.spawn_obstacle()
            self.update()


root = tk.Tk()
game = JumpGame(root)
root.mainloop()
