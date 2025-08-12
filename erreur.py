import pygame
import sys
import time
import random
import math
from typing import List, Tuple, Optional
from dataclasses import dataclass

# Configuration
@dataclass
class Config:
    """Configuration globale de l'application"""
    # Couleurs
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 150, 0)
    BRIGHT_GREEN = (0, 255, 100)
    CYAN = (0, 255, 255)
    WHITE = (255, 255, 255)

    # Polices
    MAIN_FONT_SIZE = 200
    MATRIX_FONT_SIZE = 18
    FONT_NAME = "Consolas"
    # Polices de style HACKER (essayer dans l'ordre)
    STYLISH_FONTS = [
        "Consolas",      # Style terminal/hacker parfait
        "Courier New",   # Style machine à écrire/hacker
        "Lucida Console", # Style console/hacker
        "Terminal",      # Style terminal Windows
        "Fixedsys",      # Style système fixe
        "OCR A Extended", # Style reconnaissance optique
        "Monaco",        # Style monospace élégant
        "Menlo",         # Style monospace moderne
        "Source Code Pro", # Style code source
        "Fira Code",     # Style programmation
        "JetBrains Mono", # Style IDE moderne
        "Cascadia Code", # Style moderne
        "Orbitron",      # Futuriste et technologique
        "Audiowide",     # Style gaming/cyberpunk
        "Russo One",     # Moderne et impactant
        "Chakra Petch",  # Style tech/matrix
        "Rajdhani",      # Élégant et moderne
        "Exo 2",         # Futuriste
        "Impact",        # Impactant et moderne (Windows)
        "Arial Black",   # Gras et moderne (Windows)
        "Verdana",       # Lisible et moderne (Windows)
        "Tahoma",        # Moderne (Windows)
        "Trebuchet MS",  # Moderne (Windows)
        "Georgia",       # Élégant (Windows)
        "Arial",         # Classique (Windows)
        "Times New Roman", # Classique (Windows)
    ]
    
    # Animation
    BLINK_SPEED = 0.5  # secondes
    GLITCH_COPIES = 3  # Réduit de 5 à 3 pour les performances
    MATRIX_RESET_CHANCE = 0.975
    
    # Effet Matrix amélioré
    MATRIX_CHAR_MIN = 33
    MATRIX_CHAR_MAX = 126
    MATRIX_SPEED_VARIATION = 0.3  # Variation de vitesse
    MATRIX_TRAIL_LENGTH = 15  # Longueur de la traînée
    MATRIX_FADE_SPEED = 0.95  # Vitesse de fondu
    MATRIX_GLOW_INTENSITY = 0.3  # Intensité de l'aura

