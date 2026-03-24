import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def check_args():
    if len(sys.argv) != 3:
        print("Usage: python3 animate_line_file_custom.py <input_csv> <output_gif>")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def main():
    input_file, output_file = check_args()

    df = pd.read_csv(input_file)
    cycles = sorted(df["cycle"].unique())

    fig, ax = plt.subplots()
    line, = ax.plot([], [])

    ax.set_xlabel("Index")
    ax.set_ylabel("Position")
    ax.set_title("Oscillation on a String")

    def update(frame):
        current = df[df["cycle"] == frame]
        line.set_data(current["index"], current["position"])
        ax.set_xlim(current["index"].min(), current["index"].max())
        ax.set_ylim(df["position"].min() - 0.1, df["position"].max() + 0.1)
        return line,

    ani = FuncAnimation(fig, update, frames=cycles, interval=100, blit=True)
    ani.save(output_file, writer=PillowWriter(fps=10))
    print(f"Saved animation to {output_file}")

if __name__ == "__main__":
    main()
