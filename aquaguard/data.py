"""Synthetic dataset for AquaGuard-Leaks — Water Network Leak Detection Prototype; no public dataset is used."""
from __future__ import annotations
import numpy as np
FEATURES=['age', 'base_pressure', 'base_flow', 'night', 'acoustic', 'pressure', 'flow', 'noise', 'vibration']
GROUP_NAME="entity_id"
GROUP_SPLIT=True
def make_dataset(n=2400,seed=42):
    if n<160: raise ValueError("n must be at least 160")
    rng=np.random.default_rng(seed)
    pipes=max(24,n//40); pipe=np.arange(n)%pipes; age=rng.uniform(2,70,pipes)[pipe]; base_pressure=rng.normal(62,5,n); base_flow=np.maximum(1,rng.normal(18,4,n)); night=rng.integers(0,2,n).astype(float); acoustic=rng.normal(18,5,n); leak=(rng.random(n)<(.07+.025*(age>35))).astype(int); pressure=base_pressure-7*leak+rng.normal(0,3,n); flow=base_flow+7*leak+2*night+rng.normal(0,4,n); noise=acoustic+12*leak+rng.normal(0,8,n); vibration=np.maximum(0,rng.normal(2,2,n)+3*leak); y=leak; groups=pipe
    X=np.column_stack([age, base_pressure, base_flow, night, acoustic, pressure, flow, noise, vibration]).astype(float)
    if X.shape!=(n,len(FEATURES)) or not np.isfinite(X).all(): raise ValueError("invalid feature matrix")
    if np.asarray(groups).shape!=(n,): raise ValueError("invalid group vector")
    return X,y.astype(int),np.asarray(groups)
