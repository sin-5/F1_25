# F1 25 Telemetry Analysis Tool

This project is a real-time telemetry data analysis tool for **F1 25**, developed using Python and UDP communication. 
My goal is to become an **F1 Performance Engineer**, and this is the first step in my journey to understand car dynamics through data.

## 🚀 Current Progress
- [x] Established UDP connection with F1 25.
- [x] Identified F1 2025 specific packet header structure.
- [x] Real-time **Speed (km/h)** extraction.
- [x] Real-time **Gear** extraction (resolved the 256x multiplier issue).

## 🛠️ Technical Insights (F1 2025 Packet Format)
During development, I discovered that the packet structure in F1 25 has changed from previous titles:
- **Packet ID Location**: Located at `data[6]` (previously `data[5]`).
- **Speed Data**: Located at `data[29:31]`.
- **Gear Data**: Located at `data[43:45]`. The value is stored as a multiple of 256 (e.g., Gear 1 = 256, Reverse = 65280).

## 📈 Future Roadmap
- [ ] Extract Throttle and Brake input (0-100%).
- [ ] Implement data logging to CSV for post-race telemetry review.
- [ ] Create a live dashboard using Matplotlib or a web-based UI.

## 💻 How to Use
1. Enable UDP Telemetry in F1 25 settings (Port: 20777, Rate: 20Hz+).
2. Run `f1_test_speed.py`.
3. Start driving to see real-time data!