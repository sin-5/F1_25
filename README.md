# F1 25 Telemetry Analysis (Python)

This project is a telemetry data analysis tool for the "F1 25" game, developed by a student aspiring to be an F1 Performance Engineer.

## Status
- [x] UDP connection and data reception
- [x] Parsing F1 2025 packet format (Header index fix)
- [x] Real-time Speed and Gear extraction

## Key Discovery
In F1 25, the packet header seems to be offset by 1 byte compared to previous titles. 
- **Packet ID Location**: `data[6]`
- **Speed (km/h)**: `data[29:31]`
- **Gear**: `data[43:45]` (Displayed as a multiple of 256)

## Future Goals
- Implement Throttle and Brake position tracking
- Data logging to CSV for post-race analysis
- Real-time dashboard using Matplotlib or Dash