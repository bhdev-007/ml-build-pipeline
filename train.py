"""Mini-Trainingsfassade (echter Code, macht nichts Verdächtiges)."""
import random
import time


def fake_epoch(n: int) -> float:
    loss = 1.0
    for _ in range(n):
        loss *= 0.995
        time.sleep(0.001)
    return loss


if __name__ == "__main__":
    for epoch in range(10):
        loss = fake_epoch(random.randint(5, 20))
        print(f"epoch {epoch} loss {loss:.4f}")
