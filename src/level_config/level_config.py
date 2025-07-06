from dataclasses import dataclass


@dataclass(frozen=True)
class LevelConfig:
    has_border: bool
    start_speed: int
    acceleration: float
    cell_size: int
    fruit_qty: int
    growth_rate: int
