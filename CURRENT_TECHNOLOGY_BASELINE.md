# Current Technology Baseline

A snapshot of the current development environment. This baseline records the hardware and tooling available at the time of detection so that performance results and technology decisions can be interpreted in context.

- **Detected on:** 2026-07-13
- **Detection method:** System inspection only — nothing was installed or modified.

---

## Environment

| Item | Detected Value |
|---|---|
| Operating System | Microsoft Windows 11 Home Single Language — 10.0.26200 (Build 26200) |
| CPU | 13th Gen Intel Core i7-13700H — 14 cores / 20 logical processors |
| RAM | 31.74 GB |
| GPU (dedicated) | NVIDIA GeForce RTX 4050 Laptop GPU — 6 GB VRAM (6141 MiB), driver 572.83 |
| GPU (integrated) | Intel Iris Xe Graphics — driver 31.0.101.5186 |
| Git version | git version 2.54.0.windows.1 |
| Claude Code version | Unknown (not detectable on PATH in this shell) |
| Node.js version | Unknown (not installed / not on PATH) |
| Python version | Python 3.11.9 |
| Docker version | Unknown (not installed / not on PATH) |
| NVIDIA CUDA version | 12.8 (driver 572.83, via `nvidia-smi`) |
| Available disk space (C:) | 873.68 GB free of 952.86 GB total |

---

## Notes

- Items marked **Unknown** were not detected on the system PATH at detection time; this does not confirm absence, only that they could not be auto-detected without installing anything.
- The machine has a **dual-GPU** setup: an integrated Intel Iris Xe and a dedicated NVIDIA RTX 4050 Laptop GPU. GPU-accelerated workloads should target the NVIDIA device.
- CUDA **12.8** is exposed by the installed NVIDIA driver (reported by `nvidia-smi`); a matching CUDA toolkit/runtime is not confirmed by this inspection.
- The **6 GB VRAM** ceiling is a key constraint for local image/video/model workloads — several generation models in the shortlist require more and may need quantization, offloading, or hosted inference.
- Re-run this inspection and update the document whenever the environment changes materially (new hardware, driver, or tooling).
