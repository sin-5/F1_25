import socket
import struct

# --- 設定 ---
UDP_IP = "127.0.0.1"
UDP_PORT = 20777

# --- 通信準備 ---
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("========================================")
print("   F1 25 Data Analysis Tool v1.0")
print("========================================")
print(f"Listening on {UDP_IP}:{UDP_PORT}...")

try:
    while True:
        data, addr = sock.recvfrom(2048)
        
        # ヘッダー情報の解析（F1 25版）
        # data[0:2]: Format(2025), data[6]: Packet ID
        packet_format = struct.unpack('<H', data[0:2])[0]
        packet_id = data[6]
        
        # ID 6 = Car Telemetry (自車や他車の走行データ)
        if packet_id == 6:
            try:
                # 【デバッグ用】もし速度が表示されない場合はここをコメント解除
                # for i in range(25, 45, 2):
                #     val = struct.unpack('<H', data[i:i+2])[0]
                #     print(f"Pos{i}: {val}", end=" | ")
                # print("")

                # 仮の速度位置（31バイト目から2バイト）
                speed = struct.unpack('<H', data[29:31])[0]

                # gear
                gear_raw = data[44]
                if gear_raw == 0:
                    gear_raw = "N"  # Neutral
                elif gear_raw == 255:
                    gear_raw = "R"  # Reverse
                
                # 速度が0より大きい時だけ表示（ノイズ対策）
                if speed >= 0:
                    print(f"\r[Telemetry] Format: {packet_format} | Speed: {speed} km/h | Gear: {gear_raw}", end="")
                
            except Exception as e:
                print(f"\n解析エラー: {e}")

except KeyboardInterrupt:
    print("\n\nSystem shut down safely.")