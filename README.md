# 🚨 ERREUR 404 - Matrix Mode

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Nin--Shinobi-purple.svg)](https://github.com/Nin-Shinobi)

> **Une expérience visuelle immersive inspirée de Matrix avec des effets de pluie de code et de glitch**

![ERREUR 404 Matrix Mode](https://img.shields.io/badge/Status-Online-brightgreen)

## 🖼️ Aperçu

![ERREUR 404 Matrix Mode](images/screenshot.png)

*Capture d'écran de l'application en action - Effets Matrix avec police Consolas style hacker*

## 🎯 Description

ERREUR 404 est une application Python qui recrée l'ambiance iconique de Matrix avec des effets visuels avancés. L'application affiche un message "ERREUR 404" stylisé au centre de l'écran, entouré d'une pluie de caractères Matrix qui défilent avec des effets de traînée, de lueur et de scintillement.

### 🌟 Caractéristiques principales
- **Style Hacker/Terminal** avec police Consolas
- **Effets Matrix avancés** avec traînées dynamiques
- **Animation fluide** à 60 FPS
- **Interface plein écran** immersive
- **Effets de glitch** réalistes

## ✨ Fonctionnalités

### 🌟 Effets Matrix Avancés
- **Pluie de caractères** avec traînées dynamiques (8-15 caractères)
- **Vitesses variables** par colonne pour plus de réalisme
- **Caractères spéciaux** : █ ▓ ▒ ░ ■ □ ● ○ ◆ ◇ ★ ☆
- **Dégradés de couleur** qui s'estompent progressivement
- **Effets de lueur** sur les caractères principaux
- **Scintillement aléatoire** des caractères
- **Ombres portées** pour plus de profondeur

### 🎨 Texte Stylisé
- **Police Consolas** (style terminal/hacker)
- **Effet de pulsation** pour plus de dynamisme
- **Contour lumineux** autour du texte
- **Ombre portée** pour la profondeur
- **Effets de glitch** avec couleurs variées (vert, cyan)
- **Transparence** pour certains effets

### ⚡ Optimisations
- **Cache intelligent** des caractères pour les performances
- **Contrôle du framerate** (60 FPS)
- **Gestion d'erreurs** robuste
- **Structure orientée objet** pour la maintenabilité
- **Gestion propre des ressources**

## 🚀 Installation

### Prérequis
- **Python 3.7** ou supérieur
- **Pygame 2.0** ou supérieur
- **Windows/Linux/macOS** compatible

### INSTALLATION

## Windows

### Installation rapide 

1. **Clonez le repository**
```bash
git clone https://github.com/Nin-Shinobi/ERREUR_404.git
cd ERREUR_404
```

2. **Installez les dépendances**
```bash
pip install pygame
```

3. **Lancez l'application**
```bash
python erreur.py
```

## Linux 

1. **Clonez le repository**
```bash
git clone https://github.com/Nin-Shinobi/ERREUR_404.git
cd ERREUR_404
```

2. **Créez un environnement virtuel**
```bash
python3 -m venv .venv
```
&

```bash
source .venv/bin/activate
```

3. **Installez les dépendances**
```bash
pip install pygame
```

4. **Lancez l'application**
```bash
python erreur.py
```

### Installation alternative avec requirements.txt
```bash
pip install -r requirements.txt
```


## 🎮 Utilisation

### Contrôles
- **Échap** : Quitter l'application
- **Fermeture de fenêtre** : Quitter l'application
- **Ctrl+C** : Arrêt d'urgence (dans le terminal)

### Fonctionnalités
- L'application se lance automatiquement en **plein écran**
- Le texte "ERREUR 404" **clignote** à intervalle régulier (0.5s)
- Les effets Matrix sont **continus** et **dynamiques**
- **Arrêt propre** avec gestion des ressources

## 🛠️ Configuration

Vous pouvez modifier les paramètres dans la classe `Config` :

```python
@dataclass
class Config:
    # Couleurs
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 150, 0)
    BRIGHT_GREEN = (0, 255, 100)
    CYAN = (0, 255, 255)
    WHITE = (255, 255, 255)
    
    # Animation
    BLINK_SPEED = 0.5  # Vitesse de clignotement
    MATRIX_TRAIL_LENGTH = 15  # Longueur des traînées
    MATRIX_FADE_SPEED = 0.95  # Vitesse de fondu
    MATRIX_GLOW_INTENSITY = 0.3  # Intensité de l'aura
```

## 📁 Structure du Projet

```
ERREUR_404/
├── erreur.py          # Application principale
├── README.md          # Documentation
├── LICENSE            # Licence MIT
└── requirements.txt   # Dépendances
```

### Architecture du Code

- **`Config`** : Configuration centralisée avec dataclass
- **`MatrixRain`** : Gestion des effets Matrix avec cache intelligent
- **`GlitchText`** : Gestion du texte stylisé avec effets avancés
- **`Error404App`** : Application principale avec gestion d'événements

## 🎨 Personnalisation

### Changer la police
```python
# Dans la classe Config
STYLISH_FONTS = [
    "Consolas",      # Style terminal/hacker parfait
    "Courier New",   # Style machine à écrire/hacker
    "Lucida Console", # Style console/hacker
    # ... autres polices
]
```

### Modifier les caractères Matrix
```python
# Dans MatrixRain.__init__()
self.special_chars = ['█', '▓', '▒', '░', '■', '□', '●', '○', '◆', '◇', '★', '☆']
```

### Ajuster les effets
```python
# Vitesse de pulsation du texte
self.pulse_speed = 2.0

# Vitesse des colonnes Matrix
self.speeds.append(random.uniform(0.7, 1.3))

# Intensité des effets
MATRIX_GLOW_INTENSITY = 0.3
```

## 🔧 Développement

### Ajouter de nouveaux effets

1. **Créez une nouvelle méthode** dans la classe appropriée
2. **Ajoutez les paramètres** dans la classe `Config`
3. **Intégrez l'effet** dans la boucle de rendu

### Exemple d'ajout d'effet
```python
def add_custom_effect(self):
    """Ajoute un effet personnalisé"""
    # Votre code ici
    pass
```

### Tests
```bash
# Vérifier la syntaxe
python -m py_compile erreur.py

# Lancer avec debug
python erreur.py --debug
```

## 🐛 Dépannage

### Problèmes courants

**L'application ne se lance pas**
```bash
# Vérifiez que Pygame est installé
pip install pygame

# Assurez-vous d'avoir Python 3.7+
python --version
```

**Performance lente**
- Réduisez `MATRIX_TRAIL_LENGTH` dans la configuration
- Diminuez `GLITCH_COPIES` pour moins d'effets glitch
- Vérifiez que votre GPU supporte l'accélération matérielle

**Police non trouvée**
- L'application utilise automatiquement Consolas en fallback
- Installez des polices supplémentaires si nécessaire

**Erreur de plein écran**
- Essayez en mode fenêtré en modifiant `pygame.FULLSCREEN`
- Vérifiez la résolution de votre écran

## 📊 Performances

### Optimisations implémentées
- **Cache des caractères** : Évite de re-rendre les mêmes caractères
- **Contrôle du framerate** : Limitation à 60 FPS
- **Gestion mémoire** : Nettoyage automatique des ressources
- **Rendu optimisé** : Utilisation de surfaces pré-rendues

### Métriques
- **FPS** : 60 FPS constant
- **Mémoire** : < 100 MB
- **CPU** : < 10% d'utilisation moyenne

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
MIT License - Copyright (c) 2025 Nin-Shinobi
```

## 🤝 Contribution

Les contributions sont les bienvenues ! 

### Comment contribuer

1. **Fork le projet**
2. **Créez une branche** pour votre fonctionnalité
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commettez vos changements**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push vers la branche**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Ouvrez une Pull Request**

### Guidelines
- Respectez le style de code existant
- Ajoutez des commentaires en français
- Testez vos modifications
- Mettez à jour la documentation si nécessaire

## 🙏 Remerciements

- **Pygame** pour le framework de jeu
- **Matrix** pour l'inspiration visuelle
- **La communauté open source** pour les outils et bibliothèques
- **GitHub** pour l'hébergement

## 📞 Contact

- **Auteur** : [𝕹𝖎𝖓_𝕾𝖍𝖎𝖓𝖔𝖇𝖎🥷🏾]
- **GitHub** : [@Nin-Shinobi](https://github.com/Nin-Shinobi)
- **Repository** : [ERREUR_404](https://github.com/Nin-Shinobi/ERREUR_404)

## 🚀 Roadmap

### Fonctionnalités futures
- [ ] Mode fenêtré optionnel
- [ ] Plus d'effets de glitch
- [ ] Support des polices personnalisées
- [ ] Mode nuit/jour
- [ ] Effets sonores
- [ ] Configuration via fichier JSON

---

⭐ **N'oubliez pas de donner une étoile si ce projet vous plaît !** ⭐

---

*Développé avec ❤️ par Nin-Shinobi* 