#Carregar e executar um arquivo mp3.
#/home/mychelgs/Área de Trabalho/Gil/Estudo Python/cursoemvideo
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()


