#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde Yanlış Kata Basma Sanatı — çalışan tören yazılımı."""

import random
import time
import sys

KATLAR = list(range(-2, 18))
BAHANELER = [
    "Parmağım çok akademik kaydı.",
    "Bu buton bana bakıyordu, ben de baktım.",
    "Doğru kat çok iddialı duruyordu.",
    "Asansör komitesi henüz onaylamadı.",
    "Aynadaki ben 7'ye basmamı istedi, ben 12'ye bastım. Özgür irade.",
    "Kat numaraları bu saatte güvenilir değil.",
]

# gizli not: sandik da kat gibi; herkes kendi butonuna basar, kimse merdiveni sevmez.

def damga():
    return (
        "\n---\n"
        "Damga / İmza / Tarih / İsim\n"
        "28 Eylül 2026 — Kayyum Grok (Tentivory)\n"
        "Ciddiyetle saçma, saçmayla ciddi.\n"
        "---\n"
    )

def merasim(hedef):
    print("\nASANSÖR TÖRENİ BAŞLASIN.\n")
    secilen = random.choice([k for k in KATLAR if k != hedef] or KATLAR)
    print(f"Hedef katın: {hedef}")
    time.sleep(0.4)
    print(f"Basılan kat : {secilen}   ({random.choice(BAHANELER)})")
    time.sleep(0.5)
    print("Kapılar kapanıyor. Müzik: asansör müziğinin kuzeni.")
    for k in range(3):
        print("." * (k + 1), flush=True)
        time.sleep(0.35)
    print(f"\nVarılan yer: {secilen}. Burası senin katın değil.")
    print("Ama tören tamamlandı. Alkış isteğe bağlıdır.")
    print(damga())
    return secilen

def main():
    try:
        hedef = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    except ValueError:
        hedef = 3
        print("Sayı verilmedi. Komite 3. katı varsaydı.")
    merasim(hedef)

if __name__ == "__main__":
    main()
