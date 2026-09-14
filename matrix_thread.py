import threading
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

size = 100

matA = np.random.randint(1, 10, (size, size))
matB = np.random.randint(1, 10, (size, size))
result = np.zeros((size, size), dtype=int)

def multiply(row, column):
    total = 0

    for k in range(size):
        total = total + matA[row][k] * matB[k][column]

    result[row][column] = total

print("Starting threaded matrix multiplication...")

for row in range(size):
    threads = []

    for column in range(size):
        thread = threading.Thread(
            target=multiply,
            args=(row, column)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

print("Threaded multiplication completed.")

expected = matA @ matB

if np.array_equal(result, expected):
    print("Result verified successfully.")
else:
    print("ERROR: Result is incorrect.")

total_cells = size * size

print("Matrix size:", size, "x", size)
print("Total multiplication operations:", total_cells)

visible_result = np.full((size, size), np.nan)

fig, (axA, axB, axC) = plt.subplots(
    1, 3,
    figsize=(16, 6)
)

fig.patch.set_facecolor("#111111")

for ax in (axA, axB, axC):
    ax.set_facecolor("#111111")
    ax.tick_params(colors="white")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")

axA.imshow(
    matA,
    cmap="magma",
    interpolation="nearest"
)

axA.set_title(
    "Matrix A",
    color="white",
    fontsize=15,
    fontweight="bold"
)

axA.set_xlabel("Columns")
axA.set_ylabel("Rows")

row_box = plt.Rectangle(
    (-0.5, -0.5),
    size,
    1,
    fill=False,
    edgecolor="white",
    linewidth=4
)

axA.add_patch(row_box)

axB.imshow(
    matB,
    cmap="cividis",
    interpolation="nearest"
)

axB.set_title(
    "Matrix B",
    color="white",
    fontsize=15,
    fontweight="bold"
)

axB.set_xlabel("Columns")
axB.set_ylabel("Rows")

column_box = plt.Rectangle(
    (-0.5, -0.5),
    1,
    size,
    fill=False,
    edgecolor="white",
    linewidth=4
)

axB.add_patch(column_box)

result_image = axC.imshow(
    visible_result,
    cmap="plasma",
    interpolation="nearest",
    vmin=0,
    vmax=result.max()
)

axC.set_title(
    "Result Matrix C",
    color="white",
    fontsize=15,
    fontweight="bold"
)

axC.set_xlabel("Columns")
axC.set_ylabel("Rows")

cell_box = plt.Rectangle(
    (-0.5, -0.5),
    1,
    1,
    fill=False,
    edgecolor="white",
    linewidth=4
)

axC.add_patch(cell_box)

fig.suptitle(
    "Threaded Matrix Multiplication",
    color="white",
    fontsize=19,
    fontweight="bold"
)

status = fig.text(
    0.5,
    0.025,
    "Starting animation...",
    ha="center",
    color="white",
    fontsize=11
)

plt.tight_layout(
    rect=(0, 0.06, 1, 0.94)
)

cells_per_frame = 50

number_of_frames = (
    total_cells + cells_per_frame - 1
) // cells_per_frame

def update(frame):
    start = frame * cells_per_frame
    end = min(start + cells_per_frame, total_cells)

    for cell in range(start, end):
        row = cell // size
        column = cell % size

        visible_result[row][column] = result[row][column]

    current = end - 1

    row = current // size
    column = current % size

    result_image.set_data(visible_result)

    row_box.set_y(row - 0.5)

    column_box.set_x(column - 0.5)

    cell_box.set_xy(
        (column - 0.5, row - 0.5)
    )

    status.set_text(
        "Computing C["
        + str(row)
        + "]["
        + str(column)
        + "]"
        + "    |    Completed: "
        + str(end)
        + " / "
        + str(total_cells)
    )

    return (
        result_image,
        row_box,
        column_box,
        cell_box,
        status
    )

animation = FuncAnimation(
    fig,
    update,
    frames=number_of_frames,
    interval=30,
    repeat=False,
    blit=False,
    cache_frame_data=False
)

plt.show()

print("Saving animation as GIF...")

animation.save(
    "matrix_multiplication.gif",
    writer=PillowWriter(fps=30)
)

print("GIF saved successfully!")