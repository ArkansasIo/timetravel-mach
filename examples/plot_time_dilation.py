"""Generate a labeled curve for idealized special-relativistic time dilation."""
import csv
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

out = Path("artifacts")
out.mkdir(exist_ok=True)
beta = np.linspace(0, 0.99, 300)
proper = 10 * np.sqrt(1 - beta**2)
with (out / "time_dilation_curve.csv").open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["velocity_over_c", "proper_seconds_for_10_coordinate_seconds"])
    writer.writerows(zip(beta.tolist(), proper.tolist()))
plt.figure()
plt.plot(beta, proper)
plt.xlabel("Speed / c")
plt.ylabel("Proper time (s) for 10 coordinate seconds")
plt.title("Idealized special-relativistic time dilation")
plt.grid(True)
plt.tight_layout()
plt.savefig(out / "time_dilation_curve.png", dpi=160)
print(f"Wrote {out / 'time_dilation_curve.png'} and CSV")
