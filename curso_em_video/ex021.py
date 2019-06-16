#Solução do professor: uso do pygame
import pygame
pygame.init() #necessário para iniciar
pygame.mixer.music.load('your_mp3_here.mp3')
pygame.mixer.music.play()
pygame.event.wait()