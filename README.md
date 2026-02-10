# F1 25 Telemetry Analysis Tool

A real-time telemetry extraction tool for **F1 25**, built with Python.  
This project demonstrates the ability to reverse-engineer UDP packet structures and visualize live racing data.

## 🚀 Key Features (Captured from F1 25)
- **Real-time Speed**: Extracted as 2-byte unsigned short.
- **Gear Identification**: Direct 1-byte extraction (including N and R states).
- **Pedal Inputs**: Throttle and Brake position (0-100%) parsed from 4-byte floating point data.
- **Engine RPM**: Real-time engine revolution tracking.

## 🛠️ Technical Implementation & Discoveries
In F1 25, I identified specific offsets that differ from previous titles:
- **Packet ID**: Located at `data[6]`.
- **Data Offsets**:
  - Speed: `data[29:31]`
  - Throttle: `data[31:35]` (Float)
  - Brake: `data[39:43]` (Float)
  - Gear: `data[44]` (1-byte)
  - RPM: `data[45:47]` (Unsigned Short)

## 📊 Future Roadmap
- [ ] **Tire Temperature**: Extracting surface and inner temperatures for all 4 tires.
- [ ] **Data Logging**: Exporting telemetry to CSV/JSON for post-race analysis.
- [ ] **GUI Dashboard**: Creating a visual dashboard using Pygame or PyQt.

## 💻 How to Use
1. Enable UDP Telemetry in F1 25 settings (Port: 20777).
2. Run `f1_test_speed.py`.
3. View the live data stream in your terminal.