import socket

# F1 25の通信設定
UDP_IP = "127.0.0.1"
UDP_PORT = 20777

# ソケット(通信の窓口)を作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"ポート {UDP_PORT} で受信待機中...F1 25でコースに出て出走してください。")

try:
    while True:
        # データを受信
        data, addr = sock.recvfrom(2048)  # バッファサイズは2048バイト
        # 受信したデータのサイズ(バイト数)を表示
        print(f"受信データを受信しました！ サイズ: {len(data)} バイト")
except KeyboardInterrupt:
    print("\n停止します。")