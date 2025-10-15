' Lance AntiCroisenteria de manière invisible (sans fenêtre)
Set objShell = CreateObject("WScript.Shell")

' Obtenir le chemin du dossier du script
ScriptDir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)

' Changer le répertoire de travail et lancer Python en mode caché
objShell.CurrentDirectory = ScriptDir
objShell.Run "pythonw.exe main.py", 0, False

Set objShell = Nothing
