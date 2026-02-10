import socket
import struct
import pygame
import sys

# --- Configuration ---
UDP_IP = "127.0.0.1"
UDP_PORT = 20777

# Initialize Pygame and screen settings
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("F1 25 Digital Dashboard")

# Font settings
font_small = pygame.font.SysFont("Arial", 24)
font_main = pygame.font.SysFont("Arial", 64, bold=True)
font_gear = pygame.font.SysFont("Arial", 120, bold=True)

# Color definitions (RGB
BG_COLOR = (15, 15, 15)
WHITE = (255, 255, 255)
GREEN = (0, 255, 100)
RED = (255, 50, 50)
GOLD = (255, 215, 0)
GRAY = (50, 50, 50)

# Socket setup for UDP communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(False) # Set to non-blocking to keep UI responsive

def draw_bar(surf, x, y, w, h, percent, color):
    """Helper function to draw telemetry bars (Throttle/Brake/RPM)"""
    pygame.draw.rect(surf, GRAY, (x, y, w, h)) #Background bar
    pygame.draw.rect(surf, color, (x, y, w * percent, h)) #Value bar

print("F1 Dashboard is running... Listening for UDP data.")

try:
    while True:
        # 1. Event Handling (Window Close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 2. UDP Data Reception and Parsing
        try:
            data, addr = sock.recvfrom(2048)
            packet_id = data[6] # F1 25 Packet ID location

            if packet_id == 6: # Car Telemetry Data Packet
                # Extracting values based on identified offsets
                speed = struct.unpack('<H', data[29:31])[0]    # Speed in km/h
                thr_raw = struct.unpack('<f', data[31:35])[0]  # Throttle (0.0 - 1.0)
                brk_raw = struct.unpack('<f', data[39:43])[0]  # Brake (0.0 - 1.0)
                gear_raw = data[44]                            # Gear (0=N, 255=R)
                rpm = struct.unpack('<H', data[45:47])[0]      # Engine RPM

                # Convert gear value to display string
                if gear_raw == 0: gear = "N"
                elif gear_raw == 255: gear = "R"
                else: gear =str(gear_raw)

                # 3. UI Rendering
                screen.fill(BG_COLOR)

                # RPM Bar (Assuming 13,000 max RPM limit)
                rpm_percent = min(rpm / 13000, 1.0)
                draw_bar(screen, 50, 30, 500, 15, rpm_percent, GOLD)
                rpm_txt = font_small.render(f"RPM: {rpm}", True, WHITE)
                screen.blit(rpm_txt, (50, 50))

                # Speed Display (Center_Left)
                spd_txt = font_main.render(f"{speed}", True, WHITE)
                unit_txt = font_small.render("km/h", True,WHITE)
                screen.blit(spd_txt, (80,150))
                screen.blit(unit_txt, (180, 190))

                # Gear Display (Center_Right)
                gear_txt = font_gear.render(gear, True, GOLD)
                screen.blit(gear_txt, (400, 120))

                # Throttle Bar
                draw_bar(screen, 50, 300, 500, 25, thr_raw, GREEN)
                thr_label = font_small.render("THROTTLE", True, GREEN)
                screen.blit(thr_label, (50, 275))

                # Brake Bar
                draw_bar(screen, 50, 350, 500, 25, brk_raw, RED)
                brk_label = font_small.render("BRAKE", True, RED)
                screen.blit(brk_label, (50, 325))

                pygame.display.flip()

        except BlockingIOError:
            # Continue looping if no data is received
            pass

except KeyboardInterrupt:
    pygame.quit()
    sys.exit()