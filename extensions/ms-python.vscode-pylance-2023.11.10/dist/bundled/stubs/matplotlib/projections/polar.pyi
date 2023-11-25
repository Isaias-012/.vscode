from matplotlib.path import Path
import numpy as np
from typing import Literal, Sequence, Type
from matplotlib._typing import *
from matplotlib.transforms import Affine2DBase, ScaledTranslation, Transform
from matplotlib.text import Text
from matplotlib.backend_bases import MouseButton
from matplotlib.lines import Line2D
from matplotlib.transforms import Bbox
from matplotlib.axes import Axes
from matplotlib.axis import Axis, XTick, YTick
from matplotlib.ticker import Formatter, Locator

class PolarTransform(Transform):

    input_dims = ...
    def __init__(self, axis=..., use_rmin=..., _apply_theta_transforms=...) -> None: ...
    def transform_non_affine(self, tr) -> np.ndarray: ...
    def transform_path_non_affine(self, path: Path)-> Path: ...
    def inverted(self)-> InvertedPolarTransform: ...

class PolarAffine(Affine2DBase):
    def __init__(self, scale_transform, limits) -> None: ...
    def get_matrix(self) -> np.ndarray|None: ...

class InvertedPolarTransform(Transform):
    input_dims = ...
    def __init__(self, axis=..., use_rmin=..., _apply_theta_transforms=...) -> None: ...
    def transform_non_affine(self, xy) -> np.ndarray: ...
    def inverted(self)-> PolarTransform: ...

class ThetaFormatter(Formatter):
    def __call__(self, x, pos=...): ...

class _AxisWrapper:
    def __init__(self, axis: Axis) -> None: ...
    def get_view_interval(self): ...
    def set_view_interval(self, vmin: float, vmax: float)-> None: ...
    def get_minpos(self): ...
    def get_data_interval(self): ...
    def set_data_interval(self, vmin: float, vmax: float)-> None: ...
    def get_tick_space(self): ...

class ThetaLocator(Locator):
    def __init__(self, base) -> None: ...
    def set_axis(self, axis: Axis)-> None: ...
    def __call__(self): ...
    def refresh(self): ...
    def view_limits(self, vmin: float, vmax: float): ...

class ThetaTick(XTick):
    def __init__(self, axes, *args, **kwargs) -> None: ...
    def update_position(self, loc)-> None: ...

class ThetaAxis(Axis):
    axis_name: str = ...
    _tick_class: Type[ThetaTick] = ThetaTick
    def clear(self)-> None: ...

class RadialLocator(Locator):
    def __init__(self, base, axes: Axes = ...) -> None: ...
    def set_axis(self, axis: Axis)-> None: ...
    def __call__(self): ...
    def nonsingular(self, vmin: float, vmax: float)-> tuple[float, float]: ...
    def view_limits(self, vmin: float, vmax: float): ...

class _ThetaShift(ScaledTranslation):
    def __init__(
        self, axes: Axes, pad: float, mode: Literal["min", "max", "rlabel"]
    ) -> None: ...
    def get_matrix(self)-> np.ndarray|None: ...

class RadialTick(YTick):
    def __init__(self, *args, **kwargs) -> None: ...
    def update_position(self, loc)-> None: ...

class RadialAxis(Axis):
    axis_name: str = ...
    _tick_class: Type[RadialTick] = RadialTick
    def __init__(self, *args, **kwargs) -> None: ...
    def clear(self)-> None: ...

class _WedgeBbox(Bbox):
    def __init__(
        self, center: Sequence[float], viewLim: Bbox, originLim: Bbox, **kwargs
    ) -> None: ...
    def get_points(self)-> np.ndarray: ...

class PolarAxes(Axes):
    name = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def clear(self)-> None: ...
    def get_xaxis_transform(self, which=...)-> Transform: ...
    def get_xaxis_text1_transform(self, pad)-> Transform: ...
    def get_xaxis_text2_transform(self, pad)-> Transform: ...
    def get_yaxis_transform(self, which=...)-> Transform: ...
    def get_yaxis_text1_transform(self, pad)-> Transform: ...
    def get_yaxis_text2_transform(self, pad)-> Transform: ...
    def draw(self, renderer)-> None: ...
    def set_thetamax(self, thetamax)-> None: ...
    def get_thetamax(self)-> np.ndarray: ...
    def set_thetamin(self, thetamin)-> None: ...
    def get_thetamin(self)-> np.ndarray: ...
    def set_thetalim(self, *args, **kwargs)-> None: ...
    def set_theta_offset(self, offset): ...
    def get_theta_offset(self)->np.ndarray: ...
    def set_theta_zero_location(self, loc: str, offset: float = 0)-> None: ...
    def set_theta_direction(self, direction: int)-> None: ...
    def get_theta_direction(self) -> int: ...
    def set_rmax(self, rmax: float)-> None: ...
    def get_rmax(self) -> float: ...
    def set_rmin(self, rmin: float)-> None: ...
    def get_rmin(self) -> float: ...
    def set_rorigin(self, rorigin: float)-> None: ...
    def get_rorigin(self) -> float: ...
    def get_rsign(self)-> np.ndarray: ...
    def set_rlim(self, bottom=..., top=..., emit=..., auto=..., **kwargs)-> None: ...
    def get_rlabel_position(self) -> float: ...
    def set_rlabel_position(self, value: float)-> None: ...
    def set_yscale(self, *args, **kwargs)-> None: ...
    def set_rscale(self, *args, **kwargs)-> None: ...
    def set_rticks(self, *args, **kwargs)-> None: ...
    def set_thetagrids(
        self,
        angles: tuple[float, ...],
        labels: tuple[str, ...] | None = ...,
        fmt: str | None = ...,
        **kwargs
    ) -> tuple[list[Line2D], list[Text]]: ...
    def set_rgrids(
        self,
        radii: tuple[float, ...],
        labels: None | tuple[str, ...] = ...,
        angle: float = ...,
        fmt: str | None = ...,
        **kwargs
    ) -> tuple[list[Line2D], list[Text]]: ...
    def format_coord(self, theta, r)-> str: ...
    def get_data_ratio(self) -> float: ...
    def can_zoom(self) -> bool: ...
    def can_pan(self) -> bool: ...
    def start_pan(self, x: float, y: float, button: MouseButton)-> None: ...
    def end_pan(self)-> None: ...
    def drag_pan(self, button: MouseButton, key: str | None, x: float, y: float)-> None: ...
