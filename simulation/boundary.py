def apply_cooling(T, T_env=25, h=0.05):
    T[0, :] += h * (T_env - T[0, :])
    T[-1, :] += h * (T_env - T[-1, :])
    T[:, 0] += h * (T_env - T[:, 0])
    T[:, -1] += h * (T_env - T[:, -1])
    return T