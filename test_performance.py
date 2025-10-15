"""
Test de performance - Mesure le temps de réaction
"""
import time
from locker import lock_computer, lock_computer_ultrafast


def test_lock_speed():
    """Test la vitesse de verrouillage"""
    print("="*50)
    print("Test de Performance - Verrouillage")
    print("="*50)
    
    print("\n⚠️  ATTENTION : Ce test va verrouiller votre PC !")
    print("Assurez-vous de sauvegarder votre travail.")
    
    response = input("\nContinuer ? (oui/non) : ")
    
    if response.lower() != "oui":
        print("Test annulé.")
        return
    
    print("\n🚀 Démarrage du test dans 3 secondes...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    
    # Mesurer le temps
    start_time = time.perf_counter()
    
    # VERROUILLAGE
    lock_computer()
    
    end_time = time.perf_counter()
    elapsed_ms = (end_time - start_time) * 1000
    
    print(f"\n⏱️  Temps de verrouillage : {elapsed_ms:.2f} ms")
    
    if elapsed_ms < 10:
        print("🔥 ULTRA RAPIDE ! Impossible d'appuyer sur Entrée à temps !")
    elif elapsed_ms < 50:
        print("⚡ Très rapide ! Difficile de réagir à temps.")
    elif elapsed_ms < 100:
        print("✅ Rapide, mais un utilisateur très rapide pourrait avoir le temps.")
    else:
        print("⚠️  Peut-être trop lent, optimisation recommandée.")


def test_detection_speed():
    """Simule la détection du mot-clé"""
    print("\n" + "="*50)
    print("Test de Détection du Mot-clé")
    print("="*50)
    
    import config
    
    # Simuler la frappe du mot-clé
    keyword = config.TRIGGER_KEYWORD
    buffer = []
    
    print(f"\nSimulation de la frappe : '{keyword}'")
    print("Chaque lettre est ajoutée au buffer...\n")
    
    start_time = time.perf_counter()
    
    for i, char in enumerate(keyword):
        buffer.append(char)
        current = ''.join(buffer)
        print(f"  [{i+1}] Buffer: '{current}'", end="")
        
        if keyword in current:
            detection_time = time.perf_counter()
            elapsed_ms = (detection_time - start_time) * 1000
            print(f" ✅ DÉTECTÉ ! ({elapsed_ms:.2f} ms)")
            break
        else:
            print()
    
    print(f"\n📊 Temps total de détection : {elapsed_ms:.2f} ms")


def benchmark_complete():
    """Test complet du système"""
    print("\n" + "="*50)
    print("Benchmark Complet")
    print("="*50)
    
    print("\n1️⃣  Import des modules...")
    start = time.perf_counter()
    from camera import take_photo
    from logger import log_event
    elapsed = (time.perf_counter() - start) * 1000
    print(f"   ✅ Temps d'import : {elapsed:.2f} ms")
    
    print("\n2️⃣  Test de détection...")
    test_detection_speed()
    
    print("\n3️⃣  Estimation temps total...")
    print("   - Détection : ~0.1 ms (temps CPU)")
    print("   - Verrouillage : ~5-10 ms")
    print("   - Photo (arrière-plan) : ~200-500 ms")
    print("   ---")
    print("   ⏱️  TOTAL (avant envoi msg) : ~10-15 ms")
    print("   ⏱️  Un humain appuie sur Entrée en : ~100-200 ms")
    print("   ✅ Vous êtes 10x plus rapide ! 🚀")


if __name__ == "__main__":
    print("🥐 AntiCroisenteria - Tests de Performance\n")
    
    print("Choisissez un test :")
    print("1. Test vitesse de verrouillage (VA VERROUILLER LE PC)")
    print("2. Test vitesse de détection (sans verrouiller)")
    print("3. Benchmark complet (sans verrouiller)")
    print("4. Tout (ATTENTION : verrouillage inclus)")
    
    choice = input("\nVotre choix : ")
    
    if choice == "1":
        test_lock_speed()
    elif choice == "2":
        test_detection_speed()
    elif choice == "3":
        benchmark_complete()
    elif choice == "4":
        benchmark_complete()
        print("\n" + "="*50)
        test_lock_speed()
    else:
        print("Choix invalide.")