class MatrixRain:
    """Gestion de l'effet de pluie Matrix amélioré"""
    
    def __init__(self, screen: pygame.Surface, config: Config):
        self.screen = screen
        self.config = config
        self.width, self.height = screen.get_size()
        
        # Initialisation des colonnes Matrix avec traînées
        self.columns = self.width // config.MATRIX_FONT_SIZE
        self.drops = []
        self.trails = []
        self.speeds = []
        
        for _ in range(self.columns):
            self.drops.append(random.randint(0, self.height // config.MATRIX_FONT_SIZE))
            self.trails.append([])  # Traînée pour chaque colonne
            self.speeds.append(random.uniform(0.7, 1.3))  # Vitesse variable
        
        # Cache des caractères pour éviter de re-rendre
        self.char_cache = {}
        self.matrix_font = pygame.font.SysFont(config.FONT_NAME, config.MATRIX_FONT_SIZE, bold=True)
        
        # Couleurs améliorées avec dégradés
        self.colors = [
            config.BRIGHT_GREEN,  # Plus lumineux
            config.GREEN,
            config.DARK_GREEN,
            config.CYAN,  # Ajout de cyan
            config.WHITE  # Ajout de blanc pour les caractères spéciaux
        ]
        
        # Caractères spéciaux pour plus de style
        
        self.special_chars = ['█', '▓', '▒', '░', '■', '□', '●', '○', '◆', '◇', '★', '☆']
        self.regular_chars = [chr(i) for i in range(33, 127) if chr(i) not in self.special_chars]
        
        # Effet de fondu pour l'écran
        self.fade_surface = pygame.Surface((self.width, self.height))
        self.fade_surface.set_alpha(int(255 * (1 - config.MATRIX_FADE_SPEED)))
    
    def _get_cached_char(self, char: str, color: Tuple[int, int, int]) -> pygame.Surface:
        """Récupère un caractère du cache ou le rend et l'ajoute au cache"""
        key = (char, color)
        if key not in self.char_cache:
            self.char_cache[key] = self.matrix_font.render(char, True, color)
        return self.char_cache[key]
    
    def _get_random_char(self) -> str:
        """Retourne un caractère aléatoire avec préférence pour les caractères spéciaux"""
        if random.random() < 0.3:  # 30% de chance pour un caractère spécial
            return random.choice(self.special_chars)
        return random.choice(self.regular_chars)
    
    def _get_color_with_glow(self, base_color: Tuple[int, int, int], intensity: float) -> Tuple[int, int, int]:
        """Applique un effet de lueur à une couleur"""
        r, g, b = base_color
        glow_factor = 1 + intensity
        return (
            min(255, int(r * glow_factor)),
            min(255, int(g * glow_factor)),
            min(255, int(b * glow_factor))
        )
    
    def update(self):
        """Met à jour et dessine l'effet Matrix amélioré"""
        # Effet de fondu pour créer une traînée
        self.screen.blit(self.fade_surface, (0, 0))
        
        # Effet de scintillement global
        if random.random() < 0.02:  # 2% de chance de scintillement
            self.screen.fill((0, 50, 0), special_flags=pygame.BLEND_ADD)
        
        for i in range(len(self.drops)):
            # Mise à jour de la position avec vitesse variable
            self.drops[i] += self.speeds[i]
            
            # Génération du caractère principal
            char = self._get_random_char()
            base_color = random.choice(self.colors)
            
            # Position
            x = i * self.config.MATRIX_FONT_SIZE
            y = int(self.drops[i] * self.config.MATRIX_FONT_SIZE)
            
            # Effet de traînée avec dégradé
            trail_length = random.randint(8, self.config.MATRIX_TRAIL_LENGTH)
            for j in range(trail_length):
                trail_y = y - (j * self.config.MATRIX_FONT_SIZE)
                if 0 <= trail_y < self.height:
                    # Caractère de traînée
                    trail_char = self._get_random_char()
                    
                    # Couleur de traînée avec dégradé
                    fade_factor = 1 - (j / trail_length)
                    trail_color = tuple(int(c * fade_factor) for c in base_color)
                    
                    # Effet de lueur pour le premier caractère
                    if j == 0:
                        trail_color = self._get_color_with_glow(trail_color, self.config.MATRIX_GLOW_INTENSITY)
                        # Effet de scintillement pour le premier caractère
                        if random.random() < 0.1:
                            trail_color = self._get_color_with_glow(trail_color, 0.5)
                    
                    # Rendu avec cache
                    char_surface = self._get_cached_char(trail_char, trail_color)
                    self.screen.blit(char_surface, (x, trail_y))
                    
                    # Effet d'ombre pour plus de profondeur
                    if j == 0 and random.random() < 0.3:
                        shadow_surface = self._get_cached_char(trail_char, (0, 20, 0))
                        self.screen.blit(shadow_surface, (x + 1, trail_y + 1))
            
            # Réinitialisation de la colonne
            if y > self.height and random.random() > self.config.MATRIX_RESET_CHANCE:
                self.drops[i] = 0
                self.speeds[i] = random.uniform(0.7, 1.3)  # Nouvelle vitesse aléatoire
                
                # Effet de flash lors de la réinitialisation
                if random.random() < 0.1:
                    flash_surface = pygame.Surface((self.config.MATRIX_FONT_SIZE, self.height))
                    flash_surface.fill((0, 100, 0))
                    flash_surface.set_alpha(50)
                    self.screen.blit(flash_surface, (x, 0))

class GlitchText:
    """Gestion de l'effet de texte glitch avec police stylée"""
    
    def __init__(self, config: Config):
        self.config = config
        self.main_text = "ERREUR 404"
        
        # Sélection de la meilleure police disponible
        self.font = self._get_best_font()
        print(f"Police utilisée: {self.font.get_name() if hasattr(self.font, 'get_name') else 'Police système'}")
        
        # Cache des surfaces de texte
        self.text_cache = {}
        self._create_text_surfaces()
        
        # Effet de pulsation
        self.pulse_time = 0
        self.pulse_speed = 2.0
        
    def _get_best_font(self) -> pygame.font.Font:
        """Trouve la meilleure police disponible dans la liste"""
        for font_name in self.config.STYLISH_FONTS:
            try:
                # Essaie de charger la police
                font = pygame.font.SysFont(font_name, self.config.MAIN_FONT_SIZE, bold=True)
                # Test si la police fonctionne
                test_surface = font.render("TEST", True, (0, 255, 0))
                if test_surface.get_width() > 0:
                    print(f"Police trouvée: {font_name}")
                    return font
            except Exception as e:
                print(f"Police {font_name} non disponible: {e}")
                continue
        
        # Fallback vers Consolas
        print("Utilisation de Consolas comme fallback")
        return pygame.font.SysFont("Consolas", self.config.MAIN_FONT_SIZE, bold=True)
    
    def _create_text_surfaces(self):
        """Crée les surfaces de texte avec différents effets"""
        # Texte principal
        self.main_surface = self.font.render(self.main_text, True, self.config.GREEN)
        self.text_rect = self.main_surface.get_rect()
        
        # Texte avec ombre
        self.shadow_surface = self.font.render(self.main_text, True, (0, 50, 0))
        
        # Texte avec contour
        self.outline_surface = self._create_outline_text()
        
        # Cache pour les effets glitch
        self.glitch_cache = {}
    
    def _create_outline_text(self) -> pygame.Surface:
        """Crée un texte avec contour"""
        # Surface légèrement plus grande pour le contour
        outline_size = (self.text_rect.width + 8, self.text_rect.height + 8)
        outline_surface = pygame.Surface(outline_size, pygame.SRCALPHA)
        
        # Dessine le contour en plusieurs couches
        outline_color = (0, 100, 0)
        for offset in [(2, 2), (-2, 2), (2, -2), (-2, -2), (0, 2), (0, -2), (2, 0), (-2, 0)]:
            outline_surface.blit(self.font.render(self.main_text, True, outline_color), 
                               (offset[0] + 4, offset[1] + 4))
        
        # Texte principal au centre
        outline_surface.blit(self.main_surface, (4, 4))
        return outline_surface
    
    def _get_glitch_surface(self, color: Tuple[int, int, int]) -> pygame.Surface:
        """Récupère ou crée une surface glitch"""
        if color not in self.glitch_cache:
            self.glitch_cache[color] = self.font.render(self.main_text, True, color)
        return self.glitch_cache[color]
    
    def draw(self, screen: pygame.Surface, center_x: int, center_y: int):
        """Dessine le texte avec effets avancés"""
        current_time = time.time()
        
        # Effet de pulsation
        pulse_factor = 1.0 + 0.1 * math.sin(current_time * self.pulse_speed)
        scaled_size = (int(self.text_rect.width * pulse_factor), 
                      int(self.text_rect.height * pulse_factor))
        
        # Position centrale
        self.text_rect.center = (center_x, center_y)
        
        # Ombre portée
        shadow_rect = self.shadow_surface.get_rect(center=(center_x + 3, center_y + 3))
        screen.blit(self.shadow_surface, shadow_rect)
        
        # Contour avec effet de lueur
        outline_rect = self.outline_surface.get_rect(center=(center_x, center_y))
        screen.blit(self.outline_surface, outline_rect)
        
        # Texte principal avec pulsation
        if pulse_factor != 1.0:
            # Redimensionne le texte pour l'effet de pulsation
            scaled_surface = pygame.transform.scale(self.main_surface, scaled_size)
            scaled_rect = scaled_surface.get_rect(center=(center_x, center_y))
            screen.blit(scaled_surface, scaled_rect)
        else:
            screen.blit(self.main_surface, self.text_rect)
        
        # Effet glitch amélioré
        for i in range(self.config.GLITCH_COPIES):
            glitch_x = center_x + random.randint(-12, 12)
            glitch_y = center_y + random.randint(-6, 6)
            
            # Couleurs glitch variées
            if i == 0:
                glitch_color = (0, random.randint(200, 255), 0)  # Vert lumineux
            elif i == 1:
                glitch_color = (0, random.randint(150, 200), random.randint(100, 150))  # Cyan
            else:
                glitch_color = (0, random.randint(100, 150), 0)  # Vert sombre
            
            # Effet de décalage horizontal aléatoire
            if random.random() < 0.3:
                glitch_x += random.randint(-20, 20)
            
            # Rendu avec cache
            glitch_surface = self._get_glitch_surface(glitch_color)
            glitch_rect = glitch_surface.get_rect(center=(glitch_x, glitch_y))
            screen.blit(glitch_surface, glitch_rect)
            
            # Effet de transparence pour certains glitch
            if i > 0 and random.random() < 0.5:
                temp_surface = glitch_surface.copy()
                temp_surface.set_alpha(128)
                screen.blit(temp_surface, glitch_rect)

class Error404App:
    """Application principale ERREUR 404"""
    
    def __init__(self):
        pygame.init()
        
        # Configuration
        self.config = Config()
        
        # Initialisation de l'écran
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("ERREUR 404 - MATRIX MODE")
        
        # Composants
        self.matrix_rain = MatrixRain(self.screen, self.config)
        self.glitch_text = GlitchText(self.config)
        
        # État de l'application
        self.show_text = True
        self.last_blink = time.time()
        self.running = True
        
        # Dimensions de l'écran
        self.width, self.height = self.screen.get_size()
    
    def handle_events(self):
        """Gestion des événements"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update_blink(self):
        """Met à jour l'état de clignotement du texte"""
        current_time = time.time()
        if current_time - self.last_blink > self.config.BLINK_SPEED:
            self.show_text = not self.show_text
            self.last_blink = current_time
    
    def render(self):
        """Rendu de la frame"""
        # Fond noir
        self.screen.fill(self.config.BLACK)

    # Effet Matrix
        self.matrix_rain.update()
        
        # Texte glitch (si visible)
        if self.show_text:
            self.glitch_text.draw(self.screen, self.width // 2, self.height // 2)
        
        # Mise à jour de l'affichage
        pygame.display.flip()
    
    def run(self):
        """Boucle principale de l'application"""
        try:
            while self.running:
                self.handle_events()
                self.update_blink()
                self.render()
                
                # Contrôle du framerate pour éviter une utilisation excessive du CPU
                pygame.time.Clock().tick(60)
        
        except KeyboardInterrupt:
            print("Arrêt demandé par l'utilisateur")
        except Exception as e:
            print(f"Erreur inattendue: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Nettoyage des ressources"""
        pygame.quit()
        sys.exit()

def main():
    """Point d'entrée principal"""
    try:
        app = Error404App()
        app.run()
    except Exception as e:
        print(f"Erreur lors du démarrage: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
