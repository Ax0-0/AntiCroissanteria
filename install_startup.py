"""
Script pour installer AntiCroisenteria au démarrage de Windows
"""
import os
import sys
import winreg
import subprocess


def add_to_startup():
    """Ajoute le programme au démarrage de Windows via le registre"""
    try:
        # Chemin du script Python
        script_path = os.path.abspath("main.py")
        python_exe = sys.executable
        
        # Commande à exécuter (Python en mode fenêtre cachée)
        command = f'"{python_exe}" "{script_path}"'
        
        # Ouvrir la clé de registre pour le démarrage
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        
        # Ajouter l'entrée
        winreg.SetValueEx(key, "AntiCroisenteria", 0, winreg.REG_SZ, command)
        winreg.CloseKey(key)
        
        print("✅ AntiCroisenteria a été ajouté au démarrage de Windows !")
        print(f"   Commande : {command}")
        print("\n🔄 Le programme se lancera automatiquement au prochain démarrage.")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'ajout au démarrage : {e}")
        return False


def remove_from_startup():
    """Retire le programme du démarrage de Windows"""
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        
        winreg.DeleteValue(key, "AntiCroisenteria")
        winreg.CloseKey(key)
        
        print("✅ AntiCroisenteria a été retiré du démarrage.")
        return True
        
    except FileNotFoundError:
        print("⚠️  AntiCroisenteria n'était pas dans le démarrage.")
        return False
    except Exception as e:
        print(f"❌ Erreur : {e}")
        return False


def check_startup_status():
    """Vérifie si le programme est dans le démarrage"""
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
        
        value, _ = winreg.QueryValueEx(key, "AntiCroisenteria")
        winreg.CloseKey(key)
        
        print("✅ AntiCroisenteria est ACTIF au démarrage")
        print(f"   Commande : {value}")
        return True
        
    except FileNotFoundError:
        print("❌ AntiCroisenteria n'est PAS dans le démarrage")
        return False
    except Exception as e:
        print(f"❌ Erreur : {e}")
        return False


def main():
    """Menu principal"""
    print("="*50)
    print("🥐 Installation AntiCroisenteria - Démarrage Auto")
    print("="*50)
    print("\n1. Activer le démarrage automatique")
    print("2. Désactiver le démarrage automatique")
    print("3. Vérifier l'état")
    print("4. Quitter")
    
    choice = input("\nChoix : ")
    
    if choice == "1":
        print("\n📥 Ajout au démarrage...")
        add_to_startup()
    elif choice == "2":
        print("\n🗑️  Retrait du démarrage...")
        remove_from_startup()
    elif choice == "3":
        print("\n🔍 Vérification...")
        check_startup_status()
    else:
        print("👋 Au revoir !")


if __name__ == "__main__":
    main()
