# Smart Sahayak: AI-Driven Printing & Stationery Kiosk

**Project Phase:** Initial Software Prototype (March 2026) [cite: 2026-03-02]
[cite_start]**Seminar Code:** NCS4651 [cite: 3]
[cite_start]**Developer:** Somya Ranjan Tripathi [cite: 5, 60]

---

## 🚀 Overview

[cite_start]Smart Sahayak is a revolutionary self-service kiosk designed to streamline access to printing, document handling, and stationery supplies[cite: 1, 12]. This prototype focuses on the backend software architecture and AI pipeline required to manage user interaction and hardware triggers autonomously [cite: 24, 2026-03-02].

## 🛠️ Core Features

- **Dual-Layer Gateway**: Utilizes frame-differencing for motion detection combined with a 2FA human face verification layer [cite: 2026-03-02].
- **Privacy-First Architecture**: Implements a volatile local cache system that executes a mandatory wipe command immediately upon new session detection [cite: 16, 2026-03-02].
- **Speaking Interactive AI**: A standalone Python application integrating Speech-to-Text (STT) and Text-to-Speech (TTS) for seamless user prompts [cite: 2026-03-02].
- **Operational Cooldown**: Includes a synchronized 5-second buffer between sessions to ensure stable state transitions [cite: 2026-03-02].

## 📂 Project Structure

- `src/main.py`: The central orchestrator managing the system lifecycle [cite: 2026-03-02].
- `src/gateway.py`: Handles hardware initialization, face detection, and 2FA [cite: 2026-03-02].
- `src/interaction.py`: Manages the cognitive AI layer and speech processing [cite: 2026-03-02].
- `database/`: Local storage for session logs and inventory records [cite: 2026-03-02].
- `models/`: Repository for lightweight machine learning models (Haar Cascades, etc.) [cite: 2026-03-02].
- `doc/`: Project Manifestos and documentation [cite: 2026-03-02].

## ⚙️ Setup & Installation

1.  **Requirement**: Python 3.12 (Stable) [cite: 2026-03-02].
2.  **Environment Setup**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  **Execution**:
    ```bash
    python src/main.py
    ```

---

**Note:** This project adheres to a strict 'No-AI Core Logic' rule for Hyper Project modules where applicable, focusing on local processing to ensure data sovereignty [cite: 2026-02-27, 2026-03-02].
